from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os , shutil
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QProcess 
from subprocess import Popen
import time

class ImportProject(object):
    def setupUi(self, ImportProject,ABS_Packager):
        ImportProject.setObjectName("ImportProject")
        ImportProject.resize(650, 200)
        ImportProject.setMinimumSize(QtCore.QSize(650, 200))
        ImportProject.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(ImportProject)
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
        self.fileName.setEnabled(True)
        self.fileName.setGeometry(QtCore.QRect(230, 60, 351, 31))
        self.fileName.setStyleSheet("")
        self.fileName.setReadOnly(True)
        self.fileName.setObjectName("fileName")
        
        ###################### IMPORT BUTTON ####################################
        self.ImportProject_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ImportProject_Button.setGeometry(QtCore.QRect(440, 100, 141, 71))
        self.ImportProject_Button.setFont(font)
        self.ImportProject_Button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.ImportProject_Button.setObjectName("ImportProject_Button")
        
        ##################### EXIT BUTTON #######################################
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(440, 100, 141, 71))
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px; padding: 8px 0px;")
        self.exitButton.setObjectName("ExitButton")
        self.exitButton.hide()
        
        self.abs_folder = QtWidgets.QLabel(self.centralwidget)
        self.abs_folder.setGeometry(QtCore.QRect(90, 20, 301, 31))
        self.abs_folder.setMinimumSize(QtCore.QSize(301, 31))
       
        self.abs_folder.setFont(font)
        self.abs_folder.setObjectName("label")
        self.vms_label = QtWidgets.QLabel(self.centralwidget)
        self.vms_label.setGeometry(QtCore.QRect(110, 100, 111, 31))
        self.vms_label.setMinimumSize(QtCore.QSize(101, 31))
        
        font.setPointSize(12)
        self.vms_label.setFont(font)
        self.vms_label.setStyleSheet("color: black;")
        self.vms_label.setObjectName("time_label")
        self.files_label = QtWidgets.QLabel(self.centralwidget)
        self.files_label.setGeometry(QtCore.QRect(110, 140, 111, 31))
        self.files_label.setMinimumSize(QtCore.QSize(101, 31))
        
        self.files_label.setFont(font)
        self.files_label.setStyleSheet("color: black;")
        self.files_label.setObjectName("files_label")
        
        self.vm_count = QtWidgets.QLabel(self.centralwidget)
        self.vm_count.setGeometry(QtCore.QRect(220, 100, 111, 31))
        self.vm_count.setMinimumSize(QtCore.QSize(101, 31))
        
        self.vm_count.setFont(font)
        self.vm_count.setStyleSheet("color: black;")
        self.vm_count.setObjectName("vm_count")
        
        self.file_count = QtWidgets.QLabel(self.centralwidget)
        self.file_count.setGeometry(QtCore.QRect(220, 140, 111, 31))
        self.file_count.setMinimumSize(QtCore.QSize(101, 31))
        
        self.file_count.setFont(font)
        self.file_count.setStyleSheet("color: black;")
        self.file_count.setObjectName("file_count")
        
        ImportProject.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(ImportProject)
        QtCore.QMetaObject.connectSlotsByName(ImportProject)

        ############################## DIRECTORY DATA VARIABLES ##################
        self.project_directory = str
        self.zip_file = str
        self.vms_directory = str
        self.file_directory = str
    
        self.vm_names = []
        self.file_names = []


        ############################## BUTTON ACTION #############################
        self.Browse_Button.clicked.connect(self.browse_project)
        self.ImportProject_Button.clicked.connect(self.decompress_project)
        self.exitButton.clicked.connect(ImportProject.close)
        self.exitButton.clicked.connect(ABS_Packager.close)

    def browse_project(self):
        # Gets directory name and sets it to a variable
        name = QFileDialog.getOpenFileName(self.Browse_Button, 'Choose ABS Dir', '/home/kali')
        self.zip_file = name[0]
        self.project_directory = self.zip_file[:-4] 
        self.fileName.setText(name[0])
    
    def decompress_project(self):    
        try:
            shutil.unpack_archive(self.zip_file,'Project Data/')
        except Exception as e:
            print(e)
            print('Unable to Decompress File')

        print("ABS dirname:", self.project_directory)
        self.vms_directory = self.project_directory + '/VMs/'
        self.file_directory = self.project_directory + '/Files/'
        if os.path.isdir(self.vms_directory) and os.path.isdir(self.file_directory):
            print("Valid ABS Project Inputted")
            QtWidgets.qApp.processEvents()
            self.get_project_contents(self.vms_directory,self.file_directory)
        else:
            print("Please select a valid ABS Project Directory")


    def get_project_contents(self,vms_directory,file_directory):
        QtWidgets.qApp.processEvents()
        _, _, self.vm_names = next(os.walk(vms_directory))
        self.vm_count.setText(str(len(self.vm_names)))
        print(f"VMs in project: {len(self.vm_names)}")
        print(self.vm_names)
        _, _, self.file_names = next(os.walk(file_directory))
        self.file_count.setText(str(len(self.file_names)))
        print(f"Files in project: {len(self.file_names)}")
        print(self.file_names) 
        self.import_project()
        

    def import_project(self):
        QtWidgets.qApp.processEvents()
        for vm in self.vm_names:
            vm_path = self.vms_directory + vm
            print(f"Importing: {vm}")
            command_args = ['vboxmanage','import', vm_path]
            proc = Popen(command_args,close_fds=True)
            outp, err = proc.communicate()
            if outp:
                print(outp)
            if err:    
                print(err)
        print("Finished Importing Project") 
        self.ImportProject_Button.hide()
        self.exitButton.show()
            
    def retranslateUi(self, ImportWindow):
        _translate = QtCore.QCoreApplication.translate
        ImportWindow.setWindowTitle(_translate("ImportWindow", "Import Project"))
        self.Browse_Button.setText(_translate("ImportWindow", "Browse"))
        self.ImportProject_Button.setText(_translate("ImportWindow", "Import Project"))
        self.abs_folder.setText(_translate("ImportWindow", "ABS Project Folder:"))
        self.vms_label.setText(_translate("ImportWindow", "VMs:"))
        self.files_label.setText(_translate("ImportWindow", "Files:"))
        self.exitButton.setText(_translate("ImportWindow", "Exit"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImportWindow = QtWidgets.QMainWindow()
    ui = ImportProject()
    ui.setupUi(ImportWindow)
    ImportWindow.show()
    sys.exit(app.exec_())
'''