import sys
from  PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QFormLayout, QLabel, QPushButton,
                              QComboBox, QTextEdit, QFileDialog, QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui

class NewSalientArtifact(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.deleted = None
        

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("New Salient Artifact")
        self.formArtifact()
        self.show()
        self.setStyleSheet("background-color: #f4f5f7; color:#13333F;")

    def formArtifact(self):
        title = QLabel("New Salient Artifact")
        title.setFont(QFont('Arial', 18))
        title.setAlignment(Qt.AlignCenter)

        self.typeComboBox = QComboBox()
        self.typeComboBox.addItems(["Select", "Network", "Mouse Clicks", "Keystrokes", "Image"])
        pal = self.typeComboBox.palette()
        pal.setColor(QtGui.QPalette.Button, QtGui.QColor(255,255,255))
        self.typeComboBox.setPalette(pal)
        self.typeComboBox.setStyleSheet("QListView { color:#13333F; background-color: #FFFFFF; }") 


        self.packet_label = QLabel("Packet")
        self.packets = QComboBox()
        self.packets.addItems(["TCP", "UDP", "HTTP"])
        pal = self.packets.palette()
        pal.setColor(QtGui.QPalette.Button, QtGui.QColor(255,255,255))
        self.packets.setPalette(pal)
        self.packets.setStyleSheet("QListView { color:#13333F; background-color: #FFFFFF; }") 

        self.flag_label = QLabel("Flag")
        self.flags = QComboBox()
        self.flags.addItems(["SYN", "ACK", "SYN / ACK"])
        pal = self.flags.palette()
        pal.setColor(QtGui.QPalette.Button, QtGui.QColor(255,255,255))
        self.flags.setPalette(pal)
        self.flags.setStyleSheet("QListView { color:#13333F; background-color: #FFFFFF; }") 

        self.packet_layout = QHBoxLayout()
        self.packet_layout.addStretch()
        self.packet_layout.setSpacing(5)
        self.packet_layout.addWidget(self.packet_label)
        self.packet_layout.addWidget(self.packets, 5)
        self.packet_layout.addWidget(self.flag_label)
        self.packet_layout.addWidget(self.flags, 5)
        self.packet_layout.addStretch()

        # Key strokes
        self.text_field = QTextEdit(self)
        self.text_field.resize(280, 330)
        self.text_layout = QHBoxLayout()
        self.text_layout.addWidget(self.text_field)

        # Image
        self.browse_button = QPushButton("Browse Image")
        self.browse_button.clicked.connect(self.openFile)
        self.browse_button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px; padding: 8px 0px;")

        save_button = QPushButton("Save")
        save_button.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px; padding: 8px 0px;")
        # TODO: Add Save logic

        exit_button = QPushButton("Ext")
        # TODO: Close

        self.layout_buttons = QHBoxLayout()
        self.layout_buttons.addStretch()
        self.layout_buttons.addSpacing(10)
        self.layout_buttons.addWidget(save_button)
        self.layout_buttons.addWidget(exit_button)

        self.form_layout = QFormLayout()
        self.form_layout.addRow(title)
        self.form_layout.addRow("Type  ", self.typeComboBox)
        self.form_layout.addRow(self.packet_layout)
        self.form_layout.addRow(self.text_field)
        self.form_layout.addRow(self.browse_button)
        self.form_layout.addRow(save_button)
        self.form_layout.setSpacing(20)
        self.setLayout(self.form_layout)

        self.packet_label.hide()
        self.packets.hide()
        self.flag_label.hide()
        self.flags.hide()
        self.text_field.hide()
        self.browse_button.hide()

        self.typeComboBox.activated[str].connect(self.showComboBoxes)




    def showComboBoxes(self, option):
        if option == "Select":
            self.packet_label.hide()
            self.packets.hide()
            self.flag_label.hide()
            self.flags.hide()
            self.text_field.hide()
            self.browse_button.hide()

        elif option == "Network":
            self.packet_label.show()
            self.packets.show()
            self.flag_label.show()
            self.flags.show()

            self.text_field.hide()

            self.browse_button.hide()
        elif option == "Keystrokes":
            self.packet_label.hide()
            self.packets.hide()
            self.flag_label.hide()
            self.flags.hide()

            self.browse_button.hide()

            self.text_field.show()
        elif option == "Mouse Clicks":
            print()
        elif option == "Image":
            self.packet_label.hide()
            self.packets.hide()
            self.flag_label.hide()
            self.flags.hide()

            self.text_field.hide()

            self.browse_button.show()


    def openFile(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', "", 'All Files(*);;Text Files(*.txt)',
                                                   options=options)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewSalientArtifact()
    sys.exit(app.exec_())