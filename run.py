from tensorboardX import SummaryWriter
import numpy as np
import random
import sys
import pickle
import os

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
        -   자산에 영향을 받는 cost 함수에서, asset이 포함된 항의 계수에
        -   n_agent를 곱해줘야 함: 정규화

    *   정규분포보다 현 사회를 잘 반영할 수 있는 모델로 pareto 분포를 사용함
        -   빌프레도 파레토는 파레토 분포를 사회에서 부의 분포를 나타내기 위해 사용하였다.
        -   사회에서는 부의 불공평한 분포로 인해 대부분의 부가 소수에 의해 소유되는데 (파레토 법칙),
        -   파레토 분포는 이를 효과적으로 나타낸다.
        -   Pareto, Vilfredo, Cours d’Économie Politique: Nouvelle édition par G.-H. Bousquet et G. Busino,
            Librairie Droz, Geneva, 1964, pages 299–345.

    *   정규화 과정을 거침
    *   자산이 많은 사람이 앞에(빠른 인덱스 번호) 오도록 정렬함
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
    :return:    res_returns, res_costs, res_rewards, res_actions, res_highests, res_beta_tables, res_likes,
                detail_beta_lists
                    -   for each agents
                    -   평균을 내기 위해 return함
    """
    res_returns = []
    res_costs = []
    res_rewards = []
    res_actions = []
    res_highests = []
    res_total_beta_lists = []
    res_likes = []

    detail_beta_lists = []

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

        """
        실제 1 step을 수행함.

        *   review_ratio: float
        *   actions: list of int
        *   returns: list of float
        *   costs: list of float
        *   rewards: list of float
        *   likes: list of float
        """
        review_ratio, actions, returns, costs, rewards, likes = env.step(
            agents)

        """
        get_action으로 각 에이전트의 action을 갱신하고, 리스트 형태로 저장함.
            -   deterministic=True이므로 결정론적으로 action이 결정됨
            -   highests: 가장 확률이 높은 값
            -   만일 가장 확률이 높은 값이 두 개 이상이라면 그 중에 하나 랜덤 결정
        """
        highests = [agent.get_action(deterministic=True) for agent in agents]
        total_beta_lists = [agent.beta_table for agent in agents]

        """
        default: record_term_1 = 10
        default: record_term_2 = 5
        """
        if episode % args.record_term_1 == 0:
            """
            record
            """
            # print("current episode", episode)

            res_returns.append(returns)
            res_costs.append(costs)
            res_rewards.append(rewards)
            res_actions.append(actions)
            res_highests.append(highests)
            res_total_beta_lists.append(total_beta_lists)
            res_likes.append(likes)

        if episode % args.record_term_2 == 0:
            """
            record
            """
            detail_beta_lists.append(total_beta_lists)

        """
        다음 에피소드를 위해 총 좋아요의 수를 초기화
        """
        env.total_like = 0

    return res_returns, res_costs, res_rewards, res_actions, res_highests, res_total_beta_lists, res_likes,\
        detail_beta_lists


if __name__ == '__main__':
    """
    main
    """
    print(sys.argv)
    # mechanism, n_agent, reward_pool, review_history, window
    my_args = sys.argv

    """
    set random seeds
    """
    np.random.seed(950327)
    random.seed(950327)

    args = argparser()
    writer = SummaryWriter("./visualization/{}/{}/{}/{}/{}".format(
        my_args[1][2:], my_args[2][2:], my_args[3][2:], my_args[4][2:], my_args[5][2:]))

    """
    default n_average=100
    """
    all_returns = []
    all_costs = []
    all_rewards = []
    all_actions = []
    all_highests = []
    all_total_beta_lists = []
    all_likes = []
    all_details = []

    for i in range(args.n_average):
        env = Env(args)
        agents = [Agent(env.action_space, args) for i in range(args.n_agent)]
        returns, costs, rewards, actions, highests, total_beta_lists, likes, details = run(
            env, agents, args)

        all_returns.append(returns)
        all_costs.append(costs)
        all_rewards.append(rewards)
        all_actions.append(actions)
        all_highests.append(highests)
        all_total_beta_lists.append(total_beta_lists)
        all_likes.append(likes)
        all_details.append(details)

        print("loop", i, "done")

    """
    pickle files save
    """
    meta_dict = {
        'all_returns': all_returns,
        'all_costs': all_costs,
        'all_rewards': all_rewards,
        'all_actions': all_actions,
        'all_highests': all_highests,
        'all_total_beta_lists': all_total_beta_lists,
        'all_likes': all_likes,
        'all_details_total_beta_lists': all_details
    }

    filename = "./data/{}_{}_{}_{}_{}.pkl".format(
        my_args[1][2:], my_args[2][2:], my_args[3][2:], my_args[4][2:], my_args[5][2:])
    if not os.path.exists('./data'):
        os.mkdir('./data')
    with open(filename, 'wb') as f:
        pickle.dump(meta_dict, f)

    writer.close()
