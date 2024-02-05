# Workshop setup - before you arrive

# Clone the repository
Before you attend the workshop, you will need a copy of this repository on your personal laptop. Clone the repository into your chosen folder on your personal laptop with this terminal command:

`git clone --recurse-submodules https://github.com/rvss-australia/RVSS_Need4Speed.git`

# Using Conda for package management
In this workshop, we will use Conda. Conda is a package manager for Windows, Mac and Linux - it allows you to install packages similar to `apt`, `homebrew` and `vcpkg`. Conda not only supports Python packages, but also packages in C/C++, FORTRAN, and much more.

Nothing that can be done with conda cannot be achieved otherwise. However, with conda it is usually easier and cross-platform.

Conda handles dependencies seamlessly and makes it easy to set up different environments with different versions of libraries.

Conda is also an environment manager (like `virtualenv`). Therefore, if an environment is ruined beyond repair, you can just remove it and start over with a clean one.

## Guide for setting up Conda with conda-forge
- We strongly recommend using the community-driven `conda-forge` channel, instead of the `defaults` channel that is maintained by Anaconda. 
- The easiest way to install conda with conda-forge as default channel is with `Miniforge3`. You can download the installers from [here](https://github.com/conda-forge/miniforge#miniforge3).
- If you are on Linux/MacOS, simply type `sh Miniforge3-*.sh` and follow the instructions. On Windows, double click `Miniforge3-Windows-x86_64.exe` and follow the instructions.

# Guide for setting up an RVSS conda environment
- If you have a CPU machine without GPU, create a new environment called `rvss` with all required packages: `mamba create -n rvss numpy scipy pytorch scikit-learn ipython scikit-image matplotlib tqdm roboticstoolbox-python git ipykernel mediapy py-opencv seaborn gym jupyter spatialmath-python machinevision-toolbox-python ipywidgets plotly torchvision conda-pack tensorboardx pynput click -c conda-forge`.
- If you have a GPU machine (on Linux), consider replacing `pytorch` with `pytorch-gpu` above to enforce a GPU version of `pytorch` (this should happen automatically though).
- If you have a GPU machine (on Windows), please use: `mamba create -n rvss numpy scipy 'pytorch=*=*cuda*' scikit-learn ipython scikit-image matplotlib tqdm roboticstoolbox-python git ipykernel mediapy py-opencv seaborn gym jupyter spatialmath-python machinevision-toolbox-python ipywidgets plotly torchvision conda-pack tensorboardx pynput click pytorch-cuda=11.8 cuda-version=11.8 -c conda-forge -c pytorch -c nvidia`

## Working with the environment:
- Activating the environment you just created: `conda activate rvss`
- Deactivating: `conda deactivate rvss`
- Deleting an environment: `conda remove --name FAILED_ENVIRONMENT --all`
