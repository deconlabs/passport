# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:47:27 2019

@author: user
"""
import numpy as np
alpha_=.1

class Agent:
    def __init__(self,action_space):
#        self.action_space=
        self.endeavor= action_space #action_space
        self.action=0
        self.my_like=0
        #self.seriousness=None
        self.review_history=0 # 1 -> write 0 -> no review 
    
        self.learning_rate=0.1
        self.q_table=np.zeros_like(self.endeavor)
        
        self.beta_table=self.softmax(self.q_table)
        
        self.asset=0 #분배방식을 변경하며 분배해보자
        
        self.cost=alpha_*self.asset*self.action
    
    def softmax(self,x):
            x=np.clip(x,-10,10)
            return np.exp(x) / np.sum(np.exp(x), axis=0)
        
    def get_action(self,explore_rate):
        tmp=np.random.random()
        if tmp<explore_rate:
             action = np.random.choice(self.endeavor)
#             return action
        else:
            action = np.argmax(self.beta_table)
#            return action
        self.action=action
        return action

    def get_cost(self):
        self.cost=alpha_*self.asset*self.action
        
    def receive_token(self,amount_token):
        self.asset+=amount_token
        
    def learn(self, action, reward):
        q1 = self.q_table[action]
        q2 = reward-self.cost
        self.q_table[action] += self.learning_rate * (q2 - q1) 
        self.beta_table = self.softmax(self.q_table)
    
        