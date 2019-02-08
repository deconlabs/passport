import numpy as np
import sys
import random
from mechanisms import mechanism_v1, mechanism_v2, mechanism_v3


class Env:
    def __init__(self, args):
        self.args = args

        self.n_agent = args.n_agent
        self.action_space = np.arange(0., args.range_endeavor)
        self.n_actions = len(self.action_space)
        self.reward_pool = args.reward_pool

        self.agent_assets = np.zeros(self.n_agent)
        self.review_history = [[0 for _ in range(self.args.window)] for _ in range(self.n_agent)]

    def step(self, actions):
        likes = self.get_like(actions)
        n_reviewers = sum([1 for act in actions if act != 0])
        returns = self.get_return(likes, sum(likes), n_reviewers, self.args.mechanism)
        costs = self.get_cost(actions)
        rewards = [ret - cost for ret, cost in zip(returns, costs)]
        review_ratio = n_reviewers / self.n_agent

        info = {
            # 'actions': actions,
            'review_ratio': review_ratio,
            'returns': returns,
            'costs': costs,
            'likes': likes
        }

        return None, rewards, True, info

    def get_like(self, actions):
        likes = []
        for idx, action in enumerate(actions):
            if action == 0:
                likes.append(0)

            else:
                # 0 or 1
                if self.args.review_history < 2:
                    # 범위: 0부터 최대 window=5 까지
                    score = sum(self.review_history[idx])
                    if self.args.review_history == 1:
                        if sum(self.review_history[idx]) == 0:
                            score = self.args.window + 1
                else:
                    score = self.args.window - sum(self.review_history[idx])

                coef1 = self.args.like_coef_1
                coef2 = self.args.like_coef_2 / (self.args.window + sys.float_info.epsilon)

                mu = coef1 * (action) + coef2 * score
                likes.append(max(0, random.gauss(mu, self.args.std_dev)))

        return likes

    def get_cost(self, actions):
        def real_endeavor(endeavor):
            real_endeavors = np.power(
                np.e, np.array(self.action_space) * np.log(len(self.action_space)) / (len(self.action_space) - 1)) - 1

            return real_endeavors[endeavor]

        costs = []
        for idx, action in enumerate(actions):
            if action == 0:
                costs.append(0.)

            else:
                b0 = self.args.b0
                b1 = self.args.b1 * self.args.n_agent
                b2 = self.args.b2
                b3 = self.args.b3 * self.args.n_agent

                cost =\
                    b0 +\
                    b1 * self.agent_assets[idx] +\
                    b2 * real_endeavor(action) +\
                    b3 * self.agent_assets[idx] * real_endeavor(action)

                costs.append(cost)

        return costs

    def get_return(self, likes, total_like, n_reviewers, mechanism):
        if mechanism == 'uniform':
            return mechanism_v1(self.reward_pool, likes, total_like, n_reviewers)

        elif mechanism == 'exponential':
            return mechanism_v2(self.reward_pool, likes, total_like, n_reviewers)

        elif mechanism == 'proportional':
            return mechanism_v3(self.reward_pool, likes, total_like, n_reviewers)

        else:
            raise NotImplementedError
