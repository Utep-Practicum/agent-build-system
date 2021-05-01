from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow

from Causation_Extractor.CE_GUI import *

from Builder.Controller import *
from Builder.Builder_GUI import *
from Builder.Relation import *
from Runner.Runner_GUI import *
from Runner.Runner_Manager import *

class GUIManager(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = None
        self.project = None


    def causation_extractor(self):
        self.ui = CEGUI()
        self.w = Window
        self.ui.setupUi(self.w)
        self.w.show()
        
        

    def builder(self,name = None):
        controller = Controller()
        if name == None:
            Builder_GUI(controller)
        else:
            self.project = name
            controller = Controller()
            controller.update(self.project)

            # I already got the relations
            # pass them to the Builder_GUI
            Builder_GUI(controller)

        # This is just a print...
        for relation in controller.relationships_main:
            print(relation.name)


    def runner(self,name = None):
        self.project = name
        #These lines are only to test the Runner
        #Remove upon test completion
        temp = Controller()
        temp.update(self.project)
        rel_lst = temp.relationships_main[0]
        RunnerManager(rel_lst.observation_list).runner_review()

        """
        self.runner = Runner_GUI()
        self.r = Window
        self.runner.setupUi(self.r)
        self.r.show()
        """

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    Window.show()
    manager = GUIManager()
    function = {'ce':manager.causation_extractor,
                'builder':manager.builder,
                'runner':manager.runner}
    if len(sys.argv) == 2:
        function[sys.argv[1]]()
    elif len(sys.argv) == 3:
        function[sys.argv[1]](sys.argv[2])
    else:
        manager.builder()
    sys.exit(app.exec())