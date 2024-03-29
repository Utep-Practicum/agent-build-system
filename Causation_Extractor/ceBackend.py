import json  # for reading files
import os  # for accessing files
import datetime  # For observation grouping
import re  # for regex in artifact discovery
import os
from dateutil.parser import parse  # normalize packet time method
from Causation_Extractor.pcap_import import pcapImport

class ceBackend:

    def __init__(self):
        self.master_json = "Causation_Extractor/masterJson.json"
        self.sa_file_path = "Causation_Extractor/regexLists/default.json"


    project_Name = " "
    def output_directory(self,directory,name):
        # Get filenames from the given directory (preferably "parsedLogs" within the eceld system)
        file_list = []
        head = []

        # Convert AnnotatedPCAP.pcapng to a readable .json file for relationship extraction
        pcap_in = directory.decode() + '/PCAP/'
        parsed_logs = directory.decode() + '/ParsedLogs/'
        if 'pcap_output.json' not in os.listdir(parsed_logs):
            pcap_cmd = 'tshark -r {0}AnnotatedPCAP.pcapng -T json > {1}pcap_output.json'.format(pcap_in, parsed_logs)
            os.system(pcap_cmd)

        for file in os.listdir(parsed_logs):
            file_list.append(file)

        # Stores all json file contents within the "causationSource" json file
        # output file name
        with open(self.master_json, "w") as outfile:
            for f in file_list:
                with open(parsed_logs + f, 'rb') as infile:
                    if f == "pcap_output.json":  # start adding 3/8/21
                       #print("converting pcap file")
                        data = json.load(infile)
                        packetList = []
                        node = pcapImport()
                        for i in range(len(data)):
                            node.DFS_mapping(data[i])
                            frame_time = str(node.frame_info["frame.time"])
                            packetList.append({"start":frame_time}) #The initial time of the frame capture
                            packetList[i]["data"] = node.frame_info.copy() #Frame information
                            packetList[i]["data_type"] = "network" #Packet type
                            node.frame_info.clear() #Clears node before next capture
                        #print(packetList)
                        head += packetList
                    else:
                        file_data = json.load(infile)
                        array = []
                        for line in file_data:
                            array.append(self.format_data(line))
                        head += array
            json.dump(head, outfile, indent=4)
        print("Done enumerating files")

        #self.project_Name = project_name
        #print(self.project_Name)

        ##Set num_lines count to the MouseClicks.json file number of lines for now
        num_lines = self.count_lines(parsed_logs + str(file_list[1]))
        with open(self.master_json) as jsonFile:
            self.text = jsonFile.read()

        return num_lines

    # Reformat contents of the parsed logs
    def format_data(self,line):
        data = {}
        temp_dict = {}
        for item in line:
            if item == 'start':
                temp_dict['start'] = line[item]
            elif item.lower() == 'classname':
                temp_dict['data_type'] = line[item]
            else:
                data[item] = line[item]
        temp_dict['data'] = data
        return temp_dict

    ##TODO: Find a better indicator for progress bar
    # Count lines in file for progress bar
    def count_lines(self, filename):
        num_lines = sum(1 for line in open(filename))
        return num_lines

    # defines the relationships based on the master json file created by ce_gui
    def relationshipDefiner(self,time_in):
        with open(self.master_json) as jsonFile:
            # jsons are loaded as a list of dicts. each dict is a json block
            data = json.load(jsonFile)

            for observation in data:  # Converts PCAP observations to a readable format
                if observation["data_type"] == "network":
                    observation["start"] = parse(observation["start"])
                    observation["start"] = observation["start"] + datetime.timedelta(hours=5)
                    observation["start"] = observation["start"].strftime('%Y-%m-%dT%H:%M:%S')

            sortTest = sorted(data, key=lambda i: i["start"])
        timeframe = datetime.timedelta(seconds=time_in)  # Check in 5 second blocks
        startTime = datetime.datetime.strptime(sortTest[0]["start"], '%Y-%m-%dT%H:%M:%S')  # Init time to check against
        endTime = startTime + timeframe
        relationshipList = []
        tempList = []
        auditD_found = 0

        for block in sortTest:  # Sort through json blocks, adding each to their relationship
            dateTimeObj = datetime.datetime.strptime(block["start"], '%Y-%m-%dT%H:%M:%S')

            if 'timed_id' in block.keys():  # Screenshot elements are only important after commands, and we only want 1
                if auditD_found:
                    tempList.append(block)
                    auditD_found = 0
                else:  # If a screenshot is found but not before a command, we ignore it
                    pass
            else:  # All logs that aren't screenshots get added

                if 'auditd_id' or 'keypresses_id' in block.keys():  # Turn boolean back on if we find an audit/keypress log
                    auditD_found = 1
                tempList.append(block)

            if dateTimeObj > endTime:  # Once 1st element outside of timeframe appears, store relationship and reset vars.
                relationshipList.append(tempList)
                startTime = datetime.datetime.strptime(block["start"], '%Y-%m-%dT%H:%M:%S')
                endTime = startTime + timeframe
                tempList = []
        # print(len(relationshipList))
        #self.outputRelationships(relationshipList)

        # Relationships look like the following
        # relationshipList[0], Each index is a relationship
        # relationshipList[0][0], each index is an observation
        # relationship[0][0]["fieldName"], each index is a key:value pair from the json.
        return relationshipList

    # Finds artifacts
    def makeArtifacts(self, relationshipList, sa_file_path):
        #addr = 'Causation_Extractor/regexLists/userKeywords.txt'
        #regexList = [line.rstrip() for line in open(addr)]
        count = 0

        #artifactFile = open('Causation_Extractor/regexLists/default.json',) #Change to be self.Whatevr
        print("make artifact sa file import!:", sa_file_path)
        artifactFile = open(sa_file_path,)
        artifactData = json.loads(artifactFile.read())

        auditdList =  artifactData['auditd']
        networkList = artifactData['network']


        #Goes through observations and tags qualifying observations based on Salient Artifact regex
        for relationship in relationshipList:
            for observation in relationship:

                #print(observation.keys())
                observation['artifact'] = 0 #Normal by default, changed at regex match.

                if observation["data_type"] == 'auditd' or observation["data_type"] == 'Keypresses':
                    for regex in auditdList:
               
                        if re.search(regex, observation["data"]["content"]) != None:
                            #print("regex:%s found in observation:%s"% (regex, observation["data"]["content"])) #DEBUG
                            
                            observation['artifact'] = 1
                            count += 1
                            break  # stops to avoid re-adding field

                elif observation["data_type"] == 'network':
                    for regex in networkList:
                        if re.search(regex, str(observation["data"])) != None:
                            #print("regex:%s found in observation:%s"% (regex, observation["data"]))
                            
                            observation['artifact'] = 1
                            count += 1
                            break


        # print(json.dumps(relationshipList, sort_keys=True, indent=4)) #Debug, prints out entire json list in a pretty format
        return count

    # creates individual files for each relationship
    def createRelationshipFile(self, relationshipList,project_Name):
        # relationshipList[0], Each index is a relationship
        # relationshipList[0][0], each index is an observation
        # relationship[0][0]["fieldName"], each index is a key:value pair from the json.

        # print each relationship into relationships/relationship_x.json
        for i in range(len(relationshipList)):
            filename = "Project Data/"+project_Name +"/CE/Relationships/relationship_" + str(i + 1) + ".json"
            with open(filename, 'w') as json_file:
                json.dump(relationshipList[i], json_file, indent=4)

    # Formats the relationship output, used pretty much only for debugging.
    '''
    def outputRelationships(self, relationshipList):
        for i in range(len(relationshipList)):
            print("Relationship:%i----------------------------------------------------------" % (i + 1))
            # print(json.dumps(relationshipList[i], sort_keys=True, indent=4)) #Debug, prints out entire json list in a pretty format

            for j in range(len(relationshipList[i])):
                print(
                    "Timestamp:%s, Content:%s " % (relationshipList[i][j]["start"], relationshipList[i][j]['data']))
            print("\n\n\n")  # Make the output less harsh on the yees
    '''