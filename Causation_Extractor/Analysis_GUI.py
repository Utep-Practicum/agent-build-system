# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Analyzing_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from ceBackend import ceBackend
from PyQt5.QtWidgets import QWidget
import time

class Ui_Analyzing_Window(QWidget):

    def setupUi(self, Analyzing_Window):
        Analyzing_Window.setObjectName("Analyzing_Window")
        Analyzing_Window.resize(690, 365)
        Analyzing_Window.setStyleSheet("background-color: white;")
        self.progressBar = QtWidgets.QProgressBar(Analyzing_Window)
        self.progressBar.setGeometry(QtCore.QRect(140, 60, 441, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    border: 2px solid grey;\n"
                                       "    border-radius: 5px;\n"
                                       "    text-align: center;\n"
                                       "    color: rgb(140, 140, 140);\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "    background-color: rgb(19,51,63) ;\n"
                                       "    width: 10px;\n"
                                       "    margin: 0.5px;\n"
                                       "}")
        self.progressBar.setMaximum(100)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Analyzing_Window)
        self.label.setGeometry(QtCore.QRect(270, 140, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setObjectName("label")
        self.Time_Elapsed = QtWidgets.QLabel(Analyzing_Window)
        self.Time_Elapsed.setGeometry(QtCore.QRect(150, 190, 101, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.Time_Elapsed.setFont(font)
        self.Time_Elapsed.setStyleSheet("color:black;")
        self.Time_Elapsed.setObjectName("Time_Elapsed")
        self.Time_Elapsed_A = QtWidgets.QLabel(Analyzing_Window)
        self.Time_Elapsed_A.setGeometry(QtCore.QRect(300, 190, 71, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.Time_Elapsed_A.setFont(font)
        self.Time_Elapsed_A.setStyleSheet("color:black;")
        self.Time_Elapsed_A.setObjectName("Time_Elapsed_A")
        self.Relationships = QtWidgets.QLabel(Analyzing_Window)
        self.Relationships.setGeometry(QtCore.QRect(150, 220, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.Relationships.setFont(font)
        self.Relationships.setStyleSheet("color:black;")
        self.Relationships.setObjectName("Relationships")
        self.Relationships_A = QtWidgets.QLabel(Analyzing_Window)
        self.Relationships_A.setGeometry(QtCore.QRect(300, 220, 71, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.Relationships_A.setFont(font)
        self.Relationships_A.setStyleSheet("color:black;")
        self.Relationships_A.setObjectName("Relationships_A")
        self.SArtifacts = QtWidgets.QLabel(Analyzing_Window)
        self.SArtifacts.setGeometry(QtCore.QRect(150, 250, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.SArtifacts.setFont(font)
        self.SArtifacts.setStyleSheet("color:black;")
        self.SArtifacts.setObjectName("SArtifacts")
        self.SArtifacts_A = QtWidgets.QLabel(Analyzing_Window)
        self.SArtifacts_A.setGeometry(QtCore.QRect(300, 250, 71, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.SArtifacts_A.setFont(font)
        self.SArtifacts_A.setStyleSheet("color:black;")
        self.SArtifacts_A.setObjectName("SArtifacts_A")
        self.Export = QtWidgets.QPushButton(Analyzing_Window)
        self.Export.setGeometry(QtCore.QRect(410, 200, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.Export.setFont(font)
        self.Export.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.Export.setObjectName("Export")
        self.retranslateUi(Analyzing_Window)
        QtCore.QMetaObject.connectSlotsByName(Analyzing_Window)


    def retranslateUi(self, Analyzing_Window):
        _translate = QtCore.QCoreApplication.translate
        Analyzing_Window.setWindowTitle(_translate("Analyzing_Window", "Dialog"))
        self.label.setText(_translate("Analyzing_Window", "Analyzing..."))
        self.Time_Elapsed.setText(_translate("Analyzing_Window", "Time Elapsed"))
        self.Time_Elapsed_A.setText(_translate("Analyzing_Window", "0:0:0"))
        self.Relationships.setText(_translate("Analyzing_Window", "Relationships "))
        self.Relationships_A.setText(_translate("Analyzing_Window", "0"))
        self.SArtifacts.setText(_translate("Analyzing_Window", "Salient Artifacts"))
        self.SArtifacts_A.setText(_translate("Analyzing_Window", "0"))
        self.Export.setText(_translate("Analyzing_Window", "Export to builder"))



    def progressBar_update(self,count,project_Name):
        causationObject = ceBackend()
        QtWidgets.qApp.processEvents()
        frac = round(100/count,1)
        prct = 0
        start_time = time.time()
        while 100 > prct:
            prct += frac
            time.sleep(.01)
            self.progressBar.setValue(prct)

        relationshipList = causationObject.relationshipDefiner()
        artifactCount = causationObject.makeArtifacts(relationshipList)
        print("Inside Progress Bar Method... "+project_Name)
        causationObject.createRelationshipFile(relationshipList,project_Name)
        final_time = time.time() - start_time

        self.progressBar.setValue(100)
        self.label.setText("Finished")
        self.Time_Elapsed_A.setText(str(final_time)[:5])
        self.SArtifacts_A.setText(str(artifactCount))
        self.Relationships_A.setText(str(len(relationshipList)))
