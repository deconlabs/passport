import numpy as np
import random
from collections import deque
import sys


class Agent:
    def __init__(self, action_space, args):
        """
        *   endeavor: 리뷰를 쓰는 노력의 정도, 0부터 1씩 증가하는 정수의 값을 가짐. (n까지)
            -   0의 경우: 리뷰를 쓰지 않음
            -   k > 0인 정수: 수치가 높을수록 리뷰 작성에 들어간 노력이 큼.

        *   real_endeavor: 노력을 실제 계산(cost 함수 등)에 반영할 때, 정수 값을 그대로 반영하는 것이 아니라 가공하여 적용
            -   시작점이 0, 끝 점이 n임은 동일하나,
            -   본래 선형적으로 증가하던 endeavor와는 달리
            -   지수적으로 증가함.

        *   action: 에이전트의 행동
            -   리뷰를 얼마나 열심히 쓰는지를 수치로 표현
            -   0부터 n까지의 정수, endeavor와 동일하게 햬석 가능

        *   my_like: 내가 작성한 글이 얼마나 좋아요를 많이 받았는가
            -   한 에피소드에 글은 하나만 작성한다고 가정
            -   글을 쓰지 않았을 경우 받을 수 있는 좋아요는 당연히 0

        *   review_history: 최근의 r 에피소드에서 얼마나 리뷰를 작성했었는가
            -   과거 에피소드의 리뷰 작성 여부가 현재 에이전트가 받는 좋아요 등에 영향을 끼칠 수 있음.
            -   리뷰를 작성했을 경우 1, 아닐 경우 0으로 기록
            -   최근 r 에피소드를 기록, r은 args.window에서 설정 default: 5

        *   cost: 리뷰를 작성하는데 들어가는 비용
            -   초기 cost 값이 필요할 경우, args.cost로 부여 가능 default: 5.0

        *   asset: 초기 할당받는 자산
            -   비율로 할당됨.
        """
        self.args = args

        self.endeavor = action_space  # [0, 1, 2, ...]
        self.real_endeavor =\
            np.power(np.e, np.array(self.endeavor) * np.log(len(self.endeavor)) / (len(self.endeavor) - 1)) - 1
        self.action = 0  # index: 0 or 1 or 2 or ...
        self.my_like = 0.
        self.review_history = deque(maxlen=args.window)  # 1 or 0
        self.cost = 0.
        self.asset = 0.

        self.q_table = np.zeros_like(self.endeavor)
        self.beta_table = self.softmax(self.q_table)

    def get_my_like(self):
        """
        리뷰를 쓰지 않았을 경우 my_like는 0
        """
        if self.action == 0:
            return 0

        """
        받는 좋아요 수는 노력, 그리고 과거 리뷰 개수(modified)에 영향을 받는다.

        *   과거 리뷰 작성 개수
            -   과거에 리뷰를 더 많이 쓸 수록 받는 좋아요가 많음
                -   네임드
                -   리뷰 작성의 경험이 풍부하면 더 좋은 리뷰를 작성할 가능성이 크다?
                -   더 많은 호텔을 경험했으면 보다 객관적일 것이라는 판단.
            -   (현재 주석처리됨: 미사용)과거에 리뷰를 작성하지 않다가 갑자기 작성했을 경우에 대한 판단
                -   리뷰를 안쓰던 사람이 썼을 정도이니까
                    -   완전히 좋거나
                    -   완전히 나쁘거나 할 것이다
                -   리뷰에 대한 신뢰도 UP -> 좋아요 많이 받음

        *   노력
            -   action으로 적용
            -   endeavor나 real_endeavor로 적용하지 않는 이유
                -   노력 여하가 아닌
                -   실제 행동한 action에 따라 좋아요를 받아야 하기 때문
        """
        score = sum(self.review_history)  # 범위: 0부터 최대 window=5 까지

        # 만일 리뷰를 하나도 쓰지 않다가 작성할 경우, 최대값 + 1
        # if sum(self.review_history) == 0: score = len(self.review_history) + 1

        """
        *   tiny_value를 더하여 0으로 나누는 경우를 방지

        *   정규분포를 활용하여 받는 좋아요의 수치에 확률적인 요소를 추가함

        *   현재의 action에 가장 큰 영향을 받도록 하였으며
        *   과거 리뷰 이력은 최대 액션에서 1 만큼의 차이만 나도록 함.
            -   과거 리뷰 이력보다 현재의 액션이 더 중요함
            -   과거 리뷰가 액션의 1 차이(0과 1, 1과 2와 같은 차이...) 이상의 영향을 주지는 않음.

        *   default: like_coef=1.0
            -   본 값이 클 수록 받는 좋아요의 차이가 크게 차이나게 됨.
            -   물론 확률적으로 받으므로 무조건적으로 크게 받는 것은 아니며, 크게 받을 확률이 커지는 것.
        """
        coef1 = self.args.like_coef_1
        coef2 = self.args.like_coef_2
        mu = coef1 * (self.action) + coef2 / (len(self.review_history) + sys.float_info.epsilon) * score

        """
        *   좋아요만 있기에, 음수는 있을 수 없으므로, 0으로 예외처리

        *   default: std_dev=1.0

        정규분포:
        - 약 68%의 값들이 평균에서 양쪽으로 1 표준편차 범위(μ±σ)에 존재한다.
        - 약 95%의 값들이 평균에서 양쪽으로 2 표준편차 범위(μ±2σ)에 존재한다.
        - 거의 모든 값들(실제로는 99.7%)이 평균에서 양쪽으로 3표준편차 범위(μ±3σ)에 존재한다.
        """
        self.my_like = max(0, random.gauss(mu, self.args.std_dev))
        return self.my_like

    def softmax(self, x):
        """
        Compute softmax values for each sets of scores in x.
        """

        if not isinstance(x, np.ndarray):
            x = np.array(x)

        # temperature scaling
        x = x / self.args.temperature

        # prevent overflow
        e_x = np.exp(x - np.max(x))

        return e_x / np.sum(e_x)

    def get_action(self, deterministic=False):
        """
        :param deterministic: True일 경우 결정론적으로 가장 높은 확률을 가진 action이 선출됨. 아닐 경우 확률적으로 결정.
        :return: 에이전트의 액션.
        """
        if deterministic:
            """
            만일 제일 큰 항목이 여러개라면 그 중에서 랜덤으로 선출
            """
            b = np.array(self.beta_table)
            action = np.random.choice(np.flatnonzero(b == b.max()))

        else:
            """
            endeavor 중 하나를 베타테이블 확률에 따라
            """
            action = np.random.choice(self.endeavor, 1, p=self.beta_table)

        """
        action은 정수 값을 가짐: 0 ~ n
        """
        action = int(action)
        self.action = action
        return action

    def get_cost(self):
        """
        만일 노력을 하지 않았을 경우(글을 작성하지 않은 경우) 들어가는 비용은 0
        """

        """
        노력을 했을 경우

        *   글 작성에 소요되는 비용은 asset과 endeavor에 의해 결정된다.
            -   자산이 많은 사람은 굳이 마일리지를 받기 위해 리뷰를 작성할 노고를 들일 필요가 없다.
            -   노력을 많이 들일 경우 당연히 글 작성에 들어가는 비용도 커진다.
            -   두 항목이 선형적으로 결합되는 것이 아닌 곱셈항을 넣음으로써 보다 잘 모델링 할 수 있음
                -   만일 계수 b3가 0이면 선형적인 결함임: default=0.1
            -   절대적으로 들어가는 노력은 계수 b0으로 줄 수 있음: default=0.0

            -   노력은 endeavor가 아닌 real_endeavor로 적용한다.
                -   실제 들어가는 노력은 선형적으로 증가하는 것이 아니라 지수적으로 증가함을 가정.

        *   asset은 자산 분배의 비율이므로
            -   에이전트의 수로 나눠 줄 필요가 없으며,
            -   들어가는 cost의 계산을 위해서는 오히려 에이전트의 수를 곱해줘야 하지 않을까? <- 논의 필요
        """

        if self.action == 0:
            return 0.

        else:
            # asset과 endeavor에 의해 결정
            """
            *   asset은 비율이므로 에이전트의 수를 곱하여 정규화
            """
            b0 = self.args.b0
            b1 = self.args.b1 * self.args.n_agent
            b2 = self.args.b2
            b3 = self.args.b3 * self.args.n_agent

            # self.real_endeavor[action]: 0에서 len(endeavor)-1 까지
            # reward = agent.my_like / total_like * self.reward_pool
            # rewards = [ret - cost for ret, cost in zip(returns, costs)]
            cost =\
                b0 +\
                b1 * self.asset +\
                b2 * self.real_endeavor[self.action] +\
                b3 * self.asset * self.real_endeavor[self.action]

            # print(self.asset, self.real_endeavor[self.action], self.asset*self.real_endeavor[self.action])

            return cost

    def receive_token(self, amount_token):
        """
        :param amount_token: 받은 토큰을 실제 자산에 더함
        :return: 없음

        에피소드당 step이 1이므로 사용하지 않는다.
        """
        self.asset += amount_token

    def learn(self, action, reward):
        """
        :param action: 행동
        :param reward: 보상
        :return:
        """
        q1 = self.q_table[action]
        q2 = reward

        """
        확률이 적었던 선택은 크게 업데이트 할 수 있도록
            -   beta_table의 값으로 나눠줌.
        """
        self.q_table[action] += self.args.lr * (q2 - q1) / self.beta_table[action]
        self.beta_table = self.softmax(self.q_table)
