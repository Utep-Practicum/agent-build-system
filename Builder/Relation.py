import os
import json
# from ClickCoordinate import *

counter = 1

class Relation:

    def __init__(self, fields, relation_counter=None, dependency=None, eceld_folder=None):
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
            self.observation_list.append(Observation(item, index,eceld_folder))


class Observation:
        
    def __init__(self, node, index,eceld_folder):
        # Data details and contents
        self.index_observation = index
        self.start = node['start']
        self.data = node['data']
        self.data_type = node['data_type']
        self.artifact = node['artifact']
        self.eceld_folder = eceld_folder
        self.imgName = ""
        self.is_click = True if "clicks_id" in node['data'] else False
        self.coordinateX = 0
        self.coordinateY = 0

        if self.is_click:
            print("FUE CLICK???")
            self.data = node['data']
            img_Name = self.get_image_path(self.data['content'])
            print(f"image: {img_Name}")
            self.data['content'] = img_Name
            img_Name = img_Name.strip()
            print("before coordinates ----")
            analyze = ClickCoordinate()
            print(img_Name[1:].split("/"))
            path_list = img_Name[1:].split("/")
            path_list.insert(4, 'Clicks')
            print(path_list)
            img_Name = '/'.join(path_list)
            img_Name = '/'+img_Name
            print(f"image: {img_Name}")
            analyze.analyze_file(img_Name)
            
            self.coordinateX, self.coordinateY = analyze.click_coord()
            print(f"x: {self.coordinateX}, y: {self.coordinateY}")
            

        # Depicts the time to wait before looking for observation or executing script
        self.delay = 0

        # Information to create script
        if(self.data_type == "Keypresses" or self.data_type == "imgPoint" or self.data_type == "auditd"):
            self.user_action = True
        else:
            self.user_action = False

        self.script = None

        # Selected labels which will be used to filter traffic on the Runner
        self.select_filters = []

        #change to 1 when ignoring observation in script
        self.ignore = 0

    def get_image_path(self,default_content):
        head_tail = os.path.split(default_content)
        pic_name = head_tail[1]
        pic_path = self.eceld_folder+'/'+pic_name
        return pic_path
        

    def show(self):
        string = str(self.index_observation) + ") " + "start: " + str(self.start) + ', ' + "data_type: " + str(self.data_type) + ', ' + "artifact: " + str(self.artifact) + ', ' + "data: " + str(self.data)
        return string
        

if __name__ == '__main__':
    
    directory = '../Causation_Extractor/relationships/'
    file_list = []
    eceld_folder = ""
    for file in os.listdir(directory):
        file_list.append(file)
    file_list.sort()
    for f in file_list:
        with open(directory + f, 'r') as relation:
            temp_relation = Relation(json.load(relation),eceld_folder)
            for item in temp_relation.observation_list:
                print(str(item.data))
                print("-------------")
