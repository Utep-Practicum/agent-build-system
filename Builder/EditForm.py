import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit, QScrollArea, QPushButton, QMainWindow, QVBoxLayout,
                             QGridLayout, QCheckBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import json
from subprocess import Popen,PIPE

class EditForm(QMainWindow):

    def __init__(self, item, relation_selected, builder):
        super().__init__()
        self.builder = builder
        self.relation_selected = relation_selected
        self.observation_selected = item.text()
        #self.observation_chosen = item
        self.observation_index = None
        self.start: str
        self.data_type: str
        self.artifact: str
        self.data_dict: dict = {}
        self.fields_entry: dict = {}
        self.data_checkbox: dict = {}
        self.data_clicked: dict = {}
        self.changes: bool = False
        self.initializeUI()

    def initializeUI(self):

        self.setGeometry(100, 100, 600, 550)
        self.setWindowTitle("Edit")

        self.format_data()
        self.setupWidgets()

        self.start_entry.setText(self.start)
        self.data_type_entry.setText(self.data_type)
        
        self.artifact_entry.setText(self.artifact)
        for tag in self.fields_entry.keys():
            self.fields_entry[tag].setText(str(self.data_dict[tag]))

        print("DATA_DICT")
        print(self.data_dict)
        print("FIELDS_ENTRY")
        print(self.fields_entry)

        self.show()

        self.changes_done()
        # self.start_entry.textChanged.connect(self.changes_done)


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
        self.gimp_button = QPushButton("Open GIMP")
        self.gimp_button.setDisabled(True)
        
        try:
            if self.data_dict['clicks_id'] or self.data_dict['clicks_id'] == 0:
                self.gimp_button.setDisabled(False)
                self.gimp_button.clicked.connect(self.open_gimp)
                
        except Exception as e:
            print(e)
            print("not a click")

        
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

        for tag in self.data_dict.keys():
            self.fields_entry[str(tag)] = QTextEdit()

        # Create labels for appointments seciton
        self.start_entry = QTextEdit()
        self.start_entry.setMinimumSize(35, 35)
        self.data_type_entry = QTextEdit()
        self.data_type_entry.setMinimumSize(35, 35)
        self.artifact_entry = QTextEdit()
        self.artifact_entry.setMinimumSize(35, 35)

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
            data_tag = QCheckBox(tag)
            self.data_checkbox[tag] = data_tag
            field.setMinimumSize(35, 35)
            #data_tag.setAlignment(Qt.AlignRight)
            fields_grid.addWidget(data_tag, row, 0)
            fields_grid.addWidget(field, row, 1)
            row += 1

        # Add other layouts to main grid layout
        main_grid.addWidget(edit_title, 0, 0, 1, 2)
        main_grid.addLayout(fields_grid, 1, 0)
        main_grid.addWidget(save_button, 2, 0)
        main_grid.addWidget(self.gimp_button,3,0)

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
        self.builder.save_controller_state()
        obs: any = None
        for key in self.data_checkbox:
            if self.data_checkbox[key].isChecked():
                obs = self.relation_selected.observation_list[self.observation_index]
                obs.select_filters.append(key)
        if self.changes:
            # Get the same observation from the Relation selected
            observation_object = self.relation_selected.observation_list[self.observation_index]
            observation_object.start = self.start_entry.toPlainText()
            observation_object.data_type = self.data_type_entry.toPlainText()
            observation_object.artifact = self.artifact_entry.toPlainText()

            for key in observation_object.data.keys():
                if type(self.data_dict[key]) == int:
                    observation_object.data[key] = int(self.fields_entry[key].toPlainText())
                    if key == "X_Coordinate":
                        observation_object.coordinateX = observation_object.data[key]
                    elif key == "Y_Coordinate":
                        observation_object.coordinateY = observation_object.data[key]
                else:
                    observation_object.data[key] = self.fields_entry[key].toPlainText()
        else:
            self.close()
            return
        self.builder.display_observation_after_edit()

        print("--------- End of save ---------")
        self.close()

    def open_gimp(self):
        try:
            Popen(['gimp', self.fields_entry['content'].toPlainText()],stdout=PIPE, stderr=PIPE)
        except Exception as e:
            print (e)
            self.gimp_button.setDisabled(True)
            print("Please install GIMP")
    def cancel_edit(self):
        """
        Check if changes were donde, if some changes were done, prompt the user if he wants to save before closing.
        If no changes where done, then proceed to cancel the edit window.
        """
        print("Cancel")

    def changes_done(self):
        """
        Check if changes where done in one of the fields
        :return: boolean
        """
        self.start_entry.textChanged.connect(self.quitamealv)
        self.data_type_entry.textChanged.connect(self.quitamealv)
        self.artifact_entry.textChanged.connect(self.quitamealv)

        for key in self.fields_entry.keys():
            self.fields_entry[key].textChanged.connect(self.quitamealv)
        print()

    def quitamealv(self):
        self.changes = False
        print(self.start_entry.toPlainText())
        if self.start_entry.toPlainText() != self.start:
            print("Changes done in Start")
            self.changes = True
        if self.data_type_entry.toPlainText() != self.data_type:
            print("Changes done in data_type")
            self.changes = True
        if self.artifact_entry.toPlainText() != self.artifact:
            print("Changes done in artifact")
            self.changes = True
        for key in self.fields_entry.keys():
            if type(self.data_dict[key]) == int:
                try:
                    if self.fields_entry[key].toPlainText() == '' or self.data_dict[key] != int(self.fields_entry[key].toPlainText()):
                        print(f"Chages done in {key}")
                        self.changes = True
                except Exception:
                    print("Value has to be an integer")
                    self.changes = False
                    return
            elif self.data_dict[key] != self.fields_entry[key].toPlainText():
                print(f"Chages done in {key}")
                self.changes = True



    def format_data(self):

        start_index = self.observation_selected.find("start")
        parentheses_index = self.observation_selected[:start_index].find(")")
        self.observation_index = int(self.observation_selected[:parentheses_index])
        observation_no_index = self.observation_selected[start_index:]

        data_index = observation_no_index.find(", data:")
        before_data = observation_no_index[:data_index]

        split_data = before_data.strip().split(",")
        # the number is one after the end of each key for start is 7, data_type is 11 and artifact is
        self.start = split_data[0][7:]
        self.data_type = split_data[1].strip()[11:]
        self.artifact = split_data[2].strip()[10:]

        data = observation_no_index[data_index+1:].strip()
        data = data[data.find('{'):]
        data = data[1:-1]

        divided_data = data.split(", '")

        for index in range(1, len(divided_data)):
            divided_data[index] = "'"+divided_data[index]
        self.create_data_dictionary(divided_data)

    def create_data_dictionary(self, divided_data_list):
        '''
        fills the attribute data_dict and the data_clicked with False
        '''
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
            self.data_clicked[key] = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    obs = 'start: 2021-03-09T21:44:36, data_type: imgPoint, artifact: 1, data: {"timed_id": 4, "type": "point", "content": "/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1615326276.49936_screenshot.png"}'
    window = EditForm(obs)
    # window.format_data()
    sys.exit(app.exec_())