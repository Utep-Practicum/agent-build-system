# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saveProject.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os , shutil
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import zipfile
import subprocess as sp

class CreateProject(QtWidgets.QDialog):

    def __init__(self,Form):
        super(CreateProject, self).__init__()
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

        self.CompressButton = QtWidgets.QPushButton(Form)
        self.CompressButton.setGeometry(QtCore.QRect(40, 120, 161, 41))
        font.setPointSize(11)
        self.CompressButton.setFont(font)
        self.CompressButton.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px; padding: 8px 0px;")
        self.CompressButton.setObjectName("CompressButton")
        self.CompressButton.hide()
        
        self.CancelButton = QtWidgets.QPushButton(Form)
        self.CancelButton.setGeometry(QtCore.QRect(230, 120, 161, 41))
        font.setPointSize(11)
        self.CancelButton.setFont(font)
        self.CancelButton.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px; padding: 8px 0px;")
        self.CancelButton.setObjectName("CancelButton")

        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(230, 120, 161, 41))
        font.setPointSize(11)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px; padding: 8px 0px;")
        self.exitButton.setObjectName("ExitButton")
        self.exitButton.hide()

        # Error label
        self.error_label = QtWidgets.QLabel("This project already exists")
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setGeometry(QtCore.QRect(40, 120, 250, 51))
        self.error_label.setFont(font)
        self.error_label.setHidden(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
      
        #################BUTTON ACTIONS##################################
        self.CreateButton.clicked.connect(self.create_folders)
        self.CancelButton.clicked.connect(Form.close)
        self.exitButton.clicked.connect(Form.close)
        
        self.project_sP = ""
        self.files = QtWidgets.QListWidget()
        self.VMs = []

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Save Project"))
        self.Projectlabel.setText(_translate("Form", "Project Name:"))
        self.CreateButton.setText(_translate("Form", "Create Project"))
        self.CompressButton.setText(_translate("Form", "Compress"))
        self.CancelButton.setText(_translate("Form", "Cancel"))
        self.exitButton.setText(_translate("Form", "Exit"))

    def pass_lists(self,file_List,VMs):
        self.files = file_List
        self.VMs = VMs

    def create_folders(self):
        self.error_label.setHidden(True)
        self.project_sP = self.ProjectName.text()
        
        # Create Projects root path if does not exist
        if not os.path.exists("Project Data"):
            os.makedirs("Project Data")

        #  Create Project Paths
        if not os.path.exists("../Project Data/" + self.ProjectName.text()):
            print("creating folders....")
            os.makedirs("Project Data/" + self.ProjectName.text())
            os.makedirs("Project Data/" + self.ProjectName.text() + "/VMs/")
            os.makedirs("Project Data/" + self.ProjectName.text() + "/Files/")
            self.CancelButton.hide()
            self.CreateButton.hide()

            self.CompressButton.show()
            self.CompressButton.clicked.connect(self.copy_files)
            print("Project was created")
        else:
            self.error_label.setHidden(False)
            print("Project Name Already Exists")

    ################# Copying Files & Exporting VMs ####################################
    def copy_files(self):
        if(self.files.count()>0):
            print("Copying Files into Project......")
        for i in range(self.files.count()):
            print (self.files.item(i).text())
            shutil.copy(self.files.item(i).text(),"Project Data/" + self.ProjectName.text() + "/Files/")
        
        if self.VMs:
            print("Exporting VMs.....")

        for i in self.VMs:
            dirpath = 'Project Data/'+self.ProjectName.text()+'/VMs'
            filename = i+'.ova'
            out = os.path.join(dirpath,filename)
            command_args = ['vboxmanage','export', i,'--output', out]
            print("Exporting " + i + " VM.....")
            proc = sp.Popen(command_args,stdout=sp.PIPE,stderr=sp.PIPE,shell=True)
            outp, err = proc.communicate()
            print(outp)
            print(err)
             

        self.compress_project()   

    ##TODO: Compress Project folder in Project Data directory
    def compress_project(self):
        dirpath = 'Project Data/'
        print(dirpath)
        self.CompressButton.hide()
        self.exitButton.show()
        shutil.make_archive(dirpath + self.ProjectName.text(),'zip',dirpath,self.ProjectName.text())
        

''' 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = CreateProject(Form)
    Form.show()
    sys.exit(app.exec_())
'''