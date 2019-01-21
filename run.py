# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:17:54 2019
@author: user
"""

from tensorboardX import SummaryWriter
from collections import Counter
import numpy as np

from agent import Agent
from arguments import argparser

from env import Env


def distribute_asset(agents, total_asset, n_agent):
    # np.random.pareto 분포를 쓰면 좋을듯
    probs = np.random.pareto(2, n_agent)
    probs /= np.sum(probs)
    probs = sorted(probs)[::-1]

    for i in range(n_agent):
        agents[i].asset = probs[i]*total_asset


def run(env, agents, args):
    final_list = [{} for _ in range(args.range_endeavor)]
    endeavor_list = []
    for episode in range(args.n_episode + 1):
        distribute_asset(agents, args.total_asset, args.n_agent)
#        print("episode {} starts".format(episode))
        review_ratio, actions = env.step(agents)

        endeavor_list.append([agent.get_action(deterministic=True) for agent in agents])

        # visualisation
        writer.add_scalar("data/review_ratio", review_ratio, episode)

        if episode % args.record_term == 0:
            # for idx, agent in enumerate(agents):
            #    data_beta_table = dict((str(i), v) for i, v in enumerate(agent.beta_table))
            #    writer.add_scalars("data/agents/{}".format(idx), data_beta_table, episode)

            print("episode: {}, review_ratio: {}".format(episode, review_ratio))

            counter = Counter(actions)
            for act in range(args.range_endeavor):
                final_list[act][str(episode)] = counter[act]

    for i in range(args.range_endeavor):
        writer.add_scalars("data/endeavor", final_list[i], i)


if __name__ == '__main__':
    writer = SummaryWriter()
    args = argparser()
    env = Env(args)
    agents = [Agent(env.action_space, args) for i in range(args.n_agent)]
    run(env, agents, args)
    writer.close()
