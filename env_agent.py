# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:17:54 2019

@author: user
"""

import argparse
import numpy as np
#from scipy import stats
import random
from tensorboardX import SummaryWriter
from collections import Counter

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
range_endeavor=10


class Env:
    def __init__(self):
        self.action_space = np.arange(0,range_endeavor)
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
        
        n_reviewers=0
        for idx, agent in enumerate(agents):   
            if agent.action>=1:
                agent.review_history+=1
                n_reviewers+=1
#            agent.receive_token(rewards[idx])
            agent.learn(actions[idx],rewards[idx],cost)
        
        self.total_like=0
        self.timestep += 1
        
        review_ratio= n_reviewers/len(agents)
        return review_ratio,actions
    
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
    #np.random.pareto 분포를 쓰면 좋을듯
    probs=np.random.pareto(2,n_agent)
    for i in range(n_agent):
        agents[i].asset=probs[i]*total_asset

    

from agent import Agent

endeavor_list=[]
final_list=[{} for _ in range(range_endeavor)]

def run(env):
    global explore_rate
    for episode in range(n_episode+1):
        print("episode {} starts".format(episode))
        distribute_asset(agents)
        review_ratio,actions=env.step(agents)
        
        endeavor_list.append([agent.get_action(explore_rate=0) for agent in agents])
        explore_rate*=0.9
        
        #visualisation
        writer.add_scalar("data/review_ratio",review_ratio,episode)
        
        for idx,agent in enumerate(agents):
            data_beta_table=dict( (str(i),v) for i,v in enumerate(agent.beta_table ))
            writer.add_scalars("data/{}".format(idx),data_beta_table,episode)
            
        if episode%100==0:
            counter=Counter(actions)
            for act in range(range_endeavor): 
                final_list[act][str(episode)]=counter[act]
    print(final_list)
            
    for i in range(range_endeavor):
        writer.add_scalars("data/endeavor",final_list[i],i)

if __name__ == '__main__':
    writer=SummaryWriter()
    env = Env()
    agents = [Agent(action_space=env.action_space) for i in range(n_people)]
    run(env)
    print(endeavor_list)
    writer.close()
        

