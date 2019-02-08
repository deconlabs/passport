import numpy as np
import random
import sys
import pickle
import os

from agent import Agent
from arguments import argparser
from env import Env


def distribute_asset(env, n_agent):
    # probs=np.random.normal(total_asset/n_agent, 3, n_agent)
    probs = np.random.pareto(2, n_agent)
    probs /= np.sum(probs)
    probs = sorted(probs)[::-1]

    for i in range(n_agent):
        env.agent_assets[i] = probs[i]


def run(env, agents, args):
    res_returns = []
    res_costs = []
    res_rewards = []
    res_actions = []
    res_highests = []
    res_total_beta_lists = []
    res_likes = []
    detail_beta_lists = []

    """per episode"""
    for episode in range(args.n_episode + 1):
        actions = []
        for agent in agents:
            actions.append(agent.get_action())  # 확률론적

        """per step"""
        # just a one step.
        _, rewards, _, info = env.step(actions)

        for idx, agent in enumerate(agents):
            agent.learn(actions[idx], rewards[idx])

        # review_ratio = info['review_ratio']
        returns = info['returns']
        costs = info['costs']
        likes = info['likes']

        highests = [agent.get_action(deterministic=True) for agent in agents]
        total_beta_lists = [agent.beta_table for agent in agents]

        if episode % args.record_term_1 == 0:
            res_returns.append(returns)
            res_costs.append(costs)
            res_rewards.append(rewards)
            res_actions.append(actions)
            res_highests.append(highests)
            res_total_beta_lists.append(total_beta_lists)
            res_likes.append(likes)

        if episode % args.record_term_2 == 0:
            detail_beta_lists.append(total_beta_lists)

    return (
        res_returns,
        res_costs,
        res_rewards,
        res_actions,
        res_highests,
        res_total_beta_lists,
        res_likes,
        detail_beta_lists
    )


if __name__ == '__main__':
    my_args = sys.argv
    print(my_args)
    args = argparser()

    """set random seeds"""
    np.random.seed(950327)
    random.seed(950327)

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
        distribute_asset(env, args.n_agent)
        agents = [Agent(env.action_space, args) for i in range(args.n_agent)]

        """run"""
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

    """pickle files save"""
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
