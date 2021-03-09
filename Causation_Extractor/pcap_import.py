import json
import time

#Create list dictionary to store all packets
#frames = {}
frames = []
frame_info = {}

#frame,eth,ip,tcp

def DFS_mapping(node):
    global frame_info

    for item in node:
        if type(node[item]) == dict:
            DFS_mapping(node[item])
        else:
            frame_info[item] = node[item]


def json_formatting(filename):
    try:
        #Open file in read mode
        f = open(filename,'r')
        data = json.load(f)
        f.close()

        global frames
        global frame_info

        outfile = open('test.json','w')

        #Reformat every packet in the json file
        for item in data:
            DFS_mapping(item)
            #key = str(frame_info['frame.number'])
            #frames.append(frame_info)
            #print(frame_info)
            json.dump(frame_info, outfile, indent=4)
            frame_info.clear()

        outfile.close()
    except:
        print('Input file not found')
'''
    #Export formatted data into a new json file
    try:
        with open('test.json','w') as outfile:
            json.dump(frames, outfile, indent=4)
    except:
        print("Error encountered while creating output file")
'''

def main():
    #Start timer for the program
    tic = time.perf_counter()

    #Name of pcap file in json format
    #fileName = '/home/kali/eceld-netsys/ProjectData/timeTest/PCAP/timeTest.json'
    fileName = '/home/kali/Downloads/LargeTest1.json'

    json_formatting(fileName)

    #End timer for the program
    toc = time.perf_counter()

    #Calculate time elapsed
    total = toc - tic
    print(f'Runtime {total:0.4f}')
    
    
if __name__ == '__main__':
    main()