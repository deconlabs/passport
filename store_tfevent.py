import pickle
import argparse
import numpy as np
import sys
from tensorboardX import SummaryWriter
from visualization import draw_graphs


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mechanism', type=str,)
    parser.add_argument('--n_agent', type=int,)
    parser.add_argument('--reward_pool', type=int,)
    parser.add_argument('--review_history', type=int,)
    parser.add_argument('--window', type=int,)
    parser.add_argument('--n_episode', type=int, default=500)
    parser.add_argument('--record_term_1', type=int, default=10)
    parser.add_argument('--record_term_2', type=int, default=5)
    parser.add_argument('--range_endeavor', type=int, default=10)
    parser.add_argument('--n_average', type=int, default=100)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = argparser()
    my_args = sys.argv

    writer = SummaryWriter("./visualization/{}/{}/{}/{}/{}".format(
        my_args[1][2:], my_args[2][2:], my_args[3][2:], my_args[4][2:], my_args[5][2:]))

    filename = "./data/{}_{}_{}_{}_{}.pkl".format(
        my_args[1][2:], my_args[2][2:], my_args[3][2:], my_args[4][2:], my_args[5][2:])

    """
    load pkl files
    """
    with open(filename, 'rb') as f:
        dict_ = pickle.load(f)

    all_returns = dict_['all_returns']
    all_costs = dict_['all_costs']
    all_rewards = dict_['all_rewards']
    all_actions = dict_['all_actions']
    all_highests = dict_['all_highests']
    all_likes = dict_['all_likes']
    all_total_beta_lists = dict_['all_total_beta_lists']  # term1 = 10

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
        sqr_avg_total_beta_lists = np.zeros(
            (args.n_agent, args.range_endeavor))
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

        # tensorboard
        draw_graphs(writer, args, np.arange(args.n_agent),
                    avg_returns,
                    avg_costs,
                    avg_rewards,
                    avg_actions,
                    avg_highests,
                    avg_total_beta_lists,
                    avg_likes,
                    episode * args.record_term_1, "avg_")
        draw_graphs(writer, args, np.arange(args.n_agent),
                    avg_returns - (1.96 / pow(args.n_average, 0.5)) * std_returns,
                    avg_costs - (1.96 / pow(args.n_average, 0.5)) * std_costs,
                    avg_rewards - (1.96 / pow(args.n_average, 0.5)) * std_rewards,
                    avg_actions - (1.96 / pow(args.n_average, 0.5)) * std_actions,
                    avg_highests - (1.96 / pow(args.n_average, 0.5)) * std_highests,
                    avg_total_beta_lists - (1.96 / pow(args.n_average, 0.5)) * std_total_beta_lists,
                    avg_likes - (1.96 / pow(args.n_average, 0.5)) * std_likes,
                    episode * args.record_term_1, "under_")
        draw_graphs(writer, args, np.arange(args.n_agent),
                    avg_returns + (1.96 / pow(args.n_average, 0.5)) * std_returns,
                    avg_costs + (1.96 / pow(args.n_average, 0.5)) * std_costs,
                    avg_rewards + (1.96 / pow(args.n_average, 0.5)) * std_rewards,
                    avg_actions + (1.96 / pow(args.n_average, 0.5)) * std_actions,
                    avg_highests + (1.96 / pow(args.n_average, 0.5)) * std_highests,
                    avg_total_beta_lists + (1.96 / pow(args.n_average, 0.5)) * std_total_beta_lists,
                    avg_likes + (1.96 / pow(args.n_average, 0.5)) * std_likes,
                    episode * args.record_term_1, "upper_")

    writer.close()
