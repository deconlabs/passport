import numpy as np
from collections import deque


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
            -   초기 cost 값 0.0

        *   asset: 초기 할당받는 자산
            -   비율로 할당됨.
        """
        self.args = args

        self.endeavor = action_space  # [0, 1, 2, ...]
        self.action = 0  # index: 0 or 1 or 2 or ...
        self.my_like = 0.
        self.review_history = deque(maxlen=args.window)  # 1 or 0
        self.cost = 0.
        self.asset = 0.

        self.q_table = np.zeros_like(self.endeavor)
        self.beta_table = self.softmax(self.q_table)

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

    # def receive_token(self, amount_token):
    #     self.asset += amount_token

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
        self.q_table[action] += self.args.lr * \
            (q2 - q1) / self.beta_table[action]
        self.beta_table = self.softmax(self.q_table)
