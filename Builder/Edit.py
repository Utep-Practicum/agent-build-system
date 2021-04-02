import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QLabel, QFormLayout, QGroupBox, QTextEdit,
                             QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QFont

class EditForm(QWidget):
    def __init__(self):
        super().__init__()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Edit Form')
        self.setupTabs()
        self.show()
        self.setStyleSheet("background-color: #f4f5f7; color:#13333F;")

    def set_relation(self, relation):
        self.relation = relation
        self.save_btn.clicked.connect(self.save_relation)
        self.content_entry.setText(str(relation.text()))

    def save_relation(self):
        self.relation.setText(self.content_entry.toPlainText())
        self.close()

    def setupTabs(self):
        """
        Set up tab bar an different tab widgets. Each tab is a QWidget that serves as a container for each poge.
        """
        # Create tab bar and different tabs
        self.tab_bar = QTabWidget(self)
        self.edit_tab = QWidget()
        self.tab_bar.addTab(self.edit_tab, "Edit Artifact")

        # Call methods that contain the widgets for each tab
        self.edit_component_tab()

        # Create layout for main window
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.tab_bar)

        # Set main window's layout
        self.setLayout(main_h_box)

    def edit_component_tab(self):
        """
        Create the edit tab. Allows the user enter edit the content of the artifact.
        """
        # Set up labels and text edit widgets
        content_label = QLabel("Content")
        content_label.setFont(QFont('Arial', 15))
        self.content_entry = QTextEdit()

        # Create buttons and set layout
        button_gb = QGroupBox("Sex")
        self.save_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.close)
        self.save_btn.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px; padding: 8px 0px;")
        cancel_btn.setStyleSheet("background-color: #13333F; color: #FFFFFF; border-radius: 5px; padding: 8px 0px;")

        btn_h_box = QHBoxLayout()
        btn_h_box.addWidget(self.save_btn, 10)
        btn_h_box.addWidget(cancel_btn, 10)
        btn_h_box.addStretch()

        # Add all widgets
        tab_v_box = QVBoxLayout()
        tab_v_box.addWidget(content_label)
        tab_v_box.addWidget(self.content_entry)
        tab_v_box.addStretch()

        self.form_layout = QFormLayout()
        self.form_layout.addRow(tab_v_box)
        self.form_layout.addRow(btn_h_box)

        # Set layout for to the tab
        self.edit_tab.setLayout(self.form_layout)

    


if __name__ == '__main__':
    app = QApplication([])
    window = EditForm()
    sys.exit(app.exec_())
