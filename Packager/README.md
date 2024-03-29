# Packager Component

### Export all project elements

  - Allows user to select Virtual Machines and Files that are part of a project for packaging in a zip file.

### Import ABS Project elements

  - Allows user to select an ABS packaged project (zip file format) and extract its file contents and import machines to VirtualBox.

### The Packager.exe is meant to be executed on the host machine, outside the sandbox environment.**

[Packager.exe zip folder] (https://drive.google.com/file/d/1gpIKhTxKZ_noCM6cAqphoth7miSNaa7M/view?usp=sharing)

System Requirements:

* VirtualBox Software Developer Kit (SDK) Package

  [Virtual Box Downloads Page] (https://www.virtualbox.org/wiki/Downloads)
  
* Add VBoxManage to PATH variable
  
  - Windows Powershell with Admin Privileges Command:
  
    _set PATH=%PATH%;"[Path to Oracle\VirtualBox\ Directory]"_
  
  - Manual Process:
    
    - Search for *"Edit the system environment variables"* in start menu
    
    - *System Properties* Window
    
      Select *Environment Variables...*
    
    - In *Environment Variables* window, under the *System variables* Box, Select *Path*
    
    - *Edit environment variable* window will open
    
      Select *New*
    
      Paste the location of *Oracle\VirtualBox* directory
  
  
  <sub>Default Location of VirtualBox Directory: C:\Program Files\Oracle\VirtualBox\ </sub>
    
