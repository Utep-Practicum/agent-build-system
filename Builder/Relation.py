import os
import json

counter = 1

class Relation:

    def __init__(self, fields):
        global counter
        self.number = counter
        self.name = "Relationship " + str(self.number)
        self.observation_list = []
        counter += 1

        for item in fields:
            self.observation_list.append(Observation(item))


class Observation:

    def __init__(self, node):
        self.start = node['start']
        self.data = node['data']
        self.data_type = node['data_type']
        self.artifact = node['artifact']

    def show(self):
        string = str(self.start) + ',' + str(self.data_type) + ',' + " artifact: " + str(self.artifact) + ',' + str(self.data)
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
