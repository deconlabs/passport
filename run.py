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


def distribute_asset(agents, total_asset, n_agent):
    # probs=np.random.normal(total_asset/n_agent, 3, n_agent)
    probs = np.random.pareto(2, n_agent)
    probs /= np.sum(probs)
    probs = sorted(probs)[::-1]

    for i in range(n_agent):
        agents[i].asset = probs[i]


def run(env, agents, args):
    return_dict = defaultdict(lambda: deque(maxlen=100))
    cost_dict = defaultdict(lambda: deque(maxlen=100))

    for episode in range(args.n_episode + 1):
        distribute_asset(agents, args.total_asset, args.n_agent)

        # print("episode {} starts".format(episode))
        review_ratio, actions, returns, costs, rewards = env.step(agents)
        endeavor_list = [agent.get_action(deterministic=True) for agent in agents]

        for i in range(len(agents)):
            return_dict[i].append(returns[i])
            cost_dict[i].append(costs[i])

        # visualisation
        if episode % 10 == 0:
            writer.add_scalar("review_ratio", review_ratio, episode)
            # writer.add_scalar("actions", review_ratio, episode)
            # writer.add_scalar("data/review_ratio", review_ratio, episode)
            # writer.add_scalar("data/review_ratio", review_ratio, episode)
            # writer.add_scalar("data/review_ratio", review_ratio, episode)

        if episode % args.record_term == 0:
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

            print("episode: {}, review_ratio: {}".format(episode, review_ratio))

            for j in range(len(agents)):
                print(format(j, '2d'),
                      "\tcost:", format(costs[j], '7.4f'),
                      "\treturn:", format(returns[j], '7.4f'),
                      "\treward:", format(rewards[j], '7.4f'),
                      "\tendeavor_list:", format(endeavor_list[j], '7.4f'),
                      "\taction:", format(actions[j], '7.4f'))


if __name__ == '__main__':
    args = argparser()
    writer = SummaryWriter("./visualization/{}".format(args.mechanism + "_" + str(args.n_agent)))
    env = Env(args)
    agents = [Agent(env.action_space, args) for i in range(args.n_agent)]
    run(env, agents, args)
    writer.close()
