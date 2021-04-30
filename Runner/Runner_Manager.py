from Runner.Collector import *
from Builder.Relation import *

from Builder.Controller import *

class RunnerManager:

    def __init__(self, observations):
        self.observation_list = observations
    

    def definer(self, observation):
        if observation.user_action:
            print('Call script')
        else:
            Collector(observation).tshark_collector()