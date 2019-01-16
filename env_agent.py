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
        pass
    
    
    def step(self,agents):
        
        def __init__(self, C, objectivity, forgiveness, mechanism):
        self.C = C
        self.objectivity = objectivity
        self.forgiveness = forgiveness
        self.mechanism = mechanism
        self.action_space = [RANDOM, RESEARCH]
        self.n_actions = len(self.action_space)
        self.timestep = 0
        self.data_list = []

    def step(self, agents):
        
        prev_tokens = [agent.total_tokens for agent in agents]

        actions = [agent.get_action() for agent in agents]
#        votes = self.get_vote(actions, self.objectivity)

#        tokens, token_true, token_false = self.get_token(agents, votes) #리스크 성향에 따라 토큰 검
#        result = self.get_result(token_true, token_false)

        rewards = self.get_reward(self.mechanism, agents, token_true, token_false,
                                  actions, votes, tokens, prev_tokens, result, self.C)

        for idx, agent in enumerate(agents):
            if agent not in agents:
                agent.receive_token(0.)

        for idx, agent in enumerate(agents):
            agent.learn(actions[idx], rewards[idx])
        
        self._save_data(agents, agents, votes, actions, tokens, prev_tokens,
                       result, token_true, token_false, rewards)
        self.timestep += 1
    
    def get_reward(self,agent,total_like):
        
        my_like=beta*agent.endeavor / pow((alpha*sum(agent.review_history)),gamma)   
        mu= my_like/total_like * reward_pool
        
        return random.gauss(mu,std_dev)
        

    def get_vote(self, actions, prob):
        votes = []
        for action in actions:
            if action == RESEARCH:
                v = self.decide(prob)
            else:
                v = self.decide(0.5)
            votes.append(v)
        return votes

    def get_token(self, agents, votes):
        token_true = 0.
        token_false = 0.
        tokens = []

        weights = np.array([agent.tokens for agent in agents])
        weights = weights / np.sum(weights)

        for idx, vote in enumerate(votes):
            rate = self.decide_rate(agents[idx].risk_aversion, weights[idx])
            token = agents[idx].tokens * rate
            tokens.append(token)
            agents[idx].tokens -= token
            if vote:
                token_true += token
            else:
                token_false += token
        return tokens, token_true, token_false

    def get_result(self, token_true, token_false):
        true_ratio = token_true / (token_true + token_false)
        if true_ratio > 0.5:
            result = True
        elif true_ratio < 0.5:
            result = False
        else:
            result = self.decide(0.5)
        return result

#    def decide(self, prob):
#        if np.random.random() < prob:
#            return True
#        else:
#            return False

    def decide_rate(self, risk_aversion, weight):
        # TODO(Aiden): 개선시킬 필요 있음
        risk_aversion = risk_aversion + (np.random.randn() * 0.1)
        risk_aversion = min(risk_aversion, 0.99)
        risk_aversion = max(risk_aversion, 0.01)
        return 1 - risk_aversion




def distribute_asset(total_asset,method):
    pass

class agent:
    def __init__(self):
#        self.action_space=
        self.endeavor=list(range(0,1,0.1)) #action_space
        
        #self.seriousness=None
        self.review_history=[] # 1 -> write 0 -> no review 
    
        
        self.value_table=np.zeros_like(self.endeavor)
        def softmax(x):
            return np.exp(x) / np.sum(np.exp(x), axis=0)
        self.beta_table=softmax(self.value_table)
        
        self.asset= distribute_asset() #분배방식을 변경하며 분배해보자
        

    
    def update_value(self):



    def get_action(self):
        action = np.random.choice(self.endeavor, p=self.beta_table)
        return action
        
        

