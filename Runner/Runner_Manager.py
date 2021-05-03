from Runner.Collector import *
from Builder.Relation import *

from Builder.Controller import *

import os
import time

class RunnerManager:

    def __init__(self, controller):
        self.controller = controller
        self.controller.create_delta()
        self.observation_list = self.controller.unified_list()
    

    def func_definer(self, observation):
        if observation.user_action:
        
            # This conditions is to prevent running high delta times
            if float(observation.start) < 20:
                time.sleep(float(observation.start))
            os.system("python3 Project\ Data/"+ self.controller.project_name +"/Runner/Scripts/observation"+ str(observation.observation_number) +".py")
            # execfile()
        else:
            print("Test")
            # Temporary disabled
            # Collector(observation).tshark_collector()


    def runner_review(self):
        for item in self.observation_list:
            self.func_definer(item)