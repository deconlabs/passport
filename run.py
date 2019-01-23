# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:17:54 2019
@author: user
"""

from tensorboardX import SummaryWriter
from collections import Counter, deque, defaultdict
import numpy as np

from agent import Agent
from arguments import argparser

from env import Env
from graph_generate import review_return,reward_review,cost_endeavor,avg_like_for_review,agent_base_graph

def distribute_asset(agents, total_asset, n_agent):
    # np.random.pareto 분포를 쓰면 좋을듯
#    probs=np.random.normal(total_asset/n_agent, 3, n_agent)
    
    probs = np.random.pareto(2, n_agent)
    probs /= np.sum(probs)
    probs = sorted(probs)[::-1]

    for i in range(n_agent):
        agents[i].asset = probs[i]


def run(env, agents, args):
#    final_list = [{} for _ in range(args.range_endeavor)]
    
    return_dict = defaultdict(lambda: deque(maxlen=100))
    cost_dict = defaultdict(lambda: deque(maxlen=100))
    
    for episode in range(args.n_episode + 1):
        distribute_asset(agents, args.total_asset, args.n_agent)
#        print("episode {} starts".format(episode))
        review_ratio, actions, returns, costs, rewards,likes = env.step(agents)
        endeavor_list=[agent.get_action(deterministic=True) for agent in agents]
        
        for i in range(len(agents)):
            return_dict[i].append(returns[i])
            cost_dict[i].append(costs[i])

        # visualisation
        if episode % 10==0:
#            writer.add_scalar("review_ratio", review_ratio, episode)
#            return_ = np.mean([return_dict[i][-1] for i in range(len(agents)) if return_dict[i][-1] != 0])
#            writer.add_scalars("return_cost", {"return":return_, "cost":cost}, episode)
            review_return(return_dict,review_ratio,agents,writer,episode)
#            avg_return_for_review= np.mean([return_dict[i][-1] for i in range(len(agents)) if return_dict[i][-1] != 0])-0.2
#            med_return_for_review=np.median([return_dict[i][-1] for i in range(len(agents)) if return_dict[i][-1] != 0])-0.2
#            writer.add_scalars('review_return',{'review_ratio' : review_ratio,
#                                               'avg_return_for_reviewer':avg_return_for_review,
#                                               'med_return_for_reviewer':med_return_for_review
#                                               },episode)
            reward_review(return_dict,cost_dict,review_ratio,agents,writer,episode)
#            avg_reward_for_review=np.mean([return_dict[i][-1]-cost_dict[i][-1] for i in range(len(agents)) if return_dict[i][-1] != 0])
#            med_reward_for_review=np.median([return_dict[i][-1]-cost_dict[i][-1] for i in range(len(agents)) if return_dict[i][-1] != 0])
#            writer.add_scalars('review_reward',{'review_ratio' : review_ratio,
#                                               'avg_return_for_reviewer':avg_reward_for_review,
#                                               'med_return_for_reviewer':med_reward_for_review
#                                               },episode)
            cost_endeavor(cost_dict,endeavor_list,agents,writer,episode)
#            avg_cost_for_review = np.mean([cost_dict[i][-1] for i in range(len(agents)) if cost_dict[i][-1] != 0])
#            avg_endeavor_reviewer = np.mean([endeavor for i,endeavor in enumerate(endeavor_list )if endeavor_list[i]!=0])-3
#            writer.add_scalars('cost_endeavor',{'avg_cost_for_review' : avg_cost_for_review,
#                                               'avg_endeavor_for_review':avg_endeavor_reviewer,                                 
#                                               },episode)
            avg_like_for_review(likes,endeavor_list,writer,episode)
#            avg_like_for_review = np.mean([like for like in likes if like!= 0])
#            writer.add_scalars('like_endeavor',{'avg_like_for_review' : avg_like_for_review,
#                                               'avg_endeavor_for_review':avg_endeavor_reviewer,                                 
#                                               },episode)
    
        
        
        if episode % 100 == 0:
            #"""
            
    
            print("episode: {}, review_ratio: {}".format(episode, review_ratio))
            
#            for i,agent in enumerate(agents):
#                writer.add_scalars("return_cost",
#                                   {'returns_{}'.format(episode):np.mean(return_dict[i]) , 
#                                    'costs_{}'.format(episode) : np.mean(cost_dict[i])},i)
            #"""
            for j in range(len(agents)):
                print(format(j, '2d'),
                      "\tcost:", format(costs[j], '7.4f'),
                      "\treturn:", format(returns[j], '7.4f'),
                      "\treward:", format(rewards[j], '7.4f'),
                      "\tendeavor_list:", format(endeavor_list[j], '7.4f'),
                      "\taction:", format(actions[j], '7.4f'))
    agent_base_graph(agents,writer)
#    for i,agent in enumerate(agents):
#        writer.add_scalar("endeavor_distribution",agent.get_action(deterministic=True),i)
#        writer.add_scalar("weighted_average_endeavor",np.sum(np.array(agent.endeavor)*agent.beta_table),i)
#        writer.add_scalar("asset",agent.asset,i)
                
#        writer.add_scalars("".format(episode),{'returns':np.mean(return_dict[i]) , 'costs' : np.mean(cost_dict[i])},i)

#            counter = Counter(actions)
#            for act in range(args.range_endeavor):
#                final_list[act][str(episode)] = counter[act]
#
#    for i in range(args.range_endeavor):
#        writer.add_scalars("data/endeavor", final_list[i], i)

if __name__ == '__main__':    
    args = argparser()
    writer = SummaryWriter("./visualization/{}".format(args.mechanism+"_"+str(args.n_agent)))
    env = Env(args)
    agents = [Agent(env.action_space, args) for i in range(args.n_agent)]
    run(env, agents, args)
    writer.close()