# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packager_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from CreateProject import *
import virtualbox


class Ui_ABS_Packager(object):

    def setupUi(self, ABS_Packager):
        self.ABS_Packager = ABS_Packager
        self.ABS_Packager.setObjectName("ABS_Packager")
        self.ABS_Packager.resize(662, 246)
        self.ABS_Packager.setMinimumSize(QtCore.QSize(662,220))
        font = QtGui.QFont()

        self.scroll_bar = QtWidgets.QScrollBar()
        self.scroll_bar.setStyleSheet("background: white;")
        self.scroll_bar2 = QtWidgets.QScrollBar()
        self.scroll_bar2.setStyleSheet("background: white;")

        self.machine_list = QtWidgets.QListWidget(self.ABS_Packager)
        self.machine_list.setGeometry(QtCore.QRect(30, 40, 231, 161))
        self.machine_list.setVerticalScrollBar(self.scroll_bar)
        self.machine_list.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; border: 1px solid #D2D6E0; color: #13333F;")
        self.machine_list.setObjectName("machine_list")

        self.export_button = QtWidgets.QPushButton(self.ABS_Packager)
        self.export_button.setGeometry(QtCore.QRect(280, 130, 101, 61))

        font.setPointSize(12)
        self.export_button.setFont(font)
        self.export_button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.export_button.setObjectName("export_button")

        self.select_files_button = QtWidgets.QPushButton(self.ABS_Packager)
        self.select_files_button.setGeometry(QtCore.QRect(280, 50, 101, 61))
        font.setPointSize(11)
        self.select_files_button.setFont(font)
        self.select_files_button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.select_files_button.setObjectName("select_files_button")
        

        self.file_List = QtWidgets.QListWidget(self.ABS_Packager)
        self.file_List.setGeometry(QtCore.QRect(400, 40, 231, 161))
        self.file_List.setVerticalScrollBar(self.scroll_bar2)
        self.file_List.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; border: 1px solid #D2D6E0; color: #13333F;")
        self.file_List.setObjectName("file_List")
        self.file_List.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.file_List.customContextMenuRequested[QtCore.QPoint].connect(self.contextMenuEvent)

        self.VMs_label = QtWidgets.QLabel(self.ABS_Packager)
        self.VMs_label.setGeometry(QtCore.QRect(40, 20, 181, 16))
        self.VMs_label.setStyleSheet("color:black;")
        font.setPointSize(12)
        self.VMs_label.setFont(font)
        self.VMs_label.setObjectName("VMs_label")
        self.files_label = QtWidgets.QLabel(self.ABS_Packager)
        self.files_label.setStyleSheet("color:black;")
        self.files_label.setGeometry(QtCore.QRect(410, 20, 181, 16))
        self.files_label.setFont(font)
        self.files_label.setObjectName("files_label")
        
    ################# Entry Actions ##################################
        '''When Packager is executed, first gather VMs in host and show their names.'''
        self.populate_machineList()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.ABS_Packager)

    ############ Creating Objects to execute Save Project Window #####
        self.Form = QtWidgets.QDialog()
        self.sP = CreateProject(self.Form,self.ABS_Packager)

    ################# Button Actions #################################
        self.export_button.clicked.connect(self.export)    
        self.select_files_button.clicked.connect(self.select_files)

    ##################################################################    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.ABS_Packager.setWindowTitle(_translate("ABS_Packager", "ABS_Packager"))
        self.export_button.setText(_translate("ABS_Packager", "Export"))
        self.select_files_button.setText(_translate("ABS_Packager", "Select Files"))
        self.VMs_label.setText(_translate("ABS_Packager", "Virtual Machines:"))
        self.files_label.setText(_translate("ABS_Packager", "Files:"))

    ################ Right Click Menu ###################################
    '''For now, right click menu only needs delete selected file functionality'''
    def contextMenuEvent(self):
        rightMenu = QtWidgets.QMenu(self.file_List)
        removeAction = QtWidgets.QAction("Delete")
        row_temp = self.file_List.selectedItems()
        for temp in row_temp:
            row_num = self.file_List.row(temp)
            removeAction.triggered.connect(lambda: self.file_List.takeItem(row_num))
            print("Deleting item in file list")
        rightMenu.addAction(removeAction)
        rightMenu.exec_(QtGui.QCursor.pos())

    ####################### Gather Available VMs from Host###############################
    def populate_machineList(self):
        font = QtGui.QFont()
        font.setPointSize(10)
        vbox = virtualbox.VirtualBox()
        for m in vbox.machines:
            self.machine_name = QtWidgets.QListWidgetItem()
            self.machine_name.setFont(font)
            self.machine_name.setText(m.name)
            self.machine_name.setFlags(self.machine_name.flags() | QtCore.Qt.ItemIsUserCheckable)
            self.machine_name.setCheckState(QtCore.Qt.Unchecked)
            self.machine_list.addItem(self.machine_name)

    ###################### Select and Import Files Functionality ########################
    def select_files(self):
        try:
            file_names = QFileDialog.getOpenFileNames()
            print(file_names)
            print("Selected Files:")
            i = 0
            while i < len(file_names[0]):
                if file_names[0][i] == "All Files (*)":
                   continue 
                self.file_List.addItem(file_names[0][i])
                print(file_names[0][i])
                i = i + 1
        except Exception as e:
            print(e)

    ####################### Export Button Functionality #################################
    def export(self):
        self.Form.show()
        checked_vms = []
        '''Add Selected VM's Name to New List'''
        for i in range(self.machine_list.count()):
            if self.machine_list.item(i).checkState() == Qt.Checked:
                checked_vms.append(self.machine_list.item(i).text())
        '''Send File & VM List to CreateProject.py'''        
        self.sP.pass_objects(self.file_List,checked_vms)


######################### PACKAGER WINDOW EXECUTION CALLS ###############################
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ABS_Packager = QtWidgets.QMainWindow()
    ui = Ui_ABS_Packager()
    ui.setupUi(ABS_Packager)
    ABS_Packager.show()
    sys.exit(app.exec_())
