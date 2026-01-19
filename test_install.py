"""
Check if all dependendencies are installed
"""

import importlib
from typing import List, Tuple, Optional, Dict, Any

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

MODULES_TO_CHECK: List[str] = [
        "numpy",
        "scipy",
        "torch",
        "sklearn",
        "matplotlib",
        "tqdm",
        "roboticstoolbox",
        "mediapy",
        "gym",
        "spatialmath",
        "machinevisiontoolbox",
        "plotly",
        "torchvision",
        "tensorboardX",
        "pynput",
        "click"
]

def print_coloured(text:str,colour_code:str,*args,**kwargs):
    try:
        print(colour_code + text + bcolors.ENDC,*args,**kwargs)
    except KeyboardInterrupt as e:
        raise KeyboardInterrupt
    except Exception as e:
        # For OS's that don't support the control characters.
        print(text,*args,**kwargs)

def check_import(module_name: str) -> Tuple[bool, Optional[str], Optional[str]]:
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", "unknown")
        return True, version, None
    except Exception as e:
        return False, None, str(e)


def check_cuda() -> Tuple[bool, str, Optional[Dict[str, Any]]]:
    """
    Returns:
      ok: True if the CUDA check ran (torch import worked), False otherwise
      message: one-line summary
      info: detailed info dict when available
    """
    try:
        import torch  # type: ignore

        cuda_available = bool(torch.cuda.is_available())
        torch_version = getattr(torch, "__version__", "unknown")
        cuda_version = getattr(getattr(torch, "version", None), "cuda", None)
        num_devices = int(torch.cuda.device_count()) if cuda_available else 0

        info: Dict[str, Any] = {
            "cuda_available": cuda_available,
            "torch_version": torch_version,
            "cuda_version": cuda_version,
            "num_devices": num_devices,
            "devices": [],
        }

        if cuda_available:
            for i in range(num_devices):
                name = torch.cuda.get_device_name(i)
                capability = torch.cuda.get_device_capability(i)
                info["devices"].append(
                    {"id": i, "name": name, "capability": capability}
                )

            message = f"CUDA AVAILABLE ({num_devices} GPU{'s' if num_devices != 1 else ''})"
        else:
            message = "CUDA NOT available (CPU only)"

        return True, message, info

    except ImportError:
        return False, "PyTorch not installed (cannot check CUDA)", None
    except Exception as e:
        return False, f"CUDA check failed: {e}", None

def check_dataset() -> Tuple[bool, str, Optional[str]]:
    """
    Returns:
        ok: True if dataset is found, False otherwise
        message: one-line summary
        info: extra info
    """
    import os
    retry_message = "Please run pixi run get_dataset"

    train_path = os.path.join("data", "train_starter")
    val_path = os.path.join("data", "val_starter")

    train_size = os.listdir(train_path) if os.path.exists(train_path) else []
    val_size = os.listdir(val_path) if os.path.exists(val_path) else []

    if len(train_size) == 0 or len(val_size) == 0:
        return False, "Dataset not found", retry_message
    elif len(train_size) != 793 or len(val_size) != 436:
        return False, "Dataset partially downloaded", retry_message
    else:
        return True, "Dataset found and complete", None




def main():
    print("=" * 60)
    print("Environment Import Check")
    print("=" * 60)

    ok, fail = 0, 0

    for mod in MODULES_TO_CHECK:
        success, version, error = check_import(mod)

        if success:
            ok += 1
            print_coloured(f"{mod:<15} imported successfully (version: {version})", bcolors.OKGREEN)
        else:
            fail += 1
            print_coloured(f"{mod:<15} FAILED to import", bcolors.FAIL)
            print_coloured(f"   ↳ {error}", bcolors.FAIL)

    print("-" * 60)
    cuda_ok, cuda_msg, cuda_info = check_cuda()

    if not cuda_ok:
        print_coloured(cuda_msg, bcolors.WARNING)
    else:
        if cuda_info and cuda_info.get("cuda_available", False):
            print_coloured(f"{cuda_msg}", bcolors.OKGREEN)
            print(f"   Torch version : {cuda_info.get('torch_version')}")
            print(f"   CUDA version  : {cuda_info.get('cuda_version')}")
            print(f"   # GPUs        : {cuda_info.get('num_devices')}")

            for dev in cuda_info.get("devices", []):
                print(
                    f"   • GPU {dev['id']}: {dev['name']} "
                    f"(compute capability {dev['capability']})"
                )
        else:
            print_coloured(f"{cuda_msg}", bcolors.WARNING)
            if cuda_info:
                print(f"   Torch version : {cuda_info.get('torch_version')}")
                print("   Running on CPU only")

    print("-" * 60)
    print(f"Summary: {ok} OK, {fail} FAILED")

    if fail == 0:
        print_coloured("All imports look good. Environment is ready.", bcolors.OKGREEN)
    else:
        print_coloured("Some imports failed. Check your environment.", bcolors.WARNING)

    print("=" * 60)

    print("Dataset Check")
    print("=" * 60)
    data_ok, data_msg, data_info = check_dataset()
    if data_ok:
        print_coloured(f"{data_msg}", bcolors.OKGREEN)
    else:
        print_coloured(f"{data_msg}", bcolors.FAIL)
        if data_info:
            print_coloured(f"   ↳ {data_info}", bcolors.FAIL)
    print("=" * 60)



if __name__ == "__main__":
    main()

