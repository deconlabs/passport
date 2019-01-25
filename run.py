from tensorboardX import SummaryWriter
import numpy as np
import random
import sys

from agent import Agent
from arguments import argparser
from env import Env
from visualization import draw_graphs
# from visualization import list_formated_print


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
    :return:    res_returns, res_costs, res_rewards, res_actions, res_highests, res_beta_tables, res_likes
                for each agents
    """
    res_returns = []
    res_costs = []
    res_rewards = []
    res_actions = []
    res_highests = []
    res_total_beta_lists = []
    res_likes = []

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
        get_action으로 각 에이전트의 action을 갱신하고,
        리스트 형태로 저장함.

        *   deterministic=True이므로 결정론적으로 action이 결정됨
        """
        highests = [agent.get_action(deterministic=True) for agent in agents]
        total_beta_lists = [agent.beta_table for agent in agents]

        """
        default: record_term_1 = 10
        default: record_term_2 = 100
        """
        if episode % args.record_term_1 == 0:
            """
            record
            """
            print("current episode", episode)

            res_returns.append(returns)
            res_costs.append(costs)
            res_rewards.append(rewards)
            res_actions.append(actions)
            res_highests.append(highests)
            res_total_beta_lists.append(total_beta_lists)
            res_likes.append(likes)

        """
        다음 에피소드를 위해 총 좋아요의 수를 초기화
        """
        env.total_like = 0

    return res_returns, res_costs, res_rewards, res_actions, res_highests, res_total_beta_lists, res_likes


if __name__ == '__main__':
    """
    main
    """
    # print(sys.argv)
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
    default n_average=10
    """
    all_returns = []
    all_costs = []
    all_rewards = []
    all_actions = []
    all_highests = []
    all_total_beta_lists = []
    all_likes = []

    for i in range(args.n_average):
        env = Env(args)
        agents = [Agent(env.action_space, args) for i in range(args.n_agent)]
        returns, costs, rewards, actions, highests, total_beta_lists, likes = run(
            env, agents, args)

        all_returns.append(returns)
        all_costs.append(costs)
        all_rewards.append(rewards)
        all_actions.append(actions)
        all_highests.append(highests)
        all_total_beta_lists.append(total_beta_lists)
        all_likes.append(likes)

        print("loop", i, "done")

    """
    average
    per recorded episode
    """
    for episode in range(int(args.n_episode / args.record_term_1) + 1):
        avg_returns = np.zeros(args.n_agent)
        avg_costs = np.zeros(args.n_agent)
        avg_rewards = np.zeros(args.n_agent)
        avg_actions = np.zeros(args.n_agent)
        avg_highests = np.zeros(args.n_agent)
        avg_total_beta_lists = np.zeros((args.n_agent, args.range_endeavor))
        avg_likes = np.zeros(args.n_agent)

        print("\n\nepisode {}".format(episode * args.record_term_1))

        for i in range(args.n_average):
            avg_returns += np.array(all_returns[i][episode]) / args.n_average
            avg_costs += np.array(all_costs[i][episode]) / args.n_average
            avg_rewards += np.array(all_rewards[i][episode]) / args.n_average
            avg_actions += np.array(all_actions[i][episode]) / args.n_average
            avg_highests += np.array(all_highests[i][episode]) / args.n_average
            avg_total_beta_lists += np.array(
                all_total_beta_lists[i][episode]) / args.n_average
            avg_likes += np.array(all_likes[i][episode]) / args.n_average

        """
        시각화 부분
        """

        """console"""
        """
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", end='')
        for j in range(len(avg_total_beta_lists[0])):
            if j == len(avg_total_beta_lists[0]) - 1:
                print(j)
            else:
                print(j, end='\t ')

        for j in range(len(agents)):
            print(format(j, '2d'),
                  "\treturn:", format(avg_returns[j], '5.2f'),
                  "\tcost:", format(avg_costs[j], '5.2f'),
                  "\treward:", format(avg_rewards[j], '5.2f'),
                  "\taction:", format(avg_actions[j], '5.2f'),
                  "\thighest:", format(avg_highests[j], '5.2f'),
                  "\tlike:", format(avg_likes[j], '5.2f'),
                  "\tbeta_table(%): ", end='')
            list_formated_print(avg_total_beta_lists[j])
        """

        """tensorboard"""
        draw_graphs(writer, args, agents,
                    avg_returns, avg_costs, avg_rewards, avg_actions, avg_highests, avg_total_beta_lists, avg_likes,
                    episode * args.record_term_1)

    writer.close()
