# This project emphasis on certain software tools and packages to be integrated to conduct analysis of the spectral data. The programming requirement for this analysis is aided by python and packages.

## Creating Virtual environments
A virtual environment for python is useful to isolate spectral libraries and packages the project depends on.It provides security for the main system of the PC and creates a cleaner structural management of the project. To install a Virtual environment for spectral in Linux :
1. Check if python3 is installed:
    - python3 --version
2. If python is not installed do:
    - sudo apt-get install python3
3. Install the Virtual environment module:
    - sudo apt-get install python3-venv
4. Create Virtual Environment:
    - python3 -m venv env

### Activate the Virtual environment after env is created in the directory.
5. To activate the Virtual environment:
    - source env/bin/activate
6. Check if the env is active by:
    - which python

Install any packages that the project requires and run program.

7. After finishing the certain task, deactivate env:
    - deactivate

## Software tools and libraries
This project uses spectral python to practice and run implementation with spectral data recorded by images. The software tools and packages needed for this project are:
1. Python 3.3 -> spectral python requires python 3 for the function to work.
2. NumPy
3. PIL/pillow -> to display and save spectral images.
4. matplotlib -> to plot graphs of the spectral data.
5. Jupyter Notebook -> to do interactive computing by using a inbuilt GUI.
   
This project may require more packages during it progress during and will be updated. Spy requires wxPython if cube view of the spectral data, which is not required in this project.

## Downloading these tools in Linux 
### Installing spectral package
1. Activate the virtual environment:
    - source /path/to/your/venv/bin/activate
2. Install spectral Python: 
    - pip install spectral
3.  verify the packages are install by moving and viewing the Python site packages in env

### Installing other Imaging and plotting package 
1. Install Pillow:
    - pip install Pillow
2. Install matplotlib:
    - pip install matplotlib

### Installing Jupyter notebook
1. Activate the virtual environment:
    - source /path/to/your/venv/bin/activate
2. Install Jupyter:
    - pip install jupyter
3. Install ipyKernal:
    - pip install ipykernel
4. Add virtual environment as a Kernal:
    - python -m ipykernel install --user --name=env
5. Add Jupyter kernal to vscode or directly start the notebook:
    - jupyter notebook

## Windows Subsystem for Linux (WSL) on a Windows machine requirement
This project requires the spectral imager Specim fx10e to be used. This requires either a SDK or a pre installed to be used. These software tools run on windows operating system and the Linux system is very efficient in programming on the spectral data. Therefore a mix of 2 operating system is may be used. This can be done through installing a WSL which allows a Linux terminal to be used in windows. 

