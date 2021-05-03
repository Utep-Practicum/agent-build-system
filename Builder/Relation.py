import os
import json

counter = 1

class Relation:

    def __init__(self, fields, relation_counter=None, dependency=None):
        global counter
        if relation_counter:
            counter = relation_counter
        self.number = counter
        if not dependency:
            self.name = "Relationship " + str(self.number)
        else:
            self.name = "Dependency " + str(self.number)
        self.observation_list = []
        counter += 1
        for index, item in enumerate(fields):
            self.observation_list.append(Observation(item, index))


class Observation:
        
    def __init__(self, node, index):
        # Data details and contents
        self.index_observation = index
        self.start = node['start']
        self.data = node['data']
        self.data_type = node['data_type']
        self.artifact = node['artifact']

        self.select_filters = []

        # Depicts the time to wait before looking for observation or executing script
        self.delay = 0

        # Information to create script
        self.user_action = False
        self.script = None

    def show(self):
        string = str(self.index_observation) + ") " + "start: " + str(self.start) + ', ' + "data_type: " + str(self.data_type) + ', ' + "artifact: " + str(self.artifact) + ', ' + "data: " + str(self.data)
        return string
        

if __name__ == '__main__':
    
    directory = '../Causation_Extractor/relationships/'
    file_list = []
    for file in os.listdir(directory):
        file_list.append(file)
    file_list.sort()
    for f in file_list:
        with open(directory + f, 'r') as relation:
            temp_relation = Relation(json.load(relation))
            for item in temp_relation.observation_list:
                print(str(item.data))
                print("-------------")
