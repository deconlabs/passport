import numpy as np
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
