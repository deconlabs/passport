import numpy as np
import sys
from mechanisms import mechanism_v1,mechanism_v2,mechanism_v3

class Env:
    def __init__(self, args):
        self.action_space = np.arange(0., args.range_endeavor)
        self.n_actions = len(self.action_space)
        self.total_like = 0
        self.n_agent = args.n_agent
        self.reward_pool = args.reward_pool
        self.args=args

    def step(self, agents):
        actions = []
        n_reviewers = 0
        likes=[]
        for agent in agents:
            actions.append(agent.get_action())
            
            agent.my_like = agent.get_my_like()
            likes.append(agent.my_like)
            
            self.total_like += agent.my_like
            
            if agent.action >= 1:
                agent.review_history.append(1)
                n_reviewers += 1
            else:
                agent.review_history.append(0)

#after figuring self.total_like , again for loop 
        returns = self.get_return(likes, self.total_like, n_reviewers,self.args.mechanism)
        costs = [float(agent.get_cost()) for i, agent in enumerate(agents)]
        rewards = [ret - cost for ret, cost in zip(returns, costs)]
#        print("returns : ",returns)
#        print("costs : ", costs)
        for idx, agent in enumerate(agents):
            agent.learn(actions[idx], rewards[idx])

        self.total_like = 0

        review_ratio = n_reviewers/len(agents)
        return [review_ratio, actions, returns, costs, rewards]

    def get_return(self, likes, total_like, n_reviewers, mechanism):
        if mechanism == 'uniform':
            return mechanism_v1(self.reward_pool, likes, total_like, n_reviewers)
        elif mechanism == 'exponential':
            return mechanism_v2(self.reward_pool, likes, total_like, n_reviewers)
        
        elif mechanism == 'proportional':
            return mechanism_v3(self.reward_pool, likes, total_like, n_reviewers)
        
        else:
            raise NotImplementedError
        

    def update_cost(self, agents):
        for agent in agents:
            agent.get_cost()
