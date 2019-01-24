#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 18:22:03 2019

@author: jeffrey
"""
import numpy as np


def review_return(return_dict, review_ratio, agents, writer, episode):
    avg_return_for_review = np.mean(
        [return_dict[i][-1] for i in range(len(agents)) if return_dict[i][-1] != 0]) - 0.2
    med_return_for_review = np.median(
        [return_dict[i][-1] for i in range(len(agents)) if return_dict[i][-1] != 0]) - 0.2
    writer.add_scalars('review_return', {'review_ratio': review_ratio,
                                         'avg_return_for_reviewer': avg_return_for_review,
                                         'med_return_for_reviewer': med_return_for_review
                                         }, episode)


def reward_review(return_dict, cost_dict, review_ratio, agents, writer, episode):
    avg_reward_for_review = np.mean([return_dict[i][-1] - cost_dict[i][-1]
                                     for i in range(len(agents)) if return_dict[i][-1] != 0])
    med_reward_for_review = np.median(
        [return_dict[i][-1] - cost_dict[i][-1] for i in range(len(agents)) if return_dict[i][-1] != 0])
    writer.add_scalars('reward_review', {'review_ratio': review_ratio,
                                         'avg_return_for_reviewer': avg_reward_for_review,
                                         'med_return_for_reviewer': med_reward_for_review
                                         }, episode)


def cost_endeavor(cost_dict, endeavor_list, agents, writer, episode):
    avg_cost_for_review = np.mean(
        [cost_dict[i][-1] for i in range(len(agents)) if cost_dict[i][-1] != 0])
    avg_endeavor_reviewer = np.mean(
        [endeavor for i, endeavor in enumerate(endeavor_list)if endeavor_list[i] != 0]) - 3
    writer.add_scalars('cost_endeavor', {'avg_cost_for_review': avg_cost_for_review,
                                         'avg_endeavor_for_review': avg_endeavor_reviewer,
                                         }, episode)


def avg_like_for_review(likes, endeavor_list, writer, episode):
    avg_like_for_review = np.mean([like for like in likes if like != 0])
    avg_endeavor_reviewer = np.mean(
        [endeavor for i, endeavor in enumerate(endeavor_list)if endeavor_list[i] != 0]) - 3
    writer.add_scalars('like_endeavor', {'avg_like_for_review': avg_like_for_review,
                                         'avg_endeavor_for_review': avg_endeavor_reviewer,
                                         }, episode)


def agent_base_graph(agents, writer):
    for i, agent in enumerate(agents):
        writer.add_scalar("endeavor_distribution",
                          agent.get_action(deterministic=True), i)
        writer.add_scalar("weighted_average_endeavor", np.sum(
            np.array(agent.endeavor) * agent.beta_table), i)
        writer.add_scalar("asset", agent.asset, i)
