# Workshop setup - before you arrive

Please follow each of the steps below before arriving at RVSS:
- [Clone the repository](#clone-the-repository)
- [Download the starter data](#download-the-starter-data)
- [Use Conda for package management](#use-conda-for-package-management)
- [Setup an RVSS conda environment](#setup-an-rvss-conda-environment)
- [Download Visual Studio Code for code development](#download-visual-studio-code-for-code-development)

# Clone the repository
Before you attend the workshop, you will need a copy of this repository on your personal laptop. Clone the repository into your chosen folder on your personal laptop with this terminal command:

`git clone --recurse-submodules https://github.com/rvss-australia/RVSS_Need4Speed.git`

# Download the starter data
Navigate to the [huggingface dataset](https://huggingface.co/datasets/dimitym/RVSS_Need4Speed_starter/tree/main) and download data.zip. Place this inside your cloned repository and extract the zip file.

You should have a `data` folder that contains a `train_starter` and `val_starter` folder, containing 793 and 436 images respectively.

# Use Conda for package management
In this workshop, we will use Conda. Conda is a package manager for Windows, Mac and Linux - it allows you to install packages similar to `apt`, `homebrew` and `vcpkg`. Conda not only supports Python packages, but also packages in C/C++, FORTRAN, and much more.

Nothing that can be done with conda cannot be achieved otherwise. However, with conda it is usually easier and cross-platform.

Conda handles dependencies seamlessly and makes it easy to set up different environments with different versions of libraries.

Conda is also an environment manager (like `virtualenv`). Therefore, if an environment is ruined beyond repair, you can just remove it and start over with a clean one.

## Guide for setting up Conda with conda-forge
- We strongly recommend using the community-driven `conda-forge` channel, instead of the `defaults` channel that is maintained by Anaconda. 
- The easiest way to install conda with conda-forge as default channel is with `Miniforge3`. You can download the installers from [here](https://github.com/conda-forge/miniforge#miniforge3).
- If you are on Linux/MacOS, simply type `sh Miniforge3-*.sh` and follow the instructions. On Windows, double click `Miniforge3-Windows-x86_64.exe` and follow the instructions.

# Setup an RVSS conda environment
- Linux/MacOS: Create a new environment called `rvss` with all required packages: `mamba create -n rvss numpy scipy pytorch scikit-learn ipython scikit-image matplotlib tqdm roboticstoolbox-python git ipykernel mediapy py-opencv seaborn gym jupyter spatialmath-python machinevision-toolbox-python ipywidgets plotly torchvision conda-pack tensorboardx pynput click -c conda-forge --override-channels`.
- Windows: Create a new environment called `rvss` with all required packages: `mamba create -n rvss numpy scipy pytorch pytorch-cuda scikit-learn ipython scikit-image matplotlib tqdm roboticstoolbox-python git ipykernel mediapy py-opencv seaborn gym jupyter spatialmath-python machinevision-toolbox-python ipywidgets plotly torchvision conda-pack tensorboardx pynput click -c pytorch -c conda-forge -c nvidia`. 
- Linux/Windows with GPU (optional as this should happen automatically): Replace `pytorch` with `pytorch-gpu` above to enforce a GPU version of `pytorch`.
- Windows: You may need to enable [long path lengths](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#application-manifest-updates-to-declare-long-path-capability) if you get an error when creating the environment.
## Working with the environment:
- Activating the environment you just created: `conda activate rvss`
- Deactivating: `conda deactivate rvss`
- Deleting an environment: `conda remove --name FAILED_ENVIRONMENT --all`

# Download Visual Studio Code for code development
We strongly recommend downloading Visual Studio Code to use as your code editor during the workshop. You can download VS Code [here]( https://code.visualstudio.com/). Please install at least the following two extensions: Python and Remote - SSH.
