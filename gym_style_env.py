import numpy as np
import sys
import random
from mechanisms import mechanism_v1, mechanism_v2, mechanism_v3


class Env:
    def __init__(self, args):
        """
        *   n_agent: 참여하는 에이전트의 수

        *   action_space: 에이전트가 가질 수 있는 행동의 모음

        *   n_actions: 에이전트가 취할 수 있는 액션의 수

        *   total_like: 현재 총 좋아요의 누계

        *   reward_pool: 보상으로 줄 총 액수, 이를 리뷰어들이 나누어 가진다.
        """
        self.args = args
        self.n_agent = args.n_agent
        self.action_space = np.arange(0., args.range_endeavor)
        self.n_actions = len(self.action_space)
        self.total_like = 0.
        self.reward_pool = args.reward_pool
        self.agent_assets = np.zeros(self.n_agent)
        self.review_history = [
            [0 for _ in range(self.args.window)] for _ in range(self.n_agent)]

    def step(self, actions):
        """
        실제 리뷰 작성 여하 및 얼마나 노력할 지를 결정하는 부분

        *   에이전트의 액션을 결정하고
        *   그 행동에 따른 에이전트가 작성한 리뷰의 좋아요 갯수가 결정되고
        *   이득(return)과 비용(cost)과 보상(reward)가 계산되고
            -   return: 실제 리뷰 작성을 통해 reward_pool로부터 나누어 받은 보상
            -   cost: 내가 본 리뷰를 작성함에 소요된 비용
            -   reward: return - cost
        *   이를 바탕으로 에이전트는 행동을 학습한다.
        """

        likes = self.get_like(actions)
        n_reviewers = sum([1 for act in actions if act != 0])
        returns = self.get_return(likes, sum(
            likes), n_reviewers, self.args.mechanism)
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
                coef2 = self.args.like_coef_2 / \
                    (self.args.window + sys.float_info.epsilon)
                mu = coef1 * (action) + coef2 * score
                likes.append(max(0, random.gauss(mu, self.args.std_dev)))
        return likes

    def get_cost(self, actions):
        def real_endeavor(endeavor):
            real_endeavor =\
                np.power(np.e, np.array(self.action_space) *
                         np.log(len(self.action_space)) / (len(self.action_space) - 1)) - 1
            return real_endeavor[endeavor]

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
                    b3 * self.agent_assets[idx] * \
                    real_endeavor(action)
                costs.append(cost)
                # print(self.asset, self.real_endeavor[self.action], self.asset*self.real_endeavor[self.action])

        return costs

    def get_return(self, likes, total_like, n_reviewers, mechanism):
        """
        :param likes: 내 글의 좋아요 수
        :param total_like: 모든 리뷰의 좋아요 수의 누계
        :param n_reviewers: 리뷰를 작성한 사람의 수
        :param mechanism: 어떤 방법으로 이득을 산출할 것인가.
        :return: 없음.
        """
        if mechanism == 'uniform':
            return mechanism_v1(self.reward_pool, likes, total_like, n_reviewers)

        elif mechanism == 'exponential':
            return mechanism_v2(self.reward_pool, likes, total_like, n_reviewers)

        elif mechanism == 'proportional':
            return mechanism_v3(self.reward_pool, likes, total_like, n_reviewers)

        else:
            raise NotImplementedError
