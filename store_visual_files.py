#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:31:50 2019

@author: jeffrey
"""

import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns
import pickle
import os
import argparse
import numpy as np
import sys

def argparser():
    parser=argparse.ArgumentParser()
    parser.add_argument('--mechanism',type=str,)
    parser.add_argument('--n_agent',type=int,)
    parser.add_argument('--reward_pool',type=int,)
    parser.add_argument('--review_history',type=int,)
    parser.add_argument('--window',type=int,)
    parser.add_argument('--n_episode',type=int,default=500)
    parser.add_argument('--record_term_1',type=int,default=10)
    parser.add_argument('--record_term_2',type=int,default=5)
    parser.add_argument('--range_endeavor',type=int,default=10)
    parser.add_argument('--n_average',type=int,default=100)
    args = parser.parse_args()
    return args

args=argparser()
my_args=sys.argv
filename = "./data/{}_{}_{}_{}_{}.pkl".format(
        my_args[1][2:], my_args[2][2:], my_args[3][2:], my_args[4][2:], my_args[5][2:])
with open(filename,'rb') as f:
    dict_=pickle.load(f)
    

#all_returns = dict_['all_returns']
#all_costs = dict_['all_costs']
#all_rewards = dict_['all_rewards']
#all_actions = dict_['all_actions']
#all_highests = dict_['all_highests']
#all_likes = dict_['all_likes']

#heatmap
all_total_beta_lists = dict_['all_total_beta_lists'] #term1 = 10
all_details = dict_['all_details_total_beta_lists'] #term2 = 5


weighted_endeavor_list = []
for episode in range(int(args.n_episode / args.record_term_1) + 1):
    avg_total_beta_lists = np.zeros((args.n_agent, args.range_endeavor))

    # print("\n\nepisode {}".format(episode * args.record_term_1))
    for i in range(args.n_average):
        avg_total_beta_lists += np.array(all_total_beta_lists[i][episode]) / args.n_average
    
    # heatmap
    # weighted average endeavor
    weighted_endeavor = np.array(
        [sum(avg_total_beta_lists[k] * np.arange(0., args.range_endeavor)) for k in range(args.n_agent)])
    weighted_endeavor_list.append(weighted_endeavor)
    
if not os.path.exists("./visualization/{}/{}/{}/{}/{}/images/".format(
        my_args[1][2:], my_args[2][2:], my_args[3][2:], my_args[4][2:], my_args[5][2:])):
    os.makedirs("./visualization/{}/{}/{}/{}/{}/images/".format(
        my_args[1][2:], my_args[2][2:], my_args[3][2:], my_args[4][2:], my_args[5][2:]))
# weighted average endeavor
fig = plt.figure()
ax = sns.heatmap(np.array(weighted_endeavor_list))
ax.xaxis.tick_top()
# writer.add_figure("weighted_avg_endeavor_heatmap", fig)
plt.savefig("./visualization/{}/{}/{}/{}/{}/images/weighted_endeavor".format(my_args[1][2:], my_args[2][2:], my_args[3][2:], my_args[4][2:], my_args[5][2:]))
#plt.close(fig)
    
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
#    plt.close(fig)


        

