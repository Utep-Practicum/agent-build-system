# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saveProject.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5.QtWidgets import *

class NewProject(QtWidgets.QDialog):

    def __init__(self,Form):
        super(NewProject, self).__init__()
        Form.setObjectName("Form")
        Form.resize(459, 204)
        Form.setMinimumSize(QtCore.QSize(450, 200))
        Form.setStyleSheet("background-color: white")

        self.Projectlabel = QtWidgets.QLabel(Form)
        self.Projectlabel.setGeometry(QtCore.QRect(40, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.Projectlabel.setFont(font)
        self.Projectlabel.setStyleSheet("color: black;")
        self.Projectlabel.setObjectName("Projectlabel")
        
        self.ProjectName = QtWidgets.QLineEdit(Form)
        self.ProjectName.setGeometry(QtCore.QRect(40, 60, 351, 41))
        self.ProjectName.setStyleSheet("color: black;")
        self.ProjectName.setObjectName("ProjectName")


        self.CreateButton = QtWidgets.QPushButton(Form)
        self.CreateButton.setGeometry(QtCore.QRect(40, 120, 161, 41))
        font.setPointSize(11)
        self.CreateButton.setFont(font)
        self.CreateButton.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px; padding: 8px 0px;")
        self.CreateButton.setObjectName("CreateButton")
        
        self.CancelButton = QtWidgets.QPushButton(Form)
        self.CancelButton.setGeometry(QtCore.QRect(230, 120, 161, 41))
        font.setPointSize(11)
        self.CancelButton.setFont(font)
        self.CancelButton.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px; padding: 8px 0px;")
        self.CancelButton.setObjectName("CancelButton")

        # Error label
        self.error_label = QtWidgets.QLabel(Form)
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setGeometry(QtCore.QRect(40, 165, 190, 18))
        self.error_label.setFont(font)
        self.error_label.setHidden(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #################BUTTON ACTIONS##################################
        self.CreateButton.clicked.connect(self.create_folders)
        self.CancelButton.clicked.connect(Form.close)
        
        self.project_sP = ""

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Save Project"))
        self.Projectlabel.setText(_translate("Form", "Project Name:"))
        self.CreateButton.setText(_translate("Form", "Create Project"))
        self.CancelButton.setText(_translate("Form", "Cancel"))
        self.error_label.setText(_translate("Form", "This project already exists"))
        


    def create_folders(self):
        self.error_label.setHidden(True)
        self.project_sP = self.ProjectName.text()
        
        # Create Projects root path if does not exist
        if not os.path.exists("Project Data"):
            os.makedirs("Project Data")

        #  Create Project Paths
        if not os.path.exists("Project Data/" + self.ProjectName.text()):
            print("Creating folders....")
            os.makedirs("Project Data/" + self.ProjectName.text())
            os.makedirs("Project Data/" + self.ProjectName.text() + "/CE/")
            os.makedirs("Project Data/" + self.ProjectName.text() + "/CE/CE_logs/")
            eceld_path_file = 'eceld_project_path.txt'
            with open (os.path.join("Project Data/" + self.ProjectName.text() + "/CE/CE_logs/",eceld_path_file),'w') as fp:
                pass
            os.makedirs("Project Data/" + self.ProjectName.text() + "/CE/Relationships/")
            os.makedirs("Project Data/" + self.ProjectName.text() + "/Builder/")
            os.makedirs("Project Data/" + self.ProjectName.text() + "/Builder/Builder_logs/")
            os.makedirs("Project Data/" + self.ProjectName.text() + "/Builder/Dependencies/")
            os.makedirs("Project Data/" + self.ProjectName.text() + "/Runner/")
            os.makedirs("Project Data/" + self.ProjectName.text() + "/Builder/Runner/Runner_logs")
            os.makedirs("Project Data/" + self.ProjectName.text() + "/Packager/")
            os.makedirs("Project Data/" + self.ProjectName.text() + "/Packager/Packager_logs")
            self.CancelButton.setText("Continue")
            self.CreateButton.hide()
            print("Project " + self.ProjectName.text()+" was created")
        else:
            self.error_label.setHidden(False)
            print("Project Name Already Exists")

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = NewProject(Form)
    Form.show()
    sys.exit(app.exec_())
'''