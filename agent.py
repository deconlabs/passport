# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:47:27 2019

@author: user
"""
import numpy as np

class agent:
    def __init__(self,actions):
#        self.action_space=
        self.endeavor= actions#action_space
        self.my_like=0
        #self.seriousness=None
        self.review_history=[] # 1 -> write 0 -> no review 
    
        self.learning_rate=0.1
        self.q_table=np.zeros_like(self.endeavor)
        def softmax(x):
            return np.exp(x) / np.sum(np.exp(x), axis=0)
        self.beta_table=softmax(self.q_table)
        
        self.asset=0 #분배방식을 변경하며 분배해보자
        
    def get_action(self):
        action = np.random.choice(self.endeavor, p=self.beta_table)
        return action
    
    def receive_token(self,amount_token):
        self.asset+=amount_token
        
    def learn(self, action, reward):
        q1 = self.q_table[action]
        q2 = reward
        self.q_table[action] += self.learning_rate * \
            (q2 - q1) / self.beta_table[action]
        self.beta_table = self.softmax(self.q_table)
    
        