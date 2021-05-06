# Causation Extractor Component (CE)

### Using the Causation Extractor (TL;DR)
In a typical use case: the following steps must be taken in order to use the Causation Extractor

1. CLick the "Save Project" button and enter a unique project name
2. Click the "Browse" button and select an ECELd Project
3. Enter a Time Frame (in seconds) in the input box next to "Time Frame" **(OPTIONAL)**
4. Click the "Project" menubar item at the top of the ABS GUI and select "Import JSON File" then select a valid Salient Artifact JSON file. **(OPTIONAL)**
5. CLick the "Analyze" button.

### Creating Relationships

The CE Component is capable of creating time-based causal relationships from the ECELd data captures.

A relationship is defined as an observation in data captures that may be the cause of user actions. In order to do this, the CE requires that the user browses their system and selects a ECELd Project folder that contains captured information. 

In order to create relationships: the user must select the top level folder for the ECELd Project (i.e if the user wants to use the project data within a ECELd Project named "Acosta", they must select the folder named "Acosta" NOT any of the folders located within that project folder).

### Modifying Salient Artifact Engine

The CE allows users to enter their own definitions for Salient artifacts. If the user would like to enter their own Salient Artifact Definition, you can select a json file that is located on your system with the following format

> "eceld_data_header": "value"

If no file is entered, the System will instead rely on a "default" json file to determine Salient Artifacts. 

### Modifying Time Frame Attribute
The user can modify the time frame between salient artifacts and the subsequent actions by entering a new value within the CE window's "Time Frame" field. Users are able to enter any numerical value that will get interpreted in seconds (i.e if an user enters '1', then the time frame per relationship will be 1 second)

By default this value is *5 seconds*.

### Required Fields
Out of the possible fields described above, the only field required is selecting an ECELd Project.