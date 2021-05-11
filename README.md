# Agent Build System (ABS)

## System Requirements
The Agent Build System has been tested and developed to function primarily on Kali Linux and Windows 10, functionality on *any* other operating system, future or past, is not guaranteed. Please also ensure that you have at LEAST python 3.9 installed and at LEAST 10GB of Storage Space available on your device prior to setting up the Agent Build System from source.

* Kali Linux 2020.2 64-bit
* Windows 10
* [Python 3 >= 3.8](https://www.python.org/downloads/release/python-383/

## Setting up from source

1. Unzip the repository into your directory of choosing and enter the "Agent-Build-System" folder.

2. When you enter the folder enter the following command
```
sudo ./install.sh
```
This will run a check for and install any dependencies that may not already be included within the system. 


## Run the Executable
The executable MUST be ran with root/admin privileges. You can run it with the following command:
```
sudo ./Agent-Build-System ce
```
The command above will start the *Causation Extractor* Component.


## Running Components
The executable allows you to start at any of the components within the Agent Build System without having to go through the typical sequence. In order to do this, you must type the same command as above, but replace the final portion with the name of the component that you would like to run. (Causation extractor is shortened to 'ce', the builder and runner are their respective names). So if an user would want to go straight to the Runner, they would type the following command
```
sudo ./agent-build-system runner
```
##### NOTE: all component names must be in **lowercase**. 
 
## Loading a Project from the Terminal
The executable allows you to open a project within both the Builder and the Runner via the terminal interface as well. In order to do this, you must type in the name of the project *after* the name of the component. So if an user would want to open the project "practicum" inside of the builder when starting the builder, they would type the following command
```
sudo ./agent-build-system builder practicum
```
