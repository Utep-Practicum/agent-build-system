import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox, QVBoxLayout,
                             QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Edit(QWidget):
    # def __init__(self, relation, item):
    #     super().__init__()
    #     self.relation_object = relation
    #     self.item_selected = item.text()
    #     print("----- NewEditForm -----")
    #     print(self.item_selected)
    #     print(self.relation_object.name)
    #     self.initializeUI()

    def __int__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 500, 350)
        self.setWindowTitle("Edit")
        self.setupWidgets()
        self.show()

    def setupWidgets(self):
        """
        Create widgets for to-do list GUI and arrange them in the window
        """

        # Grid Layout
        main_grid = QGridLayout()
        edit_title = QLabel("Edit Observation")
        edit_title.setFont(QFont('Arial', 24))
        edit_title.setAlignment(Qt.AlignCenter)
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_modifications)
        cancel_button = QPushButton("Cancel")



        # Create Section labels for to-do list
        tags_label = QLabel("Tags")
        tags_label.setFont(QFont('Arial', 20))
        tags_label.setAlignment(Qt.AlignCenter)
        appts_label = QLabel("Fields")
        appts_label.setFont(QFont('Arial', 20))
        appts_label.setAlignment(Qt.AlignCenter)

        start_label = QLabel("start:")
        start_label.setAlignment(Qt.AlignRight)

        data_type_label = QLabel("data type:")
        data_type_label.setAlignment(Qt.AlignRight)

        artifact_label = QLabel("artifact:")
        artifact_label.setAlignment(Qt.AlignRight)

        data_label = QLabel("data:")
        data_label.setAlignment(Qt.AlignRight)

        # Create labels for appointments seciton
        start_entry = QTextEdit()
        data_entry = QTextEdit()
        data_type_entry = QTextEdit()
        artifact_entry = QTextEdit()

        edit_grid = QGridLayout()
        edit_grid.addWidget(start_label, 0, 0)
        edit_grid.addWidget(start_entry, 0, 1)

        # Create vertical layout and add widgets
        # fields_v_box = QVBoxLayout()
        # fields_v_box.setContentsMargins(5, 5, 5, 5)
        # fields_v_box.addWidget(start_entry)
        # fields_v_box.addWidget(data_entry)
        # fields_v_box.addWidget(data_type_entry)
        # fields_v_box.addWidget(artifact_entry)

        # Add other layouts to main grid layout
        main_grid.addWidget(edit_title, 0, 0, 1, 2)
        #main_grid.addLayout(edit_grid, 1, 0)
        # main_grid.addLayout(tags_layout, 1, 0)
        # main_grid.addLayout(fields_v_box, 1, 1)
        #main_grid.addWidget(save_button, 2, 0, 1, 2)

        self.setLayout(main_grid)

    def save_modifications(self):
        print()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Edit()
    sys.exit(app.exec_())
