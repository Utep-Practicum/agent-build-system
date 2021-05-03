from Builder.Relation import *
import json
import os

class Controller:
    def __init__(self):
        self.relationships_main = []
        self.dependencies_main = []
        self.project_name = None


    def load_object(self):
        observation_list = []
        self.relationships_main.clear()
        self.dependencies_main.clear()

        with open("Project Data/"+self.project_name+"/Builder/saved_object2.json") as load_file:
            a = json.load(load_file)

        # Relations
        relations_dictionary = a[0]["Relationships"]
        print(relations_dictionary.keys())
        for key in relations_dictionary.keys():
            index = int(key.split()[1])
            for observation in relations_dictionary[key]:
                print(observation)
                observation_list.append(relations_dictionary[key][observation])
            self.relationships_main.append(Relation(observation_list, index))
            observation_list.clear()

        # Dependencies
        observation_list = []
        dependencies_dictionary = a[1]["Dependencies"]
        print(dependencies_dictionary.keys())
        for key in dependencies_dictionary.keys():
            index = int(key.split()[1])
            for observation in dependencies_dictionary[key]:
                print(observation)
                observation_list.append(dependencies_dictionary[key][observation])
            self.dependencies_main.append(Relation(observation_list, index, True))
            observation_list.clear()

    ################################

    def save_object(self):
        """
        Deep copy of project
        """
        print("save object")
        objectToSave = []

        objectToSaveRelations = {"Relationships": {}}
        objectToSaveDependencies = {"Dependencies": {}}

        for relation in self.relationships_main:
            objectToSaveRelations["Relationships"][relation.name] = {}
            print(relation.name)
            for observation in relation.observation_list:
                objectToSaveRelations["Relationships"][relation.name][observation.index_observation] = {}
                objectToSaveRelations["Relationships"][relation.name][observation.index_observation]['start'] = observation.start
                objectToSaveRelations["Relationships"][relation.name][observation.index_observation]['data'] = observation.data
                objectToSaveRelations["Relationships"][relation.name][observation.index_observation]['data_type'] = observation.data_type
                objectToSaveRelations["Relationships"][relation.name][observation.index_observation]['artifact'] = observation.artifact

        objectToSave.append(objectToSaveRelations)

        # Dependencies
        for dependency in self.dependencies_main:
            objectToSaveDependencies["Dependencies"][dependency.name] = {}
            print(dependency.name)
            for observation in dependency.observation_list:
                objectToSaveDependencies["Dependencies"][dependency.name][observation.index_observation] = {}
                objectToSaveDependencies["Dependencies"][dependency.name][observation.index_observation]['start'] = observation.start
                objectToSaveDependencies["Dependencies"][dependency.name][observation.index_observation]['data'] = observation.data
                objectToSaveDependencies["Dependencies"][dependency.name][observation.index_observation]['data_type'] = observation.data_type
                objectToSaveDependencies["Dependencies"][dependency.name][observation.index_observation]['artifact'] = observation.artifact
            #objectToSave["dependencies"].append(dependency.name)

        objectToSave.append(objectToSaveDependencies)

        with open("Project Data/"+self.project_name+"/Builder/saved_object2.json", 'w') as outfile:
            json.dump(objectToSave, outfile, indent=4)


    def update(self, project):
        # Clear previous data, if any
        self.relationships_main.clear()
        self.dependencies_main.clear()
        self.project_name = project
        """
        # Import relationships into the controller
        """
        relationship_dir = 'Project Data/' + self.project_name + '/CE/Relationships/'
        file_list = []
        for file in os.listdir(relationship_dir):
            file_list.append(file)
        file_list.sort()
        for file_name in file_list:
            with open(relationship_dir + file_name, 'r') as relation:
                self.relationships_main.append(Relation(json.load(relation)))
        ######################################################
        # self.relationships_main.append(Relation(relationship))

    def move_to_dependency(self, relationship):
        """
        # Removes relationship from relationship list and translates to dependency list
        """
        if relationship in self.relationships_main:
            relationship.name = "Dependency " + str(relationship.number)
            self.dependencies_main.append(self.relationships_main.pop(self.relationships_main.index(relationship)))
            return True
        return False

    
    def move_to_relationship(self, dependency):
        """
        # Removes dependency from dependency list and translates to relationship list
        """
        if dependency in self.dependencies_main:
            dependency.name = "Relationship " + str(dependency.number)
            self.relationships_main.append(self.dependencies_main.pop(self.dependencies_main.index(dependency)))
            return True
        return False


    def search(self, keyword = '', table = 'relationships'):
        search = []
        if table.lower() == 'relationships':
            if keyword == '' or keyword == None:
                return self.relationships_main
            else:
                for relation in self.relationships_main:
                    for item in relation.observation_list:
                        if keyword in item.show():
                            search.append(relation)
                            break
                return search
        elif table.lower() == 'dependencies':
            if keyword == '' or keyword == None:
                return self.dependencies_main
            else:
                for relation in self.dependencies_main:
                    for item in relation.observation_list:
                        if keyword in item.show():
                            search.append(relation)
                            break
                return search
