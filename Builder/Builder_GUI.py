# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Builder_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from Builder.EditForm import *
from Builder.Controller import *
from Builder.EditForm import *
from Builder.script_generator import *

import json
import sys
import copy
from subprocess import Popen,PIPE
import platform



def enable_button(button):
    button.setEnabled(True)
    button.setStyleSheet("background-color: rgba(18, 51, 62, 100%); color: #FFFFFF; border-radius: 5px;")

def disable_button(button):
    button.setEnabled(False)
    button.setStyleSheet("background-color: rgba(18, 51, 62, 50%); color: #FFFFFF; border-radius: 5px;")


class Builder_GUI(object):

    def __init__(self, controller):
        self.controller_object = controller
        self.undo_stack = []
        self.dependency = ""
        self.undo_stack = []
        self.selected_item  = None
        self.relations_list = controller.relationships_main
        self.relation_selected = None
        if __name__ != "__main__":
            self.execute()

    def setupUi(self, BuilderWindow):
        BuilderWindow.setObjectName("BuilderWindow")
        BuilderWindow.resize(778, 750)
        BuilderWindow.setStyleSheet("background-color: #f4f5f7;")
        self.centralwidget = QtWidgets.QWidget(BuilderWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(778, 720))
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()

        ######################### Search Label #########################
        self.search_label = QtWidgets.QLabel(self.centralwidget)
        self.search_label.setGeometry(QtCore.QRect(20, 14, 281, 23))
        font.setPointSize(14)
        self.search_label.setFont(font)
        self.search_label.setStyleSheet("color:black;")
        self.search_label.setObjectName("search_label")

        ######################### Search Input #########################
        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(20, 40, 721, 40))
        self.search_input.setObjectName("search_input")
        self.search_input.setStyleSheet(
            "background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.search_input.textChanged.connect(self.display_search_results)

        ######################### Detail List #########################
        self.details_list = QtWidgets.QListWidget(self.centralwidget)
        self.details_list.setGeometry(QtCore.QRect(20, 431, 721, 221))
        self.details_list.setObjectName("details_list")
        self.details_list.setStyleSheet(
            "background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.details_list.setDragEnabled(True)

        ##################### Relationships Label ##################################
        self.relationships_label = QtWidgets.QLabel(self.centralwidget)
        self.relationships_label.setGeometry(QtCore.QRect(20, 92, 291, 23))
        font.setPointSize(14)
        self.relationships_label.setFont(font)
        self.relationships_label.setStyleSheet("color:black;")
        self.relationships_label.setObjectName("label")

        ##################### Relationship List Widget ##########################
        self.relationship_list = QtWidgets.QListWidget(self.centralwidget)
        self.relationship_list.setGeometry(QtCore.QRect(20, 120, 291, 293))
        self.relationship_list.setObjectName("relationship_list")
        self.relationship_list.setStyleSheet(
            "background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")

        ######################### Dependencies Label#########################
        self.dependencies_label = QtWidgets.QLabel(self.centralwidget)
        self.dependencies_label.setGeometry(QtCore.QRect(460, 92, 281, 23))
        font.setPointSize(14)
        self.dependencies_label.setFont(font)
        self.dependencies_label.setStyleSheet("color:black;")
        self.dependencies_label.setObjectName("dependencies_label")

        ##################### Dependencies List Widget ######################
        self.dependency_list = QtWidgets.QListWidget(self.centralwidget)
        self.dependency_list.setGeometry(QtCore.QRect(460, 120, 281, 293))
        self.dependency_list.setObjectName("dependency_list")
        self.dependency_list.setStyleSheet(
            "background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.dependency_list.setDragEnabled(True)

        ################### Play Button #########################
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(660, 0, 81, 31))
        self.playButton.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.playButton.setObjectName("playButton")
        self.playButton.clicked.connect(self.open_runner)
        self.playButton.clicked.connect(BuilderWindow.close)

        ##################### Relationship -> Dependency Button #####################
        self.move_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_button.setGeometry(QtCore.QRect(340, 130, 100, 75))
        self.move_button.setMinimumSize(QtCore.QSize(100, 75))
        font.setPointSize(16)
        self.move_button.setFont(font)
        self.move_button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.move_button.setObjectName("move_button")
        self.move_button.clicked.connect(self.pass_dependency)
        BuilderWindow.setCentralWidget(self.centralwidget)

        ##################### Dependency -> Relationship Button #####################
        self.move_button_back = QtWidgets.QPushButton(self.centralwidget)
        self.move_button_back.setGeometry(QtCore.QRect(340, 220, 100, 75))
        self.move_button_back.setMinimumSize(QtCore.QSize(100, 75))
        font.setPointSize(16)
        self.move_button_back.setFont(font)
        self.move_button_back.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.move_button_back.setObjectName("move_button")
        self.move_button_back.clicked.connect(self.pass_relationship)
        BuilderWindow.setCentralWidget(self.centralwidget)

        ##################### Undo Button #####################
        self.undo_button = QtWidgets.QPushButton(self.centralwidget)
        self.undo_button.setGeometry(QtCore.QRect(340, 310, 100, 75))
        self.undo_button.setMinimumSize(QtCore.QSize(100, 75))
        font.setPointSize(16)
        self.undo_button.setFont(font)
        self.undo_button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.undo_button.setObjectName("move_button")
        self.undo_button.clicked.connect(self.undo_controller_state)
        BuilderWindow.setCentralWidget(self.centralwidget)

        ##################### Edit Artifact Button #################################
        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(25, 660, 50, 41))
        self.edit_button.setMinimumSize(QtCore.QSize(100, 41))
        font.setPointSize(16)
        self.edit_button.setFont(font)
        self.edit_button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.edit_button.setObjectName("edit_button")
        self.edit_button.clicked.connect(self.edit_observation)

        ##################### Delete Artifact Button ################################
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(150, 660, 50, 41))
        self.delete_button.setMinimumSize(QtCore.QSize(100, 41))
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.delete_button.setObjectName("delete_button")
        self.delete_button.clicked.connect(self.delete_observation)

        ##################### Ignore Artifact Button ################################
        self.ignore_button = QtWidgets.QPushButton(self.centralwidget)
        self.ignore_button.setGeometry(QtCore.QRect(275, 660, 50, 41))
        self.ignore_button.setMinimumSize(QtCore.QSize(100, 41))
        self.ignore_button.setFont(font)
        self.ignore_button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.ignore_button.setObjectName("ignore_button")
        self.ignore_button.clicked.connect(self.ignore_observation)

        ##################### Generate Script Button ################################
        self.script_button = QtWidgets.QPushButton(self.centralwidget)
        self.script_button.setGeometry(QtCore.QRect(500, 660, 241, 41))
        font.setPointSize(14)
        self.script_button.setFont(font)
        self.script_button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.script_button.setObjectName("script_button")
        # self.script_button.clicked.connect(self.show_analyzingWindow)
        self.script_button.clicked.connect(self.generate_script)

        ###################### Menu Top Bar #########################################
        self.menubar = QtWidgets.QMenuBar(BuilderWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 21))
        self.menubar.setObjectName("menubar")

        ######################Project Top Bar Dropdown ##############################
        self.menu_project = QtWidgets.QMenu(self.menubar)
        self.menu_project.setObjectName("menu_project")
        BuilderWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BuilderWindow)
        self.statusbar.setObjectName("statusbar")
        BuilderWindow.setStatusBar(self.statusbar)


        ###################### Import Project Menu Option #############################
        self.action_import_project = QtWidgets.QAction(BuilderWindow)
        self.action_import_project.setObjectName("action_import_project")
        self.menu_project.addAction(self.action_import_project)
        self.menu_project.setStyleSheet("color: black")  # modified submenu font to be black -seb
        self.action_import_project.triggered.connect(self.import_project)  # function gets ran at click -seb

        ###################### Load Project Option ##################################
        self.action_load = QtWidgets.QAction(BuilderWindow)
        self.action_load.setObjectName("action_load")
        self.action_load.setText("Load Object")
        self.menu_project.addAction(self.action_load)
        self.menu_project.setStyleSheet("color: black")
        self.action_load.triggered.connect(self.load_object)

        ###################### Save Object Option ##################################
        self.action_save_object = QtWidgets.QAction(BuilderWindow)
        self.action_save_object.setObjectName("action_save_object")
        self.action_save_object.setText("Save Object")
        self.menu_project.addAction(self.action_save_object)
        self.menu_project.setStyleSheet("color: black")
        self.action_save_object.triggered.connect(self.save_object)

        ###################### Create Salient Artifact Option ##################################
        self.action_save_object = QtWidgets.QAction(BuilderWindow)
        self.action_save_object.setObjectName("action_create_salient_artifact")
        self.action_save_object.setText("Create Salient Artifact")
        self.menu_project.addAction(self.action_save_object)
        self.menu_project.setStyleSheet("color: black")
        self.action_save_object.triggered.connect(self.create_salient_artifact)

        ###################### Quit Builder Menu Option #############################
        self.action_quit = QtWidgets.QAction(BuilderWindow)
        self.action_quit.setObjectName("action_quit")
        self.menu_project.addAction(self.action_quit)
        self.action_quit.triggered.connect(QtWidgets.qApp.quit)  # exits on click -seb


        self.menubar.addAction(self.menu_project.menuAction())
        self.retranslate_ui(BuilderWindow)
        QtCore.QMetaObject.connectSlotsByName(BuilderWindow)


        ############ Call the method to display relations #####################
        self.display_relations()
        self.display_dependencies()
        disable_button(self.edit_button)
        disable_button(self.undo_button)
        disable_button(self.ignore_button)


        ############# Add Lists actions ####################
        self.details_list.itemClicked.connect(self.enable_ignore_button)
        self.details_list.itemClicked.connect(self.enable_edit_button)
        self.relationship_list.itemClicked.connect(self.display_content)
        self.dependency_list.itemClicked.connect(self.display_dependency_detail)


    def generate_script(self):
        sc = ScriptGenerator(self.controller_object)
        sc.generate_scripts()
        self.saved_project_alert()


    ############ Open Edit Window ####################
    def edit_observation(self):
        self.edit_form = EditForm(self.details_list.currentItem(), self.relation_selected, self)

    def retranslate_ui(self, BuilderWindow):
        _translate = QtCore.QCoreApplication.translate
        BuilderWindow.setWindowTitle(_translate("BuilderWindow", "ABS_Builder"))
        self.dependencies_label.setText(_translate("BuilderWindow", "Dependencies"))
        self.relationships_label.setText(_translate("BuilderWindow", "Relationships"))
        self.search_label.setText(_translate("BuilderWindow", "Search"))
        self.edit_button.setText(_translate("BuilderWindow", "Edit"))
        # self.FilterButton.setText(_translate("BuilderWindow", "Filter"))
        self.delete_button.setText(_translate("BuilderWindow", "Delete"))
        self.ignore_button.setText(_translate("BuilderWindow", "Ignore"))
        self.SA_button.setText(_translate("BuilderWindow", "Create Salient Artifact"))
        self.script_button.setText(_translate("BuilderWindow", "Generate Script"))
        self.move_button.setText(_translate("BuilderWindow", ">>"))
        self.move_button_back.setText(_translate("BuilderWindow", "<<"))
        self.undo_button.setText(_translate("BuilderWindow", "⏎"))
        self.menu_project.setTitle(_translate("BuilderWindow", "Project"))
        self.action_import_project.setText(_translate("BuilderWindow", "Import Project"))
        self.action_quit.setText(_translate("BuilderWindow", "Quit"))
        self.playButton.setIcon(self.playButton.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))


    def display_relations(self):
        self.relationship_list.clear()
        # For each relation add them to the relations display list
        for relation in self.controller_object.relationships_main:
            self.relationship_list.addItem(relation.name)

    def display_dependencies(self):
        self.dependency_list.clear()
        # For each relation add them to the relations display list
        for dependency in self.controller_object.dependencies_main:
            self.dependency_list.addItem(dependency.name)
        # self.relationship_list.itemClicked.connect(self.display_content)


    def update_lists(self):
        self.display_relations()
        self.display_dependencies()


    def load_object(self):
        """
        Import project
        """
        print("load object")
        self.details_list.clear()
        self.relations_list.clear()
        self.relation_selected = None
        self.controller_object.load_object()
        # Display the object in their windows.
        self.update_lists()


    def save_object(self):
        """
        Deep copy of project
        """
        print("save object")
        self.controller_object.save_object()


    def display_search_results(self, text):
        self.relationship_list.clear()

        # For each relation add them to the relations display list
        for relation in self.controller_object.search(text):
            self.relationship_list.addItem(relation.name)



    ##################################### Display the content in the Detail Box ########################################
    def display_content(self, item):
        """
        first it clears the Detail List
        it stores and formats the Relation chosen (clicked) and changes the name to Dependency #
        Finally, for each observation, it will be added in the Detail list
        """
        self.selected_item = "Relationship"
        self.details_list.clear()
        # Look for the selected relation in our list of relationships
        found_relation = None
        for relation_loop in self.controller_object.relationships_main:
            if item.text() == relation_loop.name:
                found_relation = relation_loop

        self.relation_selected = found_relation
        count = 0

        if found_relation != None:
            for observation in found_relation.observation_list:
                self.details_list.addItem(observation.show())
            
                #sets font to gray
                if self.relation_selected.observation_list[count].ignore == 1:
                    self.details_list.item(count).setForeground(QtCore.Qt.gray) 
                count += 1
    

        disable_button(self.edit_button)
        disable_button(self.ignore_button)

    def display_observation_after_edit(self):
        self.details_list.clear()

        for observation in self.relation_selected.observation_list:
            self.details_list.addItem(observation.show())
        disable_button(self.edit_button)


    def display_dependency_detail(self, item):
        self.selected_item = "Dependency"
        self.details_list.clear()

        found_dependency = None
        for dependency_loop in self.controller_object.dependencies_main:
            if item.text() == dependency_loop.name:
                found_dependency = dependency_loop


        self.relation_selected = found_dependency
        count = 0
        if found_dependency != None:
            for observation in found_dependency.observation_list:
                self.details_list.addItem(observation.show())

                #sets font to gray
                if self.relation_selected.observation_list[count].ignore == 1:
                    self.details_list.item(count).setForeground(QtCore.Qt.gray) 
                count += 1

    def pass_dependency(self):
        """
        If the dependency is not in the list, then added to out dependcy list, and display it.
        """
        if self.relation_selected is None:
            return

        self.save_controller_state()
        # Add the Dependency on the dependencies_main, which is basically the relation chosen
        if not self.controller_object.move_to_dependency(self.relation_selected):
            return
        # redisplay both lists
        self.update_lists()

        # --------------------------------------------------------------
        # Display the details of the Dependency selected

    def pass_relationship(self):
        """
        If the relatioonship is not in the list, then added to out relationship list, and display it.
        """
        if self.relation_selected is None:
            return

        self.save_controller_state()
        # Add the Dependency on the dependencies_main, which is basically the relation chosen
        if not self.controller_object.move_to_relationship(self.relation_selected):
            return
        # redisplay both lists
        self.update_lists()

        # --------------------------------------------------------------
        # Display the details of the Dependency selected

    ###################### Delete Button Functions ##################################
    def delete_observation(self):
        self.save_controller_state()
        selected_relationship = self.relationship_list.selectedItems()  # Stores relationship that was selected
        selectItems = self.details_list.selectedItems()  # Stores item that was selected

        # ======================Copied display_content code here===================================================
        selected_observation_text = selectItems[0].text()  # Called before clear to avoid segmentation fault
        self.details_list.clear()

        # Look for relation that matches clicked relationship
        found_relation = None
        for relation_loop in self.controller_object.relationships_main:
            if selected_relationship[0].text() == relation_loop.name:
                found_relation = relation_loop

        # self.relation_selected = found_relation #Maybe don't need this, left in here just in case

        # Go through observations from selected relationship, if observation matches selected observation, remove entirely
        for observation in found_relation.observation_list:
            if observation.show() != selected_observation_text:
                self.details_list.addItem(observation.show())
            else:
                found_relation.observation_list.remove(
                    observation)  # Kick that guy out of the club until project is reimported.
                print("removing observation:", observation.show())  # DEBUG
    
    def disable_edit_button(self):
        self.edit_button.setEnabled(False)
        self.edit_button.setStyleSheet("background-color: rgba(18, 51, 62, 50%); color: #FFFFFF; border-radius: 5px;")

    def enable_edit_button(self):
        self.edit_button.setEnabled(True)
        self.edit_button.setStyleSheet("background-color: rgba(18, 51, 62, 100%); color: #FFFFFF; border-radius: 5px;")

    def disable_delete_button(self):
        self.delete_button.setEnabled(False)
        self.delete_button.setStyleSheet("background-color: rgba(18, 51, 62, 50%); color: #FFFFFF; border-radius: 5px;")

    def enable_delete_button(self):
        self.delete_button.setEnabled(True)
        self.delete_button.setStyleSheet(
            "background-color: rgba(18, 51, 62, 100%); color: #FFFFFF; border-radius: 5px;")

    ###################### Script Button Functions #########################
    def disable_script_button(self):
        self.script_button.setEnabled(False)
        self.script_button.setStyleSheet("background-color: rgba(18, 51, 62, 50%); color: #FFFFFF; border-radius: 5px;")

    def enable_script_button(self):
        self.script_button.setEnabled(True)
        self.script_button.setStyleSheet("background-color: rgba(18, 51, 62, 100%); color: #FFFFFF; border-radius: 5px;")

    ###################### Ignore Button Functions #########################
    def disable_ignore_button(self):
        self.ignore_button.setEnabled(False)
        self.ignore_button.setStyleSheet("background-color: rgba(18, 51, 62, 50%); color: #FFFFFF; border-radius: 5px;")

    def enable_ignore_button(self):
        self.ignore_button.setEnabled(True)
        self.ignore_button.setStyleSheet("background-color: rgba(18, 51, 62, 100%); color: #FFFFFF; border-radius: 5px;")

    def show_analyzingWindow(self):
        self.Analyzing_Window = QtWidgets.QDialog()
        self.ui = Ui_Analyzing_Window()
        self.ui.setupUi(self.Analyzing_Window)
        self.Analyzing_Window.show()
        QtWidgets.qApp.processEvents()
        self.ui.progressBar_update()

    ###################### Import Project Function ###############################
    def import_project(self):
        currentDirectory = os.getcwd()
        name = QtWidgets.QFileDialog.getExistingDirectory(self.menu_project, 'Choose Src Dir', 'currentDirectory')
        print("directory selected:", name)
        print("dirname:", os.path.dirname(name))  #The path leading up to the chosen folder
        print("basename:",os.path.basename(name)) #The actual chosen folder name

        try:
            subdir_folders = os.listdir(name)
            # print(subdir_folders[0]) #DEBUG: list elements are str
            if "Builder" not in subdir_folders:
                #print("This directory is not properly formatted, please select a project data directory")
                self.alert_msg("Invalid Directory","This directory is not properly formatted, please select a project data directory")
                
            else:
                #print("folder with relationships:", name) #DEBUG
                print("updating controller with new project:", name)
                self.controller_object.update(os.path.basename(name))
                self.display_relations()

        except Exception as e: 
            print("The following error has occured:",e)



    ###################### Ignore Project Function -Seb #############################
    def ignore_observation(self):
        self.save_controller_state()
        observationIndex = int(self.details_list.currentItem().text()[0])
        observation = self.relation_selected.observation_list[observationIndex]

        #If ignore has already been set, allow an user to revert the choice by clicking "ignore" again
        if observation.ignore == 1:
            observation.ignore = 0
            self.details_list.currentItem().setForeground(QtCore.Qt.black) 
        else:
            observation.ignore = 1
            self.details_list.currentItem().setForeground(QtCore.Qt.gray) 

    def create_salient_artifact(self):
        print("creating salient artifact chump")
        pass

    ###################### Manage control state  #############################
    def save_controller_state(self):
        if len(self.undo_stack) > 20:
            self.undo_stack.pop(0)
        enable_button(self.undo_button)
        self.undo_stack.append(copy.deepcopy(self.controller_object))

    def undo_controller_state(self):
        self.controller_object = self.undo_stack.pop()
        if len(self.undo_stack) < 1:
            disable_button(self.undo_button)

        # Update Detail List if changed detected
        if len(self.relationship_list.selectedItems()) > 0 and self.selected_item == "Relationship":
            self.display_content(self.relationship_list.selectedItems()[0])
        elif len(self.dependency_list.selectedItems()) > 0 and self.selected_item == "Dependency":
            self.display_dependency_detail(self.dependency_list.selectedItems()[0])

        self.update_lists()

    def execute(self):
        app = QtWidgets.QApplication(sys.argv)
        BuilderWindow = QtWidgets.QMainWindow()
        self.setupUi(BuilderWindow)
        BuilderWindow.show()
        sys.exit(app.exec_())

    ###################### Alert Pop-up Window  #############################
    def alert_msg(self, title, msg):
        print("Error occured. Title:%s Message:%s " %(str(title), str(msg)))
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle(str(title))
        msgbox.setText(str(msg))
        msgbox.exec_()

    def saved_project_alert(self):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Project Saved!")
        msgbox.setText("The state of the project has been saved.")
        msgbox.exec_()


    def open_runner(self):
        #Save all changes before opening runner
        self.controller_object.save_object()
        print('Finished saving changes')
        
        if platform.system() == "Windows":
            Popen(['python', 'GUI_manager.py', 'runner', self.controller_object.project_name],stdout=PIPE, stderr=PIPE)
        else:
            Popen(['python3', 'GUI_manager.py', 'runner', self.controller_object.project_name],stdout=PIPE, stderr=PIPE)



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     BuilderWindow = QtWidgets.QMainWindow()
#     ui = Ui_BuilderWindow()
#     ui.setupUi(BuilderWindow)
#     BuilderWindow.show()
#     sys.exit(app.exec_())
