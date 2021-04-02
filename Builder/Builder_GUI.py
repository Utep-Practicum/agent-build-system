# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Builder_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Edit import *
from NewSalientArtifact import *
from Controller import *

from BuilderBackEnd import *
import json
import sys

class Ui_BuilderWindow(object):

    def __init__(self, controller):
        self.controller_object = controller
        # self.back_end = BuilderBackEnd()
        self.dependency = ""
        self.relations_list = controller.relationships_main
        self.dependency_list = []
        if __name__ != "__main__":
            self.execute()

    def setupUi(self, BuilderWindow):
        BuilderWindow.setObjectName("BuilderWindow")
        BuilderWindow.resize(778, 720)
        BuilderWindow.setStyleSheet("background-color: #f4f5f7;")
        self.centralwidget = QtWidgets.QWidget(BuilderWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(778, 579))
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()

        #########################Search Label#########################
        self.search_label = QtWidgets.QLabel(self.centralwidget)
        self.search_label.setGeometry(QtCore.QRect(20, 14, 281, 23))
        font.setPointSize(14)
        self.search_label.setFont(font)
        self.search_label.setStyleSheet("color:black;")
        self.search_label.setObjectName("search_label")

        #########################Search Input#########################
        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(20, 40, 721, 40))
        self.search_input.setObjectName("search_input")
        self.search_input.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.search_input.textChanged.connect(self.displaySearchResults)

        #########################Detail List#########################
        self.details_list = QtWidgets.QListWidget(self.centralwidget)
        self.details_list.setGeometry(QtCore.QRect(20, 431, 721, 221))
        self.details_list.setObjectName("details_list")
        self.details_list.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.details_list.setDragEnabled(True)

        #####################Relationships Label##################################
        self.relationships_label = QtWidgets.QLabel(self.centralwidget)
        self.relationships_label.setGeometry(QtCore.QRect(20, 92, 291, 23))
        font.setPointSize(14)
        self.relationships_label.setFont(font)
        self.relationships_label.setStyleSheet("color:black;")
        self.relationships_label.setObjectName("label")

        #####################Relationship List Widget ##########################
        self.Relationship_list = QtWidgets.QListWidget(self.centralwidget)
        self.Relationship_list.setGeometry(QtCore.QRect(20, 120, 291, 293))
        self.Relationship_list.setObjectName("Relationship_list")
        self.Relationship_list.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")

        #########################Dependencies Label#########################
        self.dependencies_label = QtWidgets.QLabel(self.centralwidget)
        self.dependencies_label.setGeometry(QtCore.QRect(460, 92, 281, 23))
        font.setPointSize(14)
        self.dependencies_label.setFont(font)
        self.dependencies_label.setStyleSheet("color:black;")
        self.dependencies_label.setObjectName("dependencies_label")

        #####################Dependencies List Widget######################
        self.Dependency_list = QtWidgets.QListWidget(self.centralwidget)
        self.Dependency_list.setGeometry(QtCore.QRect(460, 120, 281, 293))
        self.Dependency_list.setObjectName("Dependency_list")
        self.Dependency_list.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.Dependency_list.setDragEnabled(True)

        #####################Relationship -> Dependency Button #####################
        self.move_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_button.setGeometry(QtCore.QRect(340, 180, 100, 75))
        self.move_button.setMinimumSize(QtCore.QSize(100, 75))
        font.setPointSize(16)
        self.move_button.setFont(font)
        self.move_button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.move_button.setObjectName("move_button")
        self.move_button.clicked.connect(self.passDependency)
        BuilderWindow.setCentralWidget(self.centralwidget)

        #####################Edit Artifact Button #################################
        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(340, 261, 100, 75))
        self.edit_button.setMinimumSize(QtCore.QSize(100, 75))
        font.setPointSize(16)
        self.edit_button.setFont(font)
        self.edit_button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.edit_button.setObjectName("edit_button")
        self.edit_button.clicked.connect(self.open_edit)



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

        ###################### Save Project Menu Option #############################
        self.action_save_project = QtWidgets.QAction(BuilderWindow)
        self.action_save_project.setObjectName("action_save_project")
        self.menu_project.addAction(self.action_save_project)

        ###################### Quit Builder Menu Option #############################
        self.action_quit = QtWidgets.QAction(BuilderWindow)
        self.action_quit.setObjectName("action_quit")
        self.menu_project.addAction(self.action_quit)

        self.menubar.addAction(self.menu_project.menuAction())
        self.retranslateUi(BuilderWindow)
        QtCore.QMetaObject.connectSlotsByName(BuilderWindow)

        ############ Call the method to display relations #####################
        self.displayRelations()
        self.disable_edit_button()

    ############ Open Edit Window ####################
    def open_edit(self):
        self.wind = EditForm()
        self.wind.initializeUI()
        # print(self.relations_dictionary[self.Relationship_list.currentItem().text()][self.Relationship_list.currentRow()])
        # print(self.Relationship_list.currentItem().text())
        # print(self.details_list.currentRow())
        self.wind.set_relation(self.details_list.currentItem())

    def openFilter(self):
        self.wind = NewSalientArtifact()
        self.wind.initializeUI()

    def retranslateUi(self, BuilderWindow):
        _translate = QtCore.QCoreApplication.translate
        BuilderWindow.setWindowTitle(_translate("BuilderWindow", "ABS_Builder"))
        self.dependencies_label.setText(_translate("BuilderWindow", "Dependencies"))
        self.relationships_label.setText(_translate("BuilderWindow", "Relationships"))
        self.search_label.setText(_translate("BuilderWindow", "Search"))
        self.edit_button.setText(_translate("BuilderWindow", "Edit"))
        # self.FilterButton.setText(_translate("BuilderWindow", "Filter"))
        self.move_button.setText(_translate("BuilderWindow", ">>"))
        self.menu_project.setTitle(_translate("BuilderWindow", "Project"))
        self.action_save_project.setText(_translate("BuilderWindow", "Save Project"))
        self.action_quit.setText(_translate("BuilderWindow", "Quit"))

    def displayRelations(self):
        self.Relationship_list.clear()

        #self.relations_dictionary = self.back_end.read_relationships()

        #self.search_dictionary = self.relations_dictionary

        # For each relation add them to the relations display list
        for relation in self.relations_list:
            self.Relationship_list.addItem(relation.name)

        self.Relationship_list.itemClicked.connect(self.displayContent)

    def displaySearchResults(self, text):
        self.search_dictionary = {}
        for relationship in self.relations_dictionary:
            relationship_added = False
            for relation in self.relations_dictionary.get(relationship):
                if text in str(relation):
                    if relationship_added == False:
                        self.search_dictionary[relationship] = [relation]
                        relationship_added = True
                    self.search_dictionary[relationship].append(relation)

        self.Relationship_list.clear()
        for relation_name in self.search_dictionary.keys():
            self.Relationship_list.addItem(relation_name)

    ##################################### Display the content in the Detail Box ########################################
    def displayContent(self, item):
        """
        first it clears the Detail List
        it stores and formats the Relation chosen (clicked) and changes the name to Dependency #
        Finally, for each observation, it will be added in the Detail list
        """

        self.details_list.clear()

        self.dependency = "Dependency " + item.text().split(" ")[1]
        print(item)
        print(item.text())
        # Change this
        # self.relations_list.observation_list
        # Look for the selected relation in our list of relationships
        found_relation = None
        for relation in self.relations_list:
            if item.text() == relation.name:
                found_relation = relation

        for observation in found_relation.observation_list:
            self.details_list.addItem(observation.show())

        self.disable_edit_button()
        self.details_list.itemClicked.connect(self.enable_edit_button)

    def passDependency(self):
        """
        If the dependency is not in the list, then added to out dependcy list, and display it.
        """
        if self.dependency not in self.dependency_list:
            self.dependency_list.append(self.dependency)
            self.Dependency_list.addItem(self.dependency)

    def disable_edit_button(self):
        self.edit_button.setEnabled(False)
        self.edit_button.setStyleSheet("background-color: rgba(18, 51, 62, 50%); color: #FFFFFF; border-radius: 5px;")

    def enable_edit_button(self):
        self.edit_button.setEnabled(True)
        self.edit_button.setStyleSheet("background-color: rgba(18, 51, 62, 100%); color: #FFFFFF; border-radius: 5px;")


    def execute(self):
        app = QtWidgets.QApplication(sys.argv)
        BuilderWindow = QtWidgets.QMainWindow()
        # ui = Ui_BuilderWindow()
        self.setupUi(BuilderWindow)
        BuilderWindow.show()
        sys.exit(app.exec_())

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     BuilderWindow = QtWidgets.QMainWindow()
#     ui = Ui_BuilderWindow()
#     ui.setupUi(BuilderWindow)
#     BuilderWindow.show()
#     sys.exit(app.exec_())
