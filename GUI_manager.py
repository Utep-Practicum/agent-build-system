from Builder.Controller import *
from Builder.Builder_GUI import *

if __name__ == "__main__":
    project = '/Users/Rick/Desktop/My Documents/VSCode/Practicum/agent-build-system/Project Data/test0'
    controller = Controller()
    controller.update(project)

    # I already got the relations
    # pass them to the Builder_GUI
    builder_window = Ui_BuilderWindow(controller)

    # This is just a print...
    for relation in controller.relationships_main:
        print(relation.name)

# main should start builder
# others should call the different methods