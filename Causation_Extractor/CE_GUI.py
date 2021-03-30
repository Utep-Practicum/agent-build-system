# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CE_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from Analysis_GUI import Ui_Analyzing_Window
from ceBackend import *
from saveProject import *
import os #os and json are used for dir json aggregation for now

class Ui_CEWindow(QMainWindow):
    def setupUi(self, CEWindow):
        CEWindow.setObjectName("CEWindow")
        CEWindow.resize(689, 250)
        CEWindow.setMinimumSize(QtCore.QSize(650, 250))
        CEWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(CEWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Browse_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_Button.setGeometry(QtCore.QRect(110, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.Browse_Button.setFont(font)
        self.Browse_Button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.Browse_Button.setObjectName("Browse_Button")
        self.fileName = QtWidgets.QLineEdit(self.centralwidget)

        self.fileName.setGeometry(QtCore.QRect(230, 60, 351, 31))
        self.fileName.setFont(font)
        self.fileName.setReadOnly(True)
        self.fileName.setStyleSheet("color: black")
        self.fileName.setObjectName("fileName")

        self.Analyze_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Analyze_Button.setGeometry(QtCore.QRect(370, 150, 121, 31))
        self.Analyze_Button.setFont(font)
        self.Analyze_Button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.Analyze_Button.setObjectName("Analyze_Button")

        self.SaveProject_Button = QtWidgets.QPushButton(self.centralwidget)
        self.SaveProject_Button.setGeometry(QtCore.QRect(170, 150, 161, 31))
        self.SaveProject_Button.setFont(font)
        self.SaveProject_Button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.SaveProject_Button.setObjectName("SaveProject_Button")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 301, 31))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: black")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(120, 100, 101, 31))
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: black;")
        self.time_label.setObjectName("time_label")
        CEWindow.setCentralWidget(self.centralwidget)

        self.time_input = QtWidgets.QLineEdit(self.centralwidget)
        self.time_input.setGeometry(QtCore.QRect(230, 100, 351, 31))
        self.time_input.setStyleSheet("color: black;")
        self.time_input.setObjectName("time_input")
        CEWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CEWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("color: black")
        self.menuNew_Project = QtWidgets.QMenu(self.menubar)
        self.menuNew_Project.setObjectName("menuNew_Project")
        self.menuNew_Project.setStyleSheet("color: black")
        
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuNew_Project.setStyleSheet("color: black")

        CEWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CEWindow)
        self.statusbar.setObjectName("statusbar")
        CEWindow.setStatusBar(self.statusbar)
        self.actionSave_Project = QtWidgets.QAction(CEWindow)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionExit = QtWidgets.QAction(CEWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionREADME = QtWidgets.QAction(CEWindow)
        self.actionREADME.setObjectName("actionREADME")
        self.menuNew_Project.addAction(self.actionSave_Project)
        self.menuNew_Project.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionREADME)
        self.menubar.addAction(self.menuNew_Project.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        ################## TIME FRAME ##############################
        self.time_frame = 5

        self.retranslateUi(CEWindow)
        QtCore.QMetaObject.connectSlotsByName(CEWindow)

        self.retranslateUi(CEWindow)
        QtCore.QMetaObject.connectSlotsByName(CEWindow)

         ################# PROJECT NAME #############################
        self.project_name = ""
        self.check_project()
        
        ################# BUTTON ACTIONS ###########################
        self.Browse_Button.clicked.connect(self.browse_Files)
        self.Analyze_Button.clicked.connect(self.show_analyzingWindow)
        self.SaveProject_Button.clicked.connect(self.save_Project)

       
    ######################  BROWSE BUTTON FUNCTION ###############
    def browse_Files(self):
        # Gets directory name and sets it to a variable
        name = QFileDialog.getExistingDirectory(self.Browse_Button, 'Choose Src Dir', 'c:\\')
        print("dirname:", name)
        directory = os.fsencode(name)
        self.fileName.setText(name)
        backend = ceBackend()
        self.num_lines = backend.output_directory(directory,name)
        self.get_ProjectName()
        self.check_project()

    def show_analyzingWindow(self):
        self.hide()
        self.Analyzing_Window = QtWidgets.QDialog()
        self.ui = Ui_Analyzing_Window()
        self.ui.setupUi(self.Analyzing_Window)
        self.Analyzing_Window.show()
        QtWidgets.qApp.processEvents()   
        self.time_frame = float(self.time_input.text())  
        self.ui.progressBar_update(self.num_lines,self.project_name,self.time_frame)


    ###################### SAVE PROJECT BUTTON #######################################
    def save_Project(self):
        self.Form = QtWidgets.QDialog()
        self.sP = NewProject(self.Form)
        self.Form.show()

    ##############################################################################
    def get_ProjectName(self):
        self.project_name = self.sP.project_sP
        print(self.project_name)
    ###################### CHECK THAT A PROJECT HAS BEEN CREATED #############################
    def check_project(self):
        if self.project_name == "":
            self.Analyze_Button.setEnabled(False)
            print("Project not created. Please create one")
        else:
            print("Working with project...." +self.project_name)
            self.label.setText("ECELd Project Folder:")
            self.Analyze_Button.setEnabled(True)
            self.SaveProject_Button.setEnabled(False)    
        

    def retranslateUi(self, CEWindow):
        _translate = QtCore.QCoreApplication.translate
        CEWindow.setWindowTitle(_translate("CEWindow", "MainWindow"))
        self.Browse_Button.setText(_translate("CEWindow", "Browse"))
        self.Analyze_Button.setText(_translate("CEWindow", "Analyze"))
        self.SaveProject_Button.setText(_translate("CEWindow", "Save Project"))
        self.label.setText(_translate("CEWindow", "ECELd Project Folder:"))
        self.time_label.setText(_translate("CEWindow", "Time Frame:"))
        self.menuNew_Project.setTitle(_translate("CEWindow", "Project"))
        self.menuHelp.setTitle(_translate("CEWindow", "Help"))
        self.actionSave_Project.setText(_translate("CEWindow", "Save Project"))
        self.actionExit.setText(_translate("CEWindow", "Exit"))
        self.actionREADME.setText(_translate("CEWindow", "README"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    CEWindow = QtWidgets.QMainWindow()
    ui = Ui_CEWindow()
    ui.setupUi(CEWindow)
    CEWindow.show()
    sys.exit(app.exec())
