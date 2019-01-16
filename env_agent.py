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
reward_pool=100000
alpha=1
beta=1
gamma=1
n_people=15
std_dev=0.1
n_episode=300
n_timestep=50
tiny_value=0.05
total_asset=100000
explore_rate=0.3
cost=10000

class Env:
    def __init__(self):
        self.action_space = np.arange(0,10)
        self.n_actions = len(self.action_space)
        self.timestep = 0
        self.total_like=0

    def step(self, agents):
        
        actions = [agent.get_action(explore_rate) for agent in agents]
        
        for agent in agents:
            
            agent.my_like=beta*agent.action / pow((alpha*agent.review_history+tiny_value),gamma)
#            print(agent.my_like)
            self.total_like+=agent.my_like
#            print("like : " ,agent.my_like,self.total_like)
            
        rewards = [self.get_reward( agent,self.total_like) for agent in agents]
#        print(rewards)
        
        for idx, agent in enumerate(agents):   
            if agent.action>=1:agent.review_history+=1
            agent.receive_token(rewards[idx])
            agent.learn(actions[idx],rewards[idx],cost)
        
        self.total_like=0
        self.timestep += 1
    
    def get_reward(self,agent,total_like):        
        mu= agent.my_like/(self.total_like) * reward_pool
        reward=max(0,random.gauss(mu,std_dev))
#        print("reward=",reward)
        return reward
        
    def reset(self,agents):
        self.timestep=0
        distribute_asset(agents)


def distribute_asset(agents):
    n_agent=len(agents)    
#    random_numbers = np.random.random(n_agent)
#    # random samples of Rayleigh Dist. through the inverse transform
#    random_numbers_from_rayleigh =np.sqrt(-2*np.log(1-random_numbers)) #[inv_rayleigh_cdf(number) for number in random_numbers]
#    proportion=random_numbers_from_rayleigh/sum(random_numbers_from_rayleigh) #[num/sum(random_numbers_from_rayleigh) for num in random_numbers_from_rayleigh]
#    
    
    #np.random.pareto 분포를 쓰면 좋을듯
    probs=np.random.pareto(2,n_agent)
    for i in range(n_agent):
        agents[i].asset=probs[i]*total_asset

    

from agent import Agent

endeavor_list=[]
def run(env):
    global explore_rate
    for episode in range(n_episode):
        print("episode {} starts".format(episode))
        distribute_asset(agents)
        env.step(agents)
        endeavor_list.append([agent.get_action(explore_rate=0) for agent in agents])
        explore_rate*=0.9

if __name__ == '__main__':
    env = Env()
    agents = [Agent(action_space=env.action_space) for i in range(n_people)]
    run(env)
        

