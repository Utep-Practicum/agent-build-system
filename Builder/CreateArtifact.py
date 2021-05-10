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
  

    def save_SA(self, comboBox):
        self.builder.save_controller_state()
        artifact_regex = self.artifact_entry.toPlainText()
        data_type = str(self.comboBox.currentText())

        #fix variable to match observation types
        if data_type != None and data_type == "User Input":
            data_type = "auditd"
        if data_type != None and data_type == "Network Packet":
            data_type = "network"

     
        if artifact_regex:
            self.close() #?????
        else:
            self.alert_msg("No Rule Input", "Please input a regex rule before saving. If you do not want to create a rule, close this window")
            return
        self.builder.add_new_salient_rule(data_type, artifact_regex) #Send new rule back to Builder
        self.close()

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
    window = EditForm(obs)
    sys.exit(app.exec_())