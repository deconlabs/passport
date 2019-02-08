import numpy as np


class Agent:
    def __init__(self, action_space, args):
        self.args = args

        self.endeavor = action_space  # [0, 1, 2, ...]
        self.action = 0  # index: 0 or 1 or 2 or ...

        self.q_table = np.zeros_like(self.endeavor)
        self.beta_table = self.softmax(self.q_table)

    def softmax(self, x):
        if not isinstance(x, np.ndarray):
            x = np.array(x)

        x = x / self.args.temperature  # temperature scaling
        e_x = np.exp(x - np.max(x))  # prevent overflow
        return e_x / np.sum(e_x)

    def get_action(self, deterministic=False):
        """
        :param deterministic: True일 경우 결정론적으로 가장 높은 확률을 가진 action이 선출됨. 아닐 경우 확률적으로 결정.
        :return: 에이전트의 액션.
        """

        if deterministic:
            b = np.array(self.beta_table)
            action = np.random.choice(np.flatnonzero(b == b.max()))

        else:
            action = np.random.choice(self.endeavor, 1, p=self.beta_table)

        action = int(action)
        self.action = action
        return action

    def learn(self, action, reward):
        q1 = self.q_table[action]
        q2 = reward

        self.q_table[action] += self.args.lr * (q2 - q1) / self.beta_table[action]
        self.beta_table = self.softmax(self.q_table)
