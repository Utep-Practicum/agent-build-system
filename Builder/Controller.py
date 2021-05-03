from Builder.Relation import *
import json
import os
import datetime  # For observation grouping #Delta Time Creation


class Controller:
    def __init__(self):
        self.relationships_main = []
        self.dependencies_main = []
        self.project_name = None


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
        
        self.create_delta()

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

    #NOTE: start is a str before and after translation to deltaTime
    def create_delta(self): 
        for relationship in self.relationships_main:
            #print(relationship.name) #DEBUG
            timeDiff_list = [0.0] #Initial observation will always occur at 0.0 in script

            #Makes DeltaTime Calculations
            for x in range(1, len(relationship.observation_list)):
                currTime = datetime.datetime.strptime(relationship.observation_list[x].start,'%Y-%m-%dT%H:%M:%S')
                pastTime = datetime.datetime.strptime(relationship.observation_list[x-1].start,'%Y-%m-%dT%H:%M:%S')
                timeDiff = currTime-pastTime
                timeDiff_list.append(timeDiff.total_seconds())
                #print("delta:",timeDiff.total_seconds()) #DEBUG

            #Replaces startTime with DeltaTimes, Normalizes times differences that got rounded down to 0
            for y in range(len(relationship.observation_list)):
                if timeDiff_list[y] == 0.0: 
                    relationship.observation_list[y].start = str(timeDiff_list[y]+0.1)
                else:
                    relationship.observation_list[y].start = str(timeDiff_list[y])


    def unified_list(self):
        uni_list = []
        i = 1
        for dep in self.dependencies_main:
            for obs in dep.observation_list:
                if obs.ignore != 1:
                    obs.observation_number = i
                    uni_list.append(obs)
                    i += 1

        return uni_list


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
            # objectToSave[dependency.name] = {}
            print(dependency.name)
            for observation in dependency.observation_list:
                objectToSaveDependencies["Dependencies"][dependency.name][observation.index_observation] = {}
                objectToSaveDependencies["Dependencies"][dependency.name][observation.index_observation]['start'] = observation.start
                objectToSaveDependencies["Dependencies"][dependency.name][observation.index_observation]['data'] = observation.data
                objectToSaveDependencies["Dependencies"][dependency.name][observation.index_observation]['data_type'] = observation.data_type
                objectToSaveDependencies["Dependencies"][dependency.name][observation.index_observation]['artifact'] = observation.artifact
            #objectToSave["dependencies"].append(dependency.name)

        objectToSave.append(objectToSaveDependencies)

        with open("Project Data/"+self.project_name+"/Builder/" + self.project_name + ".json", 'w') as outfile:
            json.dump(objectToSave, outfile, indent=4)


    def load_object(self,project_name):
        """
        Import project
        """
        self.project_name = project_name

        observation_list = []
        self.relationships_main.clear()
        self.dependencies_main.clear()

        with open("Project Data/" + self.project_name + "/Builder/" + self.project_name + ".json", 'r') as load_file:
            a = json.load(load_file)

        # Relations
        relations_dictionary = a[0]["Relationships"]
        for key in relations_dictionary.keys():
            index = int(key.split()[1])
            for observation in relations_dictionary[key]:
                observation_list.append(relations_dictionary[key][observation])
            self.relationships_main.append(Relation(observation_list, index))
            observation_list.clear()


        # Dependencies
        observation_list = []
        dependencies_dictionary = a[1]["Dependencies"]
        for key in dependencies_dictionary.keys():
            index = int(key.split()[1])
            for observation in dependencies_dictionary[key]:
                observation_list.append(dependencies_dictionary[key][observation])
            self.dependencies_main.append(Relation(observation_list, index, True))
            observation_list.clear()