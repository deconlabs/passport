# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:47:27 2019
@author: user
"""
import numpy as np
import random
from collections import deque
import math


class Agent:
    def __init__(self, action_space, args):
        self.endeavor = action_space  # [0, 1, 2, ...]
        self.real_endeavor = list(pow(math.e, np.array([i/(len(self.endeavor)-1)*math.log(len(self.endeavor)) for i in range(len(self.endeavor))]))-1.)
        self.action = 0  # index: 0 or 1 or 2 or ...
        self.my_like = 0
        self.review_history = deque(maxlen=args.window)  # 1 or 0
        self.cost = args.cost
        self.asset = 0

        self.temperature = args.temperature
        self.learning_rate = args.lr
        self.tiny_value = args.tiny_value
        self.std_dev = args.std_dev

        self.args = args

        self.q_table = np.zeros_like(self.endeavor)
        self.beta_table = self.softmax(self.q_table)

    def get_my_like(self):
        """받는 좋아요 수: 노력(=빡침도), 그리고 과거 리뷰 개수(modified)에 정비례"""

        # 리뷰 점수
        score = sum(self.review_history)  # 범위: 0부터 최대 window=5 까지
        if sum(self.review_history) == 0:
            score = len(self.review_history) + 1  # 만일 리뷰를 하나도 쓰지 않다가 작성할 경우, 최대값 + 1

        # 정규분포를 취한 후 연속적인 범위가 나올 수 있도록
        coef1 = 2.
        coef2 = coef1 / (len(self.review_history) + self.tiny_value)  # coef1에 종속적
        mu = coef1 * (self.real_endeavor[self.action] + 1) + coef2 * score

        """
        정규분포:
        - 약 68%의 값들이 평균에서 양쪽으로 1 표준편차 범위(μ±σ)에 존재한다.
        - 약 95%의 값들이 평균에서 양쪽으로 2 표준편차 범위(μ±2σ)에 존재한다.
        - 거의 모든 값들(실제로는 99.7%)이 평균에서 양쪽으로 3표준편차 범위(μ±3σ)에 존재한다.
        """
        # 정규분포(0, 1) 적용 후 범위: 대략 0 ~ 25 예
        # 좋아요만 있기에, 음수는 있을 수 없으므로, 0으로 예외처리
        self.my_like = max(0, random.gauss(mu, self.std_dev))
        return self.my_like

    def softmax(self, x):
        """Compute softmax values for each sets of scores in x."""

        if not isinstance(x, np.ndarray):
            x = np.array(x)

        # temperature scaling
        x = x / self.temperature

        e_x = np.exp(x - np.max(x))  # prevent overflow
        return e_x / np.sum(e_x)

    def get_action(self, deterministic=False):
        if deterministic:
            # 만일 제일 큰 항목이 여러개라면 랜덤으로 선출
            b = np.array(self.beta_table)
            action = np.random.choice(np.flatnonzero(b == b.max()))
        else:
            # endeavor 중 하나를 베타테이블 확률에 따라
            action = np.random.choice(self.endeavor, 1, p=self.beta_table)

        action = int(action)
        self.action = action
        return action

    def get_cost(self):
        if self.action == 0:
            return 0.
        else:
            # asset과 endeavor에 의해 결정
            b0 = self.args.b0 / self.args.n_agent
            b1 = self.args.b1 / self.args.n_agent
            b2 = self.args.b2 / self.args.n_agent
            b3 = self.args.b3 / self.args.n_agent

            # self.real_endeavor[action]: 0에서 len(endeavor)-1 까지
            # reward = agent.my_like / total_like * self.reward_pool
            # rewards = [ret - cost for ret, cost in zip(returns, costs)]
            cost = b0 + b1*self.asset + b2*self.real_endeavor[self.action] + b3*self.asset*self.real_endeavor[self.action]

            # print(self.asset, self.real_endeavor[self.action], self.asset*self.real_endeavor[self.action])

            return cost

    def receive_token(self, amount_token):
        self.asset += amount_token

    def learn(self, action, reward):
        q1 = self.q_table[action]
        q2 = reward
        self.q_table[action] += self.learning_rate * (q2 - q1) / self.beta_table[action]  # 확률이 적었던 선택은 크게 업데이트 할 수 있도록
        self.beta_table = self.softmax(self.q_table)
