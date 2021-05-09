#import sys
#from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit, QScrollArea, QPushButton, QMainWindow, QVBoxLayout,
#                             QGridLayout, QCheckBox)
#from PyQt5.QtGui import QFont
#from PyQt5.QtCore import Qt
#import json
#from subprocess import Popen,PIPE


# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys


class CreateArtifact(QMainWindow):

    def __init__(self, builder):
        super().__init__()
        self.builder = builder

        self.artifact_type = None
        self.artifact_rule = None
        self.initializeUI()

    def initializeUI(self):

        self.setGeometry(100, 100, 600, 550)
        self.setWindowTitle("Create Salient Artifact Rule")

        #self.format_data()
        self.setupWidgets()
        self.show()


    def setupWidgets(self):
        """
        Create widgets for to-do list GUI and arrange them in the window
        """
        # Grid Layout
        main_grid = QGridLayout()
        edit_title = QLabel("Create Salient Artifact Rule")
        edit_title.setFont(QFont('Arial', 20))
        edit_title.setAlignment(Qt.AlignCenter)
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_SA)


        artifact_label = QLabel("Artifact Rule:")
        artifact_label.setAlignment(Qt.AlignRight)

        self.artifact_entry = QTextEdit()
        self.artifact_entry.setMinimumSize(35, 35)

        fields_grid = QGridLayout()
        fields_grid.setContentsMargins(1, 1, 1, 1)
        fields_grid.addWidget(artifact_label, 2, 0)
        fields_grid.addWidget(self.artifact_entry, 2, 1)

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("User Input")
        self.comboBox.addItem("Network Packet")
        #print(comboBox.currentText())
        #comboBox.move(250, 50)

        # Add other layouts to main grid layout
        main_grid.addWidget(edit_title, 0, 0, 1, 2)
        main_grid.addLayout(fields_grid, 1, 0)
        main_grid.addWidget(save_button, 2, 0)
        main_grid.addWidget(self.comboBox,0,0)

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
        self.setLayout(main_grid)

        # For displaying confirmation message along with user's info. 
        #self.label = QLabel(self.centralwidget)    
        #self.label.setGeometry(QtCore.QRect(170, 40, 201, 111))
  
        # Keeping the text of label empty initially.       
        #self.label.setText("dszfds")     

    def save_SA(self, comboBox):
        self.builder.save_controller_state()
        artifact_regex = self.artifact_entry.toPlainText()
        data_type = str(self.comboBox.currentText())
        #print("this finna crash", artifact_regex)
        #print("data_type", data_type)
        if artifact_regex:
            self.close()
            #return (artifact_regex, data_type)
        else:
            self.alert_msg("No Rule Input", "Please input a regex rule before saving. If you do not want to create a rule, close this window")
            #self.close()
            return
        print('is this dead code')
        self.builder.add_new_salient_rule(data_type, artifact_regex)
        #self.builder.display_observation_after_edit()

        #obs: any = None
        #for key in self.data_checkbox:
        #    if self.data_checkbox[key].isChecked():
        #        obs = self.relation_selected.observation_list[self.observation_index]
        #        obs.select_filters.append(key)

        #print("--------- End of save ---------")
        self.close()

    def cancel_edit(self):
        """
        Check if changes were donde, if some changes were done, prompt the user if he wants to save before closing.
        If no changes where done, then proceed to cancel the edit window.
        """
        print("Cancel")

    """
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
    """
    """
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
    """

        ###################### Alert Pop-up Window  #############################
    def alert_msg(self, title, msg):
        print("Error occured: \n\t-Title: %s\n\t-Message: %s\n " %(str(title), str(msg)))
        msgbox = QMessageBox()
        msgbox.setWindowTitle(str(title))
        msgbox.setText(str(msg))
        msgbox.setStyleSheet("QLabel{ color: red}");
        msgbox.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #obs = 'start: 2021-03-09T21:44:36, data_type: imgPoint, artifact: 1, data: {"timed_id": 4, "type": "point", "content": "/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/timed_screenshots/1615326276.49936_screenshot.png"}'
    window = EditForm(obs)
    # window.format_data()
    sys.exit(app.exec_())