# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:47:27 2019
@author: user
"""
import numpy as np
import random


class Agent:
    def __init__(self, action_space, args):
        self.endeavor = action_space  # action_space
        self.action = 0
        self.my_like = 0
        self.review_history = [0 for _ in range(args.window)]  # 1 -> write 0 -> no review
        self.cost = args.cost
        self.asset_coef = args.asset_coef
        self.learning_rate = args.lr
        self.temperature = args.temperature
        self.q_table = np.zeros_like(self.endeavor)
        self.beta_table = self.softmax(self.q_table)
        self.mu_table = [10 + 1 * i for i in self.endeavor]

        self.asset = 0  # 분배방식을 변경하며 분배해보자
        self.beta = args.beta
        self.alpha = args.alpha
        self.gamma = args.gamma
        self.tiny_value = args.tiny_value
        self.std_dev = args.std_dev

    def get_my_like(self):
        score = sum(self.review_history)
        if sum(self.review_history) == 0:
            score = len(self.review_history) + 1
#        mu = self.beta*self.action / pow((self.alpha*score+self.tiny_value), self.gamma) 
        mu = self.mu_table[self.action] + score / 10.
        
        self.my_like=max(0,random.gauss(mu,self.std_dev))
        return self.my_like
    

        
    def softmax(self, x):
        """Compute softmax values for each sets of scores in x."""
        if not isinstance(x, np.ndarray):
            x = np.array(x)

        # temperature scaling
        x = x / self.temperature

        e_x = np.exp(x - np.max(x))
        return e_x / np.sum(e_x)

    def get_action(self, deterministic=False):
        if deterministic:
            action = np.argmax(self.beta_table)
        else:
            action = np.random.choice(self.endeavor, 1, p=self.beta_table)
            action = int(action)
        self.action = action
        return action

    def get_cost(self, action):
        cost = self.cost + self.asset_coef * self.asset + (action - 4.5)
        return cost

    def receive_token(self, amount_token):
        self.asset += amount_token

    def learn(self, action, reward):
        q1 = self.q_table[action]
        q2 = reward
        self.q_table[action] += self.learning_rate * (q2 - q1) / self.beta_table[action]
        self.beta_table = self.softmax(self.q_table)
