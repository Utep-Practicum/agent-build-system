from Builder.Relation import *

from Builder.Controller import *
from Runner.Eceld_Validate import *

import os
import time
from subprocess import Popen,PIPE
import platform

class RunnerManager:

    def __init__(self, controller):
        self.eceld_dir = os.path.dirname('/home/kali/eceld-netsys/eceld/')
        self.eceld_service_proc = Popen(['sudo', './eceld_service'],cwd=dir)
        self.controller = controller
        self.observation_list = self.controller.unified_list()
        self.Eceld_manager = EceldValidate(controller.project_name)
    

    def func_definer(self, observation):
        if observation.user_action and observation.data_type != "auditd":
        
            os.system("python3 Project\ Data/"+ self.controller.project_name +"/Runner/Scripts/user_action"+ str(observation.user_action_number) +".py")
            # execfile()
        elif observation.user_action == False:
            self.Eceld_manager.start_eceld(observation)
            print("\n\n\n\n\n\nObservation "+str(observation.observation_number)+" was found\n\n\n\n\n\n")


    def runner_review(self):
        for item in self.observation_list:
            self.func_definer(item)

        print("Done")


    def back_to_builder(self):
        self.eceld_service_proc.kill()
        if platform.system() == "Windows":
            Popen(['python', 'GUI_manager.py', 'builder', self.controller.project_name],stdout=PIPE, stderr=PIPE)
        else:
            Popen(['python3', 'GUI_manager.py', 'builder', self.controller.project_name],stdout=PIPE, stderr=PIPE)