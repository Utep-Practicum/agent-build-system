import os
import json
from Builder.Coordinates.ClickCoordinate import ClickCoordinate

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
        self.imgName = str
        self.is_click = True if "clicks_id" in node['data'] else False

        # If Click image detected, get coordinates and save them as object data
        if self.is_click:
            self.data = node['data']
            img_Name = self.get_image_path(self.data['content'])
            self.data['content'] = img_Name
            self.coordinateX = 0
            self.coordinateY = 0
            self.button = 'left'
            self.clicks = 1
            self.data['clicks'] = self.clicks
            self.data['button'] = self.button
            try:
                analyze = ClickCoordinate()
                analyze.analyze_file(img_Name)
                self.coordinateX, self.coordinateY = analyze.click_coord()
                self.data['X_Coordinate'] = int(self.coordinateX)
                self.data['Y_Coordinate'] = int(self.coordinateY)
            except Exception as e:
                # If algorithm cannot determine the coordinates, they will be set to (0,0)
                print(e)
                self.data['X_Coordinate'] = 0
                self.data['Y_Coordinate'] = 0    
            #print(f"image: {img_Name}")
            #print(f"x: {self.coordinateX}, y: {self.coordinateY}")
            

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

    # Get location of image for further analysis
    def get_image_path(self,default_content):
        head_tail = os.path.split(default_content)
        pic_name = head_tail[1]
        pic_path = self.eceld_folder+'/Clicks/'+pic_name
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
