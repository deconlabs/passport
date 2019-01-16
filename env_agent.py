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
            agent.learn(actions[idx],rewards[idx])
        
        self.total_like=0
        self.timestep += 1
    
    def get_reward(self,agent,total_like):        
        mu= agent.my_like/self.total_like * reward_pool
        return random.gauss(mu,std_dev)
        
    def reset(self,agents):
        self.timestep=0
        distribute_asset(agents)


def distribute_asset(agents):
    n_agent=len(agents)    
    random_numbers = np.random.random(n_agent)
    # random samples of Rayleigh Dist. through the inverse transform
    random_numbers_from_rayleigh =np.sqrt(-2*np.log(1-random_numbers)) #[inv_rayleigh_cdf(number) for number in random_numbers]
    proportion=random_numbers_from_rayleigh/sum(random_numbers_from_rayleigh) #[num/sum(random_numbers_from_rayleigh) for num in random_numbers_from_rayleigh]
    
    for i in range(n_agent):
        agents[i].asset=proportion[i]*reward_pool
        



        
        

