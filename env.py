import numpy as np
import random


class Env:
    def __init__(self, args):
        self.action_space = np.arange(0., args.range_endeavor)
        self.n_actions = len(self.action_space)
        self.total_like = 0

        self.n_agent = args.n_agent
        self.beta = args.beta
        self.alpha = args.alpha
        self.gamma = args.gamma
        self.tiny_value = args.tiny_value
        self.reward_pool = args.reward_pool
        self.std_dev = args.std_dev

    def step(self, agents):
        actions = [agent.get_action() for agent in agents]

        for agent in agents:
            agent.my_like = self.beta*agent.action / pow((self.alpha*agent.review_history+self.tiny_value), self.gamma)
            self.total_like += agent.my_like

        returns = [float(self.get_reward(agent, self.total_like)) for agent in agents]
        costs = [float(agent.get_cost(actions[i])) for i, agent in enumerate(agents)]
        rewards = [ret - cost for ret, cost in zip(returns, costs)]

        n_reviewers = 0
        for idx, agent in enumerate(agents):
            if agent.action >= 1:
                agent.review_history += 1
                n_reviewers += 1
            agent.learn(actions[idx], rewards[idx])

        self.total_like = 0

        review_ratio = n_reviewers/len(agents)
        return review_ratio, actions

    def get_reward(self, agent, total_like):
        mu = agent.my_like/(self.total_like) * self.reward_pool
        reward = max(0, random.gauss(mu, self.std_dev))
        return reward

    def update_cost(self, agents):
        for agent in agents:
            agent.get_cost()
