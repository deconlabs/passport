import numpy as np
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

    def step(self, agents):
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
        actions = []
        n_reviewers = 0
        likes = []
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

        returns = self.get_return(likes, self.total_like, n_reviewers, self.args.mechanism)
        costs = [float(agent.get_cost()) for i, agent in enumerate(agents)]
        rewards = [ret - cost for ret, cost in zip(returns, costs)]

        for idx, agent in enumerate(agents):
            agent.learn(actions[idx], rewards[idx])

        """
        다음 에피소드를 위해 총 좋아요의 수를 초기화
        """
        self.total_like = 0

        """
        리뷰 작성의 비율
            -   에이전트 중 몇 명이 리뷰를 작성하였는가.
        """
        review_ratio = n_reviewers / len(agents)
        return [review_ratio, actions, returns, costs, rewards, likes]

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
