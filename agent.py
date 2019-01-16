# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:47:27 2019

@author: user
"""

class agent:
    def __init__(self):
#        self.action_space=
        self.endeavor= #action_space
        
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