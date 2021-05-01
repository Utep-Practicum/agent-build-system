from Runner.Collector import *
from Builder.Relation import *

from Builder.Controller import *

class RunnerManager:

    def __init__(self, controller):
        self.observation_list = controller.unified_list()
    

    def func_definer(self, observation):
        if observation.user_action:
            print('Call script')
        else:
            Collector(observation).tshark_collector()


    def runner_review(self):
        for item in self.observation_list:
            self.func_definer(item)