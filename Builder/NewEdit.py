import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit, QScrollArea, QPushButton, QMainWindow, QVBoxLayout,
                             QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import json

class EditForm(QMainWindow):

    def __init__(self, item):
        super().__init__()
        self.obs = item.text()
        self.start: str
        self.data_type: str
        self.artifact: str
        self.data_dict: dict = {}
        self.fields_entry: dict = {}
        self.initializeUI()

    def initializeUI(self):

        self.setGeometry(100, 100, 500, 350)
        self.setWindowTitle("Edit")

        self.format_data()
        self.setupWidgets()

        self.start_entry.setText(self.start)
        self.data_type_entry.setText(self.data_type)
        self.artifact_entry.setText(self.artifact)
        for tag in self.fields_entry.keys():
            self.fields_entry[tag].setText(str(self.data_dict[tag]))

        print(self.data_dict)
        print(self.fields_entry)

        self.show()

    def setupWidgets(self):
        """
        Create widgets for to-do list GUI and arrange them in the window
        """
        # Grid Layout
        main_grid = QGridLayout()
        edit_title = QLabel("Edit Observation")
        edit_title.setFont(QFont('Arial', 20))
        edit_title.setAlignment(Qt.AlignCenter)
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_modifications)
        cancel_button = QPushButton("Cancel")

        # Create Section labels for to-do list
        tags_label = QLabel("Tags")
        tags_label.setFont(QFont('Arial', 20))
        tags_label.setAlignment(Qt.AlignCenter)

        fields_label = QLabel("Fields")
        fields_label.setFont(QFont('Arial', 20))
        fields_label.setAlignment(Qt.AlignCenter)

        start_label = QLabel("start:")
        start_label.setAlignment(Qt.AlignRight)

        data_type_label = QLabel("data type:")
        data_type_label.setAlignment(Qt.AlignRight)

        artifact_label = QLabel("artifact:")
        artifact_label.setAlignment(Qt.AlignRight)



        # tags_layout = QVBoxLayout()
        # tags_layout.setContentsMargins(1, 0, 1, 0)
        # tags_layout.addWidget(start_label)
        # tags_layout.addWidget(data_type_label)
        # tags_layout.addWidget(artifact_label)


        for tag in self.data_dict.keys():
            self.fields_entry[str(tag)] = QTextEdit()

        # Create labels for appointments seciton
        self.start_entry = QTextEdit()
        self.start_entry.setMinimumSize(30, 30)
        self.data_type_entry = QTextEdit()
        self.data_type_entry.setMinimumSize(30, 30)
        self.artifact_entry = QTextEdit()
        self.artifact_entry.setMinimumSize(30, 30)

        fields_grid = QGridLayout()
        fields_grid.setContentsMargins(5, 5, 5, 5)
        fields_grid.addWidget(start_label, 0, 0)
        fields_grid.addWidget(self.start_entry, 0, 1)
        fields_grid.addWidget(data_type_label, 1, 0)
        fields_grid.addWidget(self.data_type_entry, 1, 1)
        fields_grid.addWidget(artifact_label, 2, 0)
        fields_grid.addWidget(self.artifact_entry, 2, 1)

        row = 3

        for tag, field in self.fields_entry.items():
            data_tag = QLabel(tag)
            field.setMinimumSize(30, 30)
            data_tag.setAlignment(Qt.AlignRight)
            fields_grid.addWidget(data_tag, row, 0)
            fields_grid.addWidget(field, row, 1)
            row += 1



        # Add other layouts to main grid layout
        main_grid.addWidget(edit_title, 0, 0, 1, 2)
        main_grid.addLayout(fields_grid, 1, 0)
        main_grid.addWidget(save_button, 2, 0)

        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        self.vbox.addLayout(main_grid)

        self.widget.setLayout(self.vbox)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)
        # self.setLayout(main_grid)

    def save_modifications(self):
        print()

    def format_data(self):

        data_index = self.obs.find(", data:")
        before_data = self.obs[:data_index]
        split_data = before_data.strip().split(",")

        self.start = split_data[0].split()[1]
        self.data_type = split_data[1].strip().split()[1]
        self.artifact = split_data[2].strip().split()[1]

        data = self.obs[data_index+1:].strip()
        print(data)
        data = data[data.find('{'):]
        print(data)

        data = data[1:-1]
        print(data)

        divided_data = data.split(", '")
        print(divided_data)

        for index in range(1, len(divided_data)):
            divided_data[index] = "'"+divided_data[index]
            print(divided_data[index])
        print(divided_data)
        self.create_data_dictionary(divided_data)

    def create_data_dictionary(self, divided_data_list):
        for pair_data in divided_data_list:
            divider = pair_data.find(" ")
            # print(pair_data[:divider-1])
            key = pair_data[:divider-1]
            key = key[1:-1]
            value = pair_data[divider+1:]
            if value.isnumeric():
                value = int(value)
            else:
                value = value[1:-1]
            self.data_dict[key] = value

            print(pair_data)
        print(self.data_dict)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    obs = 'start: 2021-03-09T21:44:36, data_type: imgPoint, artifact: 1, data: {"timed_id": 4, "type": "point", "content": "/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1615326276.49936_screenshot.png"}'
    window = EditForm(obs)
    # window.format_data()
    sys.exit(app.exec_())