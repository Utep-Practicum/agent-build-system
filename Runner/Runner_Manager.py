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
            # Still need to add delta time to run script

            # if int(observation.start) > 20:
            #     time.sleep(int(observation.start))
            os.system("python3 Project\ Data/"+ self.controller.project_name +"/Builder/Dependencies/observation"+ str(observation.observation_number) +".py")
            # execfile()
        else:
            print("Test")
            # Collector(observation).tshark_collector()


    def runner_review(self):
        for item in self.observation_list:
            self.func_definer(item)