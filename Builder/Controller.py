from Relation import *
from Builder_GUI import *
import json
import os

class Controller:
    def __init__(self, project_directory):
        self.relationships_main = []
        self.dependencies_main = []
        self.project_dir = project_directory


    def add_relationship(self):
        """
        # Import relationships into the controller
        """
        directory = self.project_dir + '/relationships/'
        file_list = []
        for file in os.listdir(directory):
            file_list.append(file)
        file_list.sort()
        for file_name in file_list:
            with open(directory + file_name, 'r') as relation:
                self.relationships_main.append(Relation(json.load(relation)))
        ######################################################
        # self.relationships_main.append(Relation(relationship))

    
    def move_to_dependency(self, relationship_name):
        """
        # Removes relationship from relationship list and translates to dependency list
        """
        self.dependencies_main.append(self.relationships_main.pop(self.relationships_main.index(relationship_name)))

    
    def move_to_relationship(self, relationship_name):
        """
        # Removes dependency from dependency list and translates to relationship list
        """
        self.relationships_main.append(self.dependencies_main.pop(self.dependencies_main.index(relationship_name)))


    def get(self, keyword = '', table = 'relationships'):
        search = []
        if table.lower() == 'relationships':
            if keyword == '' or keyword == None:
                return self.relationships_main
            else:
                for relation in self.relationships_main:
                    for item in relation:
                        if keyword in item.show():
                            search.append(relation)
                            break
                return search
        elif table.lower() == 'dependencies':
            if keyword == '' or keyword == None:
                return self.dependencies_main
            else:
                for relation in self.dependencies_main:
                    for item in relation:
                        if keyword in item.show():
                            search.append(relation)
                            break
                return search


if __name__ == "__main__":
    project = './Causation_Extractor'
    controller = Controller(project)
    controller.add_relationship()

    # I already got the relations
    # pass them to the Builder_GUI
    builder_window = Ui_BuilderWindow(controller)

    # This is just a print...
    for relation in controller.relationships_main:
        print(relation.name)
