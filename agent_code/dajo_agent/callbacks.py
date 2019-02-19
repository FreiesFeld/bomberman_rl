
import numpy as np
from random import shuffle
from time import time, sleep
from collections import deque

from settings import s
from settings import e


def setup(self):
    self.switch = True
    print(self.switch)


def act(self):
    # try to  go up and down all the time

    # testTimeout
    self.next_action = "BOMB"

    arena = self.game_state['arena']
    position = self.game_state['self']

    '''
    if(arena[position[0] - 1, position[1]] == 0 and position[0] - 1 >= 0): 
        self.next_action = "LEFT"
    else:
        #print(arena[position[0] - 1, position[1]], position[0] - 1)
        self.next_action = "DOWN"
    '''
    self.next_action = "UP"
    if(self.switch):
        self.next_action = "DOWN"
    self.switch = not self.switch
    print(self.switch)


def reward_update(self):
    print("da")
    print(self.shape)
    


def learn(self):
    pass
