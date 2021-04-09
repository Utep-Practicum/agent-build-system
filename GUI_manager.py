from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow

from Causation_Extractor.CE_GUI import *
#from Causation_Extractor.Analysis_GUI import *

from Builder.Controller import *
from Builder.Builder_GUI import *
from Builder.Relation import *

class GUIManager(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = None
        self.project = None


    def causation_extractor(self):
        #CEGUI().execute()
        
        ui = CEGUI()
        self.w = Window
        ui.setupUi(self.w)
        self.w.show()
        
        

    def builder(self):
        project = '/Users/Rick/Desktop/My Documents/VSCode/Practicum/agent-build-system/Project Data/test12'
        controller = Controller()
        controller.update(project)

        # I already got the relations
        # pass them to the Builder_GUI
        builder_window = Ui_BuilderWindow(controller)

        # This is just a print...
        for relation in controller.relationships_main:
            print(relation.name)


    def runner(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    Window.show()
    manager = GUIManager()
    manager.causation_extractor()
    sys.exit(app.exec())
    
    # main should start builder
    # others should call the different methods