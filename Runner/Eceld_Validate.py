import threading
import time
import os
import json

from subprocess import Popen,PIPE,TimeoutExpired

traffic_found = False
dir = os.path.dirname('/home/kali/eceld-netsys/eceld/')

class EceldValidate:

    def __init__(self, project_name):
        self.proc = None
        self.project_name = project_name
        self.stop_eceld = False
        


    def start_eceld(self,observation):
        # time.sleep(15)
        self.compare_thread = threading.Thread(target=self.validate,args=(observation,),daemon=True)
        self.compare_thread.start()
        counter = 0
        while not self.stop_eceld:
            self.proc = Popen(['sudo','python3', 'test_engine_invoke.py'], cwd=dir)
            print('Waiting 10 sec for ECELd to complete')
            try:
                outs, errs = self.proc.communicate(timeout=12)
            except TimeoutExpired:
                self.proc.kill()
                outs, errs = self.proc.communicate()
                file_src = dir+'/plugins/collectors/tshark/parsed/networkDataAll.JSON'
                if 'networkDataAll.JSON' in os.listdir(dir+'/plugins/collectors/tshark/parsed/'):
                    file_dst = '/home/kali/Desktop/Practicum/agent-build-system/Project Data/'+self.project_name+'/Runner/Eceld/temp/comp'+str(counter)+'.json'
                    Popen(['sudo','cp',file_src,file_dst], cwd='/')
                counter += 1
                if counter > 10:
                    break



    def validate(self, observation):
        # Eceld files will be saved in "Project Data/Runner/Eceld/temp"
        #traffic_found = bool(input('Has the packet been found'))
        #observation.select_filters = ['ip.src']
        print(observation.select_filters)
        # 1) Create directory where files are going to be stored
        if not os.path.exists("Project Data/"+self.project_name+"/Runner/Eceld/temp"):
            os.makedirs("Project Data/"+self.project_name+"/Runner/Eceld/temp")
            

        # 2) get the list of files of the folder we created, if this is empty wait 5 seconds
        times_waited = 0
        while True:
            fileList = os.listdir("Project Data/"+self.project_name+"/Runner/Eceld/temp")
            if len(fileList) == 0:
                time.sleep(5)
                times_waited += 1
                if times_waited == 5:
                    for f in os.listdir("Project Data/"+self.project_name+"/Runner/Eceld/temp"):
                        os.remove(os.path.join("Project Data/"+self.project_name+"/Runner/Eceld/temp", f))
                    self.stop_eceld = True
                    return False
            else:  # Files are on the folder
                file_name = fileList.pop()  # Get the file name and remove it from the list
        # 3) Read the json file from file_name
                with open("Project Data/" + self.project_name + "/Runner/Eceld/temp/" + file_name,
                          'r') as load_file:
                    sally = json.load(load_file)
                if len(sally) == 0:
                    continue
                # Format the data of the json file
                for row in sally:
                    netDataRaw = row["title"]
                    networkList = netDataRaw.split("\n")[:-1] # split by "\n" and remove the last one because is empty
                    network_dict = {}  # Here I'll store the values to compare it with the observation
                    for values in networkList:

                        tisco = values.split("  ")  # divide in two, because it has two spaces "eth:ethertype:ip:tcp  "
                        netInfo = tisco[1]  # the string that we care [eth:ethertype:ip:tcp, THIS ONE I CARE]
                        netInfoList = netInfo.split(" ")
                        lastValue = netInfoList[-1]
                        if lastValue[1] == "x":
                            netInfoList = netInfoList[:-1]  # Remove the 0x000000 that Bebe said we don't need
                        # fill the dictionary ------------------------------------
                        
                        if len(netInfoList) >= 1:
                            network_dict['eth.src'] = netInfoList[0]
                        if len(netInfoList) >= 2:
                            network_dict['eth.dst'] = netInfoList[1]
                        if len(netInfoList) >= 3:
                            network_dict['ip.src'] = netInfoList[2]
                        if len(netInfoList) >= 4:
                            network_dict['ip.dst'] = netInfoList[3]
                        if len(netInfoList) >= 5:
                            network_dict['tcp.srcport'] = netInfoList[4]
                        if len(netInfoList) >= 6:
                            network_dict['tcp.dstport'] = netInfoList[5]
            
                        # Compare based on the filters chosen
                        for item in observation.select_filters:
                            if observation.data[item] == network_dict[item]:
                                print("\n\n\n\n\nMatch Found" + item + ': ' + str(observation.data[item]) + '\n\n\n\n')
                                self.stop_eceld = True
                                return True
                            break
                os.remove(os.path.join("Project Data/"+self.project_name+"/Runner/Eceld/temp", file_name))

