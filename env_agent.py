# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:17:54 2019

@author: user
"""

import argparse
import numpy as np
#from scipy import stats
import random

parser=argparse

reward_pool=1000000
alpha=1
beta=1
gamma=1
n_people=15
std_dev=0.1

class env:
    def __init__(self):
        self.action_space = np.arange(0,1,0.1)
        self.n_actions = len(self.action_space)
        self.timestep = 0
        self.total_like=0

    def step(self, agents):
        
        actions = [agent.get_action() for agent in agents]
        
        for agent in agents:
            agent.my_like=beta*agent.endeavor / pow((alpha*sum(agent.review_history)),gamma)
            self.total_like+=agent.my_like
            
        rewards = [self.get_reward( agent,self.total_like) for agent in agents]
        
        for idx, agent in enumerate(agents):   
            agent.receive_token(rewards[idx])
            agent.learn(action_space)
        
        self.total_like=0
        self.timestep += 1
    
    def get_reward(self,agent,total_like):        
        mu= agent.my_like/self.total_like * reward_pool
        return random.gauss(mu,std_dev)
        
    def reset(self):
        self.timestep=0


def distribute_asset(total_asset,agents,method):
    n_agent=len(agents)
    

import math
import random

def inv_rayleigh_cdf(u):
    return math.sqrt(-2 * math.log(1 - u))

# random samples from Unif(0, 1)
for i in range(5):
    random_numbers = [random.random() for _ in range(10000)]
    # random samples of Rayleigh Dist. through the inverse transform
    random_numbers_from_rayleigh = [inv_rayleigh_cdf(number) for number in random_numbers]
    proportion=[num/sum(random_numbers_from_rayleigh) for num in random_numbers]
    print(sum(proportion))
    print(sum(np.round(np.array(proportion)*reward_pool)))
            
import matplotlib.pyplot as plt
plt.hist(random_numbers_from_rayleigh)



        
        

