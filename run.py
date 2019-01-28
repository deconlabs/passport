from tensorboardX import SummaryWriter
import numpy as np
import random
import sys
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns

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
        review_ratio, actions, returns, costs, rewards, likes = env.step(agents)

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
        returns, costs, rewards, actions, highests, total_beta_lists, likes, details = run(env, agents, args)

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
    files save
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

    """
    get average values per recorded episode
    """
    """
    weighted_endeavor_list = []

    for episode in range(int(args.n_episode / args.record_term_1) + 1):
        avg_returns = np.zeros(args.n_agent)
        avg_costs = np.zeros(args.n_agent)
        avg_rewards = np.zeros(args.n_agent)
        avg_actions = np.zeros(args.n_agent)
        avg_highests = np.zeros(args.n_agent)
        avg_total_beta_lists = np.zeros((args.n_agent, args.range_endeavor))
        avg_likes = np.zeros(args.n_agent)

        sqr_avg_returns = np.zeros(args.n_agent)
        sqr_avg_costs = np.zeros(args.n_agent)
        sqr_avg_rewards = np.zeros(args.n_agent)
        sqr_avg_actions = np.zeros(args.n_agent)
        sqr_avg_highests = np.zeros(args.n_agent)
        sqr_avg_total_beta_lists = np.zeros((args.n_agent, args.range_endeavor))
        sqr_avg_likes = np.zeros(args.n_agent)

        # print("\n\nepisode {}".format(episode * args.record_term_1))

        for i in range(args.n_average):
            avg_returns += np.array(all_returns[i][episode]) / args.n_average
            avg_costs += np.array(all_costs[i][episode]) / args.n_average
            avg_rewards += np.array(all_rewards[i][episode]) / args.n_average
            avg_actions += np.array(all_actions[i][episode]) / args.n_average
            avg_highests += np.array(all_highests[i][episode]) / args.n_average
            avg_total_beta_lists += np.array(all_total_beta_lists[i][episode]) / args.n_average
            avg_likes += np.array(all_likes[i][episode]) / args.n_average

            sqr_avg_returns += np.power(np.array(all_returns[i][episode]), 2) / args.n_average
            sqr_avg_costs += np.power(np.array(all_costs[i][episode]), 2) / args.n_average
            sqr_avg_rewards += np.power(np.array(all_rewards[i][episode]), 2) / args.n_average
            sqr_avg_actions += np.power(np.array(all_actions[i][episode]), 2) / args.n_average
            sqr_avg_highests += np.power(np.array(all_highests[i][episode]), 2) / args.n_average
            sqr_avg_total_beta_lists += np.power(np.array(all_total_beta_lists[i][episode]), 2) / args.n_average
            sqr_avg_likes += np.power(np.array(all_likes[i][episode]), 2) / args.n_average

        std_returns = np.power(sqr_avg_returns - np.power(avg_returns, 2), 0.5)
        std_costs = np.power(sqr_avg_costs - np.power(avg_costs, 2), 0.5)
        std_rewards = np.power(sqr_avg_rewards - np.power(avg_rewards, 2), 0.5)
        std_actions = np.power(sqr_avg_actions - np.power(avg_actions, 2), 0.5)
        std_highests = np.power(sqr_avg_highests - np.power(avg_highests, 2), 0.5)
        std_total_beta_lists = np.power(sqr_avg_total_beta_lists - np.power(avg_total_beta_lists, 2), 0.5)
        std_likes = np.power(sqr_avg_likes - np.power(avg_likes, 2), 0.5)

        # 시각화 부분
        # console

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

        # tensorboard
        draw_graphs(writer, args, agents,
                    avg_returns,
                    avg_costs,
                    avg_rewards,
                    avg_actions,
                    avg_highests,
                    avg_total_beta_lists,
                    avg_likes,
                    episode * args.record_term_1, "avg_")

        draw_graphs(writer, args, agents,
                    avg_returns - (1.96 / pow(args.n_average, 0.5)) * std_returns,
                    avg_costs - (1.96 / pow(args.n_average, 0.5)) * std_costs,
                    avg_rewards - (1.96 / pow(args.n_average, 0.5)) * std_rewards,
                    avg_actions - (1.96 / pow(args.n_average, 0.5)) * std_actions,
                    avg_highests - (1.96 / pow(args.n_average, 0.5)) * std_highests,
                    avg_total_beta_lists - (1.96 / pow(args.n_average, 0.5)) * std_total_beta_lists,
                    avg_likes - (1.96 / pow(args.n_average, 0.5)) * std_likes,
                    episode * args.record_term_1, "under_")

        draw_graphs(writer, args, agents,
                    avg_returns + (1.96 / pow(args.n_average, 0.5)) * std_returns,
                    avg_costs + (1.96 / pow(args.n_average, 0.5)) * std_costs,
                    avg_rewards + (1.96 / pow(args.n_average, 0.5)) * std_rewards,
                    avg_actions + (1.96 / pow(args.n_average, 0.5)) * std_actions,
                    avg_highests + (1.96 / pow(args.n_average, 0.5)) * std_highests,
                    avg_total_beta_lists + (1.96 / pow(args.n_average, 0.5)) * std_total_beta_lists,
                    avg_likes + (1.96 / pow(args.n_average, 0.5)) * std_likes,
                    episode * args.record_term_1, "upper_")

        # heatmap
        # weighted average endeavor
        weighted_endeavor = np.array(
            [sum(avg_total_beta_lists[k] * np.arange(0., args.range_endeavor)) for k in range(len(agents))])
        weighted_endeavor_list.append(weighted_endeavor)

    if not os.path.exists("./visualization/{}/{}/{}/{}/{}/images".format(
            my_args[1][2:], my_args[2][2:], my_args[3][2:], my_args[4][2:], my_args[5][2:])):
        os.mkdir("./visualization/{}/{}/{}/{}/{}/images".format(
            my_args[1][2:], my_args[2][2:], my_args[3][2:], my_args[4][2:], my_args[5][2:]))

    # weighted average endeavor
    fig = plt.figure()
    ax = sns.heatmap(np.array(weighted_endeavor_list))
    ax.xaxis.tick_top()
    # writer.add_figure("weighted_avg_endeavor_heatmap", fig)
    plt.savefig("./visualization/{}/{}/{}/{}/{}/images/weighted_endeavor".format(my_args[1][2:], my_args[2][2:], my_args[3][2:], my_args[4][2:], my_args[5][2:]))
    plt.close(fig)

    # details beta table heatmap
    for episode in range(int(args.n_episode / args.record_term_2) + 1):
        avg_details = np.zeros((args.n_agent, args.range_endeavor))

        for i in range(args.n_average):
            avg_details += np.array(all_details[i][episode]) / args.n_average

        # beta_table
        fig = plt.figure()
        ax = sns.heatmap(avg_details.T)
        ax.xaxis.tick_top()
        # writer.add_figure("beta_table_heatmap", fig, episode)
        plt.savefig("./visualization/{}/{}/{}/{}/{}/images/{}".format(
            my_args[1][2:], my_args[2][2:], my_args[3][2:], my_args[4][2:], my_args[5][2:], episode))
        plt.close(fig)
    """

    writer.close()
