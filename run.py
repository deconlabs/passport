# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:17:54 2019
@author: user
"""

from tensorboardX import SummaryWriter
from collections import deque, defaultdict
import numpy as np

from agent import Agent
from arguments import argparser

from env import Env


def distribute_asset(agents, n_agent):
    """
    :param agents: 참여 에이전트들
    :param n_agent: 참여 에이전트의 수
    :return: 없음
    """

    """
    초기에 에이전트에게 자산을 배분하는 함수

    *   초기 구현에서는 total_asset이라는 실제 자산의 양을 설정하고 이를 배분했으나,
        그럴 경우 참여 에이전트 수에 따라 배분받는 total_asset이 현저하게 차이날 수 있으므로,
    *   실제 자산을 배분하는 것이 아닌 비율만 산정하는 것으로 변경함.

    *   정규분포보다 현 사회를 잘 반영할 수 있는 모델로
    *   pareto 분포를 사용함
        -   빌프레도 파레토는 파레토 분포를 사회에서 부의 분포를 나타내기 위해 사용하였다.
        -   사회에서는 부의 불공평한 분포로 인해 대부분의 부가 소수에 의해 소유되는데 (파레토 법칙),
        -   파레토 분포는 이를 효과적으로 나타낸다.
        -   Pareto, Vilfredo, Cours d’Économie Politique: Nouvelle édition par G.-H. Bousquet et G. Busino,
            Librairie Droz, Geneva, 1964, pages 299–345.

    *   에이전트의 수에 영향을 받지 않도록 정규화 과정을 거침
    *   자산이 많은 사람이 앞에(빠른 인덱스 번호) 오도록 정렬
    """
    # probs=np.random.normal(total_asset/n_agent, 3, n_agent)
    probs = np.random.pareto(2, n_agent)
    probs /= np.sum(probs)
    probs = sorted(probs)[::-1]

    for i in range(n_agent):
        agents[i].asset = probs[i]


def run(env, agents, args):
    """
    :param env: 정의한 환경
    :param agents: 참여 에이전트들
    :param args: 하이퍼파라메터들
    :return: 없음
    """

    return_dict = defaultdict(lambda: deque(maxlen=100))
    cost_dict = defaultdict(lambda: deque(maxlen=100))

    """
    환경에서 에이전트를 구동하는 함수
    
    *   에피소드보다 1만큼 더 돌림
        -   record_term 만큼 돌리는데 제일 마지막 수행까지 기록하기 위하여
        -   가령 300 에피소드를 100번째마다 기록한다고 하면, 0, 100, 200, 300의 수행을 기록할 수 있다.
    """
    for episode in range(args.n_episode + 1):
        """
        자산을 분배한다.
        
        *   매 에피소드마다 자산을 새로 분배함
            -   본 시뮬레이션에서는 step이라는 개념이 딱히 필요 없음
            -   매 에피소드는 1 step으로 돌아간다고 봐도 무방
        """
        distribute_asset(agents, args.n_agent)

        # print("episode {} starts".format(episode))
        """
        실제 1 step을 수행함.
        """
        review_ratio, actions, returns, costs, rewards = env.step(agents)

        """
        get_action으로 각 에이전트의 action을 갱신하고,
        리스트 형태로 저장함.
        
        *   deterministic=True이므로 결정론적으로 action이 결정됨  
        """
        endeavor_list = [agent.get_action(deterministic=True) for agent in agents]

        for i in range(len(agents)):
            return_dict[i].append(returns[i])
            cost_dict[i].append(costs[i])

        """
        시각화 부분.
        
        default: record_term_1 = 10
        default: record_term_2 = 100
        """
        # visualisation
        if episode % args.record_term_1 == 0:
            writer.add_scalar("review_ratio", review_ratio, episode)
            # writer.add_scalar("actions", review_ratio, episode)
            # writer.add_scalar("data/review_ratio", review_ratio, episode)
            # writer.add_scalar("data/review_ratio", review_ratio, episode)
            # writer.add_scalar("data/review_ratio", review_ratio, episode)

        if episode % args.record_term_2 == 0:
            print("episode: {}, review_ratio: {}".format(episode, review_ratio))

            # for idx, agent in enumerate(agents):
            # data_beta_table = dict((str(i), v) for i, v in enumerate(agent.beta_table))
            # writer.add_scalars("data/{}".format(idx), data_beta_table, episode)
            for i, agent in enumerate(agents):
                writer.add_scalar("episode{}/endeavor_distribution".format(episode),
                                  agent.get_action(deterministic=True), i)
                writer.add_scalar("episode{}/weighted_average_endeavor".format(episode),
                                  np.sum(np.array(agent.endeavor) * agent.beta_table), i)
                writer.add_scalars("episode{}/return_cost".format(episode),
                                   {'returns': np.mean(return_dict[i]), 'costs': np.mean(cost_dict[i])}, i)

            """
            console 출력 부분
            """
            for j in range(len(agents)):
                print(format(j, '2d'),
                      "\tcost:", format(costs[j], '7.4f'),
                      "\treturn:", format(returns[j], '7.4f'),
                      "\treward:", format(rewards[j], '7.4f'),
                      "\tendeavor_list:", format(endeavor_list[j], '7.4f'),
                      "\taction:", format(actions[j], '7.4f'))


"""
main
"""
if __name__ == '__main__':
    args = argparser()
    writer = SummaryWriter("./visualization/{}".format(args.mechanism + "_" + str(args.n_agent)))

    env = Env(args)
    agents = [Agent(env.action_space, args) for i in range(args.n_agent)]
    run(env, agents, args)

    writer.close()
