from Runner.Collector import *
from Builder.Relation import *

from Builder.Controller import *

import os
import time
from subprocess import Popen,PIPE
import platform

class RunnerManager:

    def __init__(self, controller):
        self.controller = controller
        self.observation_list = self.controller.unified_list()
    

    def func_definer(self, observation):
        if observation.user_action and observation.data_type != "auditd":
        
            # This conditions is to prevent running high delta times
            if float(observation.start) < 20:
                time.sleep(float(observation.start))
            os.system("python3 Project\ Data/"+ self.controller.project_name +"/Runner/Scripts/user_action"+ str(observation.user_action_number) +".py")
            # execfile()
        elif observation.user_action == False:
            print("Test")
            Collector(observation).tshark_collector()


    def runner_review(self):
        for item in self.observation_list:
            self.func_definer(item)


    def back_to_builder(self):
        if platform.system() == "Windows":
            Popen(['python', 'GUI_manager.py', 'builder', self.controller.project_name],stdout=PIPE, stderr=PIPE)
        else:
            Popen(['python3', 'GUI_manager.py', 'builder', self.controller.project_name],stdout=PIPE, stderr=PIPE)