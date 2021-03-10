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
import ceBackend
import time
import os  # os and json are used for dir json aggregation for now
import json
import re


class Ui_CEWindow(QMainWindow):
    def setupUi(self, CEWindow):
        CEWindow.setObjectName("CEWindow")
        CEWindow.resize(689, 230)
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
        self.fileName.setObjectName("fileName")

        self.Analyze_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Analyze_Button.setGeometry(QtCore.QRect(390, 110, 121, 31))
        self.Analyze_Button.setFont(font)
        self.Analyze_Button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.Analyze_Button.setObjectName("Analyze_Button")

        self.SaveProject_Button = QtWidgets.QPushButton(self.centralwidget)
        self.SaveProject_Button.setGeometry(QtCore.QRect(150, 110, 161, 31))
        self.SaveProject_Button.setFont(font)
        self.SaveProject_Button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.SaveProject_Button.setObjectName("SaveProject_Button")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 301, 31))
        self.label.setFont(font)
        self.label.setObjectName("label")
        CEWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CEWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 21))
        self.menubar.setObjectName("menubar")
        self.menuNew_Project = QtWidgets.QMenu(self.menubar)
        self.menuNew_Project.setObjectName("menuNew_Project")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
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

        self.retranslateUi(CEWindow)
        QtCore.QMetaObject.connectSlotsByName(CEWindow)

        self.retranslateUi(CEWindow)
        QtCore.QMetaObject.connectSlotsByName(CEWindow)
        #################Button Actions###########################
        self.Browse_Button.clicked.connect(self.browseFiles)
        self.Analyze_Button.clicked.connect(self.show_analyzingWindow)

    ######################  BROWSE BUTTON FUNCTION ###############
    def browseFiles(self):
        # Gets directory name and sets it to a variable
        name = QFileDialog.getExistingDirectory(self.Browse_Button, 'Choose Src Dir', 'c:\\')
        print("dirname:", name)
        directory = os.fsencode(name)
        self.fileName.setText(name)

        # Get filenames from the given directory (preferably "parsedLogs" within the eceld system)
        file_list = []
        head = []

        for file in os.listdir(directory):
            file_list.append(file.decode())

        ##Set num_lines count to the MouseClicks.json file number of lines for now
        self.num_lines = self.count_lines(name + "/" + str(file_list[1]))

        # Stores all json file contents within the "causationSource" json file
        # output file name
        with open("masterJson.json", "w") as outfile:
            for f in file_list:
                with open(name + "/" + f, 'rb') as infile:
                    if f == "pcapOutput.json":  # start adding 3/8/21
                        # print("converting pcap file")
                        data = json.load(infile)
                        packetList = []
                        for i in range(len(data)):
                            level = data[i]["_source"]["layers"]
                            frame_number = str(level["frame"]["frame.number"])
                            frame_time = str(level["frame"]["frame.time"])
                            packetList.append({"start": frame_time})
                            packetList[i]["data"] = data[i]
                            packetList[i]["content"] = "network"
                        head += packetList
                    else:
                        file_data = json.load(infile)
                        head += file_data
            json.dump(head, outfile)
        print("done enumerating files")

        #self.num_lines = self.count_lines("masterJson.json")
        with open("masterJson.json") as jsonFile:
            self.text = jsonFile.read()


    def count_lines(self, filename):
        num_lines = sum(1 for line in open(filename))
        return num_lines

    ####################    ANALYSIS WINDOW POPUP  ####################################

    def show_analyzingWindow(self):
        self.hide()
        self.Analyzing_Window = QtWidgets.QDialog()
        self.ui = Ui_Analyzing_Window()
        self.ui.setupUi(self.Analyzing_Window)
        self.Analyzing_Window.show()
        QtWidgets.qApp.processEvents()
        self.ui.progressBar_update(self.num_lines)

    ##############################################################################

    def retranslateUi(self, CEWindow):
        _translate = QtCore.QCoreApplication.translate
        CEWindow.setWindowTitle(_translate("CEWindow", "MainWindow"))
        self.Browse_Button.setText(_translate("CEWindow", "Browse"))
        self.Analyze_Button.setText(_translate("CEWindow", "Analyze"))
        self.SaveProject_Button.setText(_translate("CEWindow", "Save Project"))
        self.label.setText(_translate("CEWindow", "ECELd Project Folder:"))
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