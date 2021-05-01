import sys
import os
import json

# This uses a json file that converts the labels into filter syntax
filter_def = None
with open('Runner/filter_settings.json') as f:
    filter_def = json.load(f)[0]

class Collector:

    def __init__(self, observation):
        self.observation = observation
        self.running = True

    def tshark_collector(self):
        count = 0
        while count < 1:
            file_name = 'pcap_' + str(count) + '.pcap'
            filter_str = self.traffic_filter()
            cmd = 'tshark -c 1 -w Runner/tshark/{0} -f \"{1}\"'.format(file_name, filter_str)
            print(cmd)
            os.system(cmd)
            count += 1


    def traffic_filter(self):
        global filter_def
        filter = ''
        counter = 0

        # This line is to test the filter function
        # Remove before final integration
        #############################################
        self.observation.data['ip.src'] = '10.0.2.15'
        #############################################

        for item in self.observation.select_filters:       
            if counter == 0:
                filter += ' ' + filter_def[item] + ' ' + self.observation.data[item]
            else:
                filter += ' && ' + filter_def[item] + ' ' + self.observation.data[item]
            counter += 1
        
        return filter


    def file_cleanup(self,file_name):
        if os.path.exists(file_name):
            os.sytem(file_name)
        else:
            print('File does not exist')


if __name__ == '__main__':

    select_filters = {'ip.src':'src net', 'ip.len':'len <= '}
    observation = {'ip.src':'10.0.2.15','ip.len':'200'}

    Collector(observation).tshark_collector()