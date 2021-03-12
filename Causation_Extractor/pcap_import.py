import json
import time

#Create list dictionary to store all packets
#frames = {}


#frame,eth,ip,tcp
class pcapImport:
    def __init__(self):
        self.frame_info = {}


    def DFS_mapping(self, node):
        for item in node:
            if type(node[item]) == dict:
                self.DFS_mapping(node[item])
            else:
                self.frame_info[item] = node[item]

    '''
        #Export formatted data into a new json file
        try:
            with open('test.json','w') as outfile:
                json.dump(frames, outfile, indent=4)
        except:
            print("Error encountered while creating output file")
    '''