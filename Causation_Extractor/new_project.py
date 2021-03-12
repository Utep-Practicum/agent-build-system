import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class NewProject(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 400, 120)
        self.setWindowTitle('Edit Form')
        
        self.setup_widget_layout()

        self.show()
        self.setStyleSheet("background-color: #f4f5f7; color:#13333F;")
 

    def setup_widget_layout(self):

        # Main Label
        content_label = QLabel("Project Name")

        # Buttons
        self.project_name = QLineEdit()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px; padding: 8px 0px;")
        save_btn = QPushButton("Create Project")
        save_btn.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px; padding: 8px 0px;")

        # Button Actions
        cancel_btn.clicked.connect(self.close)
        save_btn.clicked.connect(self.createFolders)

        # Error label
        self.error_label = QLabel("This project already exists")
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setHidden(True)

        # QHBox Layout
        btn_h_box = QHBoxLayout()
        btn_h_box.addWidget(cancel_btn, 10)
        btn_h_box.addWidget(save_btn, 10)
        btn_h_box.addSpacing(10)
        btn_h_box.addStretch()


        form_layout = QFormLayout(self)
        form_layout.addRow(content_label)
        form_layout.addRow(self.project_name)
        form_layout.addRow(btn_h_box)
        form_layout.addRow(self.error_label)


    def createFolders(self):
        print(self.project_name.text())
        self.error_label.setHidden(True)

        # Create Projects root path if does not exist
        if not os.path.exists("Project Data"):
            os.makedirs("Project Data")

        #  Create Project Paths
        if not os.path.exists("Project Data/" + self.project_name.text()):
            os.makedirs("Project Data/" + self.project_name.text())
            os.makedirs("Project Data/" + self.project_name.text() + "/CE/")
            os.makedirs("Project Data/" + self.project_name.text() + "/CE/CE_logs/")
            os.makedirs("Project Data/" + self.project_name.text() + "/CE/Relationships/")
            os.makedirs("Project Data/" + self.project_name.text() + "/Builder/")
            os.makedirs("Project Data/" + self.project_name.text() + "/Builder/Builder_logs/")
            os.makedirs("Project Data/" + self.project_name.text() + "/Builder/Dependencies/")
            os.makedirs("Project Data/" + self.project_name.text() + "/Runner/")
            os.makedirs("Project Data/" + self.project_name.text() + "/Builder/Runner/Runner_logs")
            os.makedirs("Project Data/" + self.project_name.text() + "/Packager/")
            os.makedirs("Project Data/" + self.project_name.text() + "/Packager/Packager_logs")
            self.close()
        else:
            self.error_label.setHidden(False)


if __name__ == '__main__':
    app = QApplication([])
    window = NewProject()
    sys.exit(app.exec_())
