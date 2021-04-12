# Agent Build System
___

Mechanism for creating agents that are based on collected data.

___

To Execute Default ABS Component (*Builder*): 
* Windows:

  *python GUI_manager.py*
	
* Linux:

  *python3 GUI_manager.py*

To Execute Another ABS Component (*Causation Extractor*,*Runner*) add component name to end of command:
* Windows Example:

  *python GUI_manager.py* **ce**
	
* Linux Example:

  *python3 GUI_manager.py* **runner**

To Load Project in Builder Component:
* Windows:

  *python GUI_manager.py builder* **Project_Folder**
	
* Linux:

  *python3 GUI_manager.py builder* **Project_Folder**
