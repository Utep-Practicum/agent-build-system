# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Runner_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Runner.Runner_Manager import *
import sys


class Runner_GUI(object):
    def __init__(self, controller):
        self.runner_manager = RunnerManager(controller)
        if __name__ != "__main__":
            self.execute()

    def setupUi(self, Runner):
        Runner.setObjectName("Runner_GUI")
        Runner.resize(800, 569)
        Runner.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(Runner)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMinimumSize(QtCore.QSize(760, 530))
        font = QtGui.QFont()

        ###################### Labels ##########################
        self.ECELd = QtWidgets.QLabel(self.centralwidget)
        self.ECELd.setGeometry(QtCore.QRect(420, 20, 151, 21))
        font.setPointSize(14)
        self.ECELd.setFont(font)
        self.ECELd.setStyleSheet("color:black;")
        self.ECELd.setObjectName("ECELd")

        self.ABS = QtWidgets.QLabel(self.centralwidget)
        self.ABS.setStyleSheet("color:black;")
        self.ABS.setGeometry(QtCore.QRect(20, 20, 151, 21))
        self.ABS.setFont(font)
        self.ABS.setObjectName("ABS")

        #################### ABS Output ########################
        self.ABSOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.ABSOutput.setGeometry(QtCore.QRect(20, 50, 321, 391))
        self.ABSOutput.setObjectName("ABSOutput")
        self.ABSOutput.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.ABSOutput.setEnabled(False)

        #################### ECELd Output #######################
        self.ECELdOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.ECELdOutput.setGeometry(QtCore.QRect(420, 50, 301, 391))
        self.ECELdOutput.setObjectName("ECELdOutput")
        self.ECELdOutput.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.ECELdOutput.setEnabled(False)

        ################### Back2Builder Button #########################
        self.back2BuilderButton = QtWidgets.QPushButton(self.centralwidget)
        self.back2BuilderButton.setGeometry(QtCore.QRect(470, 470, 150, 31))
        self.back2BuilderButton.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.back2BuilderButton.setObjectName("back2Builder")
        self.back2BuilderButton.clicked.connect(self.back_to_builder)

        ################### Play Button #########################
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(20, 470, 81, 31))
        self.playButton.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.playButton.setObjectName("playButton")
        self.playButton.clicked.connect(self.play_runner)

        ################## Pause Button #########################
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(110, 470, 71, 31))
        self.pauseButton.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.pauseButton.setObjectName("pauseButton")

        ################## Stop Button ##########################
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(190, 470, 81, 31))
        self.stopButton.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; border: 1px solid #D2D6E0; color: black;")
        self.stopButton.setObjectName("stopButton")

        ################## Menu Top Bar #########################
        Runner.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Runner)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Runner.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Runner)
        self.statusbar.setObjectName("statusbar")
        Runner.setStatusBar(self.statusbar)
        self.actionSave_Project = QtWidgets.QAction(Runner)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionExit = QtWidgets.QAction(Runner)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(Runner.close)
        self.actionREADME = QtWidgets.QAction(Runner)
        self.actionREADME.setObjectName("actionREADME")
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionREADME)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Runner)
        QtCore.QMetaObject.connectSlotsByName(Runner)

    def retranslateUi(self, Runner_GUI):
        _translate = QtCore.QCoreApplication.translate
        Runner_GUI.setWindowTitle(_translate("Runner_GUI", "ABS_Runner"))
        self.ECELd.setText(_translate("Runner_GUI", "ECELd Output:"))

        self.back2BuilderButton.setText(_translate("Runner_GUI","Back to Builder"))
        self.playButton.setIcon(self.playButton.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.stopButton.setIcon(self.stopButton.style().standardIcon(QtWidgets.QStyle.SP_MediaStop))
        self.ABS.setText(_translate("Runner_GUI", "ABS Output:"))
        self.pauseButton.setIcon(self.pauseButton.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
        self.menuFile.setTitle(_translate("Runner_GUI", "File"))
        self.menuHelp.setTitle(_translate("Runner_GUI", "Help"))
        self.actionSave_Project.setText(_translate("Runner_GUI", "Save Project"))
        self.actionExit.setText(_translate("Runner_GUI", "Exit"))
        self.actionREADME.setText(_translate("Runner_GUI", "README"))


    def back_to_builder(self):
        self.runner_manager.back_to_builder()
        self.close

    
    def play_runner(self):
        self.runner_manager.runner_review()

    def execute(self):
        app = QtWidgets.QApplication(sys.argv)
        RunnerWindow = QtWidgets.QMainWindow()
        self.setupUi(RunnerWindow)
        RunnerWindow.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Runner = QtWidgets.QMainWindow()
    ui = Runner_GUI()
    ui.setupUi(Runner)
    Runner.show()
    sys.exit(app.exec_())
