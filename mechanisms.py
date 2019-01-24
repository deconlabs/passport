#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 19:12:17 2019

@author: jeffrey
"""

import numpy as np

# reward  distribution system
# how to change get_reward()  function

# encourage influentail people
# previous: porportional to like [0.1,0.3,0.4,0.2]
# after: quadratically proportianl [0.03333333, 0.3       , 0.53333333, 0.13333333]


# UNIFORM
def mechanism_v1(reward_pool, likes, total_like, n_reviewers):
    uniform_reward = reward_pool / n_reviewers
    likes = np.array(likes) / total_like
    rewards = [uniform_reward if like != 0 else 0 for like in likes]
    return rewards


# EXPONENTIAL
def mechanism_v2(reward_pool, likes, total_like, n_reviewers):
    likes = np.array(likes) / total_like
    exp_prop = np.power(likes, 2)
    exp_prop = exp_prop / sum(exp_prop)
    rewards = exp_prop * reward_pool
    return rewards


# DEFAULT: PROPORTIONAL
def mechanism_v3(reward_pool, likes, total_like, n_reviewers):
    likes = np.array(likes) / total_like
    rewards = likes * reward_pool
    return rewards


# give rewards more when write reviews for hotel which has few reviews
def mec4():
    pass


# cannot figure autonomously the best reward system, but gives hints of which system is better.
