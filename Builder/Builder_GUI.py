# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Builder_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Builder_Window(object):
    def setupUi(self, Builder_Window):
        Builder_Window.setObjectName("Builder_Window")
        Builder_Window.setEnabled(True)
        Builder_Window.resize(800, 617)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setKerning(False)
        Builder_Window.setFont(font)
        Builder_Window.setStyleSheet("background-color: #f4f5f7;")
        Builder_Window.setAnimated(True)
        Builder_Window.setDocumentMode(False)
        Builder_Window.setTabShape(QtWidgets.QTabWidget.Rounded)
        Builder_Window.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(Builder_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.Relations_view = QtWidgets.QListView(self.centralwidget)
        self.Relations_view.setGeometry(QtCore.QRect(20, 340, 521, 221))
        self.Relations_view.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; border: 1px solid #D2D6E0;")
        self.Relations_view.setObjectName("Relations_view")
        self.Network_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.Network_checkBox.setGeometry(QtCore.QRect(580, 130, 151, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.Network_checkBox.setFont(font)
        self.Network_checkBox.setStyleSheet("color: #13333F;")
        self.Network_checkBox.setObjectName("Network_checkBox")
        self.MouseClicks_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.MouseClicks_checkBox.setGeometry(QtCore.QRect(580, 160, 151, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.MouseClicks_checkBox.setFont(font)
        self.MouseClicks_checkBox.setStyleSheet("color: #13333F;")
        self.MouseClicks_checkBox.setObjectName("MouseClicks_checkBox")
        self.Keystroke_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.Keystroke_checkBox.setGeometry(QtCore.QRect(580, 190, 151, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Keystroke_checkBox.setFont(font)
        self.Keystroke_checkBox.setStyleSheet("color: #13333F;")
        self.Keystroke_checkBox.setObjectName("Keystroke_checkBox")
        self.Screenshots_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.Screenshots_checkBox.setGeometry(QtCore.QRect(580, 220, 161, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Screenshots_checkBox.setFont(font)
        self.Screenshots_checkBox.setStyleSheet("color: #13333F;")
        self.Screenshots_checkBox.setObjectName("Screenshots_checkBox")
        self.Filters_label = QtWidgets.QLabel(self.centralwidget)
        self.Filters_label.setGeometry(QtCore.QRect(580, 100, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.Filters_label.setFont(font)
        self.Filters_label.setAutoFillBackground(False)
        self.Filters_label.setStyleSheet("color: #13333F;")
        self.Filters_label.setObjectName("Filters_label")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(580, 270, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 51, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 51, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 51, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 51, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 51, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 51, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 51, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 51, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 51, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.saveButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setAutoFillBackground(False)
        self.saveButton.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.saveButton.setObjectName("saveButton")
        self.NRelationship_Button = QtWidgets.QPushButton(self.centralwidget)
        self.NRelationship_Button.setGeometry(QtCore.QRect(580, 320, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.NRelationship_Button.setFont(font)
        self.NRelationship_Button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.NRelationship_Button.setObjectName("NRelationship_Button")
        self.NSArtifact_Button = QtWidgets.QPushButton(self.centralwidget)
        self.NSArtifact_Button.setGeometry(QtCore.QRect(580, 370, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NSArtifact_Button.setFont(font)
        self.NSArtifact_Button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px;")
        self.NSArtifact_Button.setObjectName("NSArtifact_Button")
        self.Filters_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.Filters_label_2.setGeometry(QtCore.QRect(20, 10, 135, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Filters_label_2.setFont(font)
        self.Filters_label_2.setAutoFillBackground(False)
        self.Filters_label_2.setStyleSheet("color: #13333F;")
        self.Filters_label_2.setObjectName("Filters_label_2")
        self.RelationshipsWidget = QtWidgets.QListWidget(self.centralwidget)
        self.RelationshipsWidget.setGeometry(QtCore.QRect(20, 40, 521, 281))
        self.RelationshipsWidget.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; border: 1px solid #D2D6E0; color: #13333F;")
        self.RelationshipsWidget.setObjectName("RelationshipsWidget")
        Builder_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Builder_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("color: black")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Builder_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Builder_Window)
        self.statusbar.setObjectName("statusbar")
        Builder_Window.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(Builder_Window)
        self.actionNew.setObjectName("actionNew")
        self.actionCreate_New_Relationship = QtWidgets.QAction(Builder_Window)
        self.actionCreate_New_Relationship.setObjectName("actionCreate_New_Relationship")
        self.actionCreate_New_Salient_Artifact = QtWidgets.QAction(Builder_Window)
        self.actionCreate_New_Salient_Artifact.setObjectName("actionCreate_New_Salient_Artifact")
        self.actionREADME = QtWidgets.QAction(Builder_Window)
        self.actionREADME.setObjectName("actionREADME")
        self.actionSave = QtWidgets.QAction(Builder_Window)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCreate_New_Relationship)
        self.menuEdit.addAction(self.actionCreate_New_Salient_Artifact)
        self.menuHelp.addAction(self.actionREADME)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.Keystroke_checkBox.stateChanged.connect(self.test_fuction)
        self.Network_checkBox.stateChanged.connect(self.test_fuction)
        self.MouseClicks_checkBox.stateChanged.connect(self.test_fuction)
        self.Screenshots_checkBox.stateChanged.connect(self.test_fuction)

        self.retranslateUi(Builder_Window)
        QtCore.QMetaObject.connectSlotsByName(Builder_Window)

    def test_fuction(self):
        print(self.Network_checkBox.isChecked())
        self.RelationshipsWidget.clear()
        if (self.Network_checkBox.isChecked()):
            items = ["Network 1", "Network 2", "Network 3"]
            for item in items:
                self.RelationshipsWidget.addItem(item)
        if (self.Keystroke_checkBox.isChecked()):
            items = ["Keystroke 1", "Keystroke 2", "Keystroke 3"]
            for item in items:
                self.RelationshipsWidget.addItem(item)
        if (self.MouseClicks_checkBox.isChecked()):
            items = ["Mouse Click 1", "Mouse Click 2", "Mouse Click 3"]
            for item in items:
                self.RelationshipsWidget.addItem(item)
        if (self.Screenshots_checkBox.isChecked()):
            items = ["Screenshot 1", "Screenshot 2", "Screenshot 3"]
            for item in items:
                self.RelationshipsWidget.addItem(item)

    def retranslateUi(self, Builder_Window):
        _translate = QtCore.QCoreApplication.translate
        Builder_Window.setWindowTitle(_translate("Builder_Window", "MainWindow"))
        self.Network_checkBox.setText(_translate("Builder_Window", "Networks"))
        self.MouseClicks_checkBox.setText(_translate("Builder_Window", "Mouse Clicks"))
        self.Keystroke_checkBox.setText(_translate("Builder_Window", "Keystrokes"))
        self.Screenshots_checkBox.setText(_translate("Builder_Window", "Timed Screenshots"))
        self.Filters_label.setText(_translate("Builder_Window", "Filters"))
        self.saveButton.setStatusTip(_translate("Builder_Window", "Save File"))
        self.saveButton.setText(_translate("Builder_Window", "SAVE"))
        self.NRelationship_Button.setStatusTip(_translate("Builder_Window", "Create a New Relationship"))
        self.NRelationship_Button.setText(_translate("Builder_Window", "NEW RELATIONSHIP"))
        self.NSArtifact_Button.setStatusTip(_translate("Builder_Window", "Create a New Salient Artifact"))
        self.NSArtifact_Button.setText(_translate("Builder_Window", "NEW SALIENT ARTIFACT"))
        self.Filters_label_2.setText(_translate("Builder_Window", "Relationships"))
        self.menuFile.setTitle(_translate("Builder_Window", "File"))
        self.menuEdit.setTitle(_translate("Builder_Window", "Edit"))
        self.menuHelp.setTitle(_translate("Builder_Window", "Help"))
        self.actionNew.setText(_translate("Builder_Window", "New"))
        self.actionCreate_New_Relationship.setText(_translate("Builder_Window", "Create New Relationship"))
        self.actionCreate_New_Relationship.setStatusTip(_translate("Builder_Window", "Create a New Relationship"))
        self.actionCreate_New_Salient_Artifact.setText(_translate("Builder_Window", "Create New Salient Artifact"))
        self.actionREADME.setText(_translate("Builder_Window", "README"))
        self.actionSave.setText(_translate("Builder_Window", "Save"))
        self.actionSave.setStatusTip(_translate("Builder_Window", "Save File"))
        self.actionSave.setShortcut(_translate("Builder_Window", "Ctrl+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Builder_Window = QtWidgets.QMainWindow()
    ui = Ui_Builder_Window()
    ui.setupUi(Builder_Window)
    Builder_Window.show()
    sys.exit(app.exec_())
