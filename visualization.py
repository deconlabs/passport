def list_formated_print(flist):
    print('[ ', end='')
    for i, elem in enumerate(flist):
        if i == len(flist) - 1:
            print(str(format(elem * 100, '7.2f')), end='')
            print(' ]')
        else:
            print(str(format(elem * 100, '7.2f')) + ',', end='')


def draw_graphs(
        writer, args, agents, returns, costs, rewards, actions, highests, total_beta_lists, likes, episode, name):
    draw_action_ratio(writer, args, agents, returns, costs, rewards,
                      actions, highests, total_beta_lists, likes, episode, name)
    draw_about_reward(writer, args, agents, returns, costs, rewards,
                      actions, highests, total_beta_lists, likes, episode, name)
    draw_weighted_endeavor(writer, args, agents, returns, costs,
                           rewards, actions, highests, total_beta_lists, likes, episode, name)
    draw_highest(writer, args, agents, returns, costs, rewards,
                 actions, highests, total_beta_lists, likes, episode, name)


# """x축: episode"""
# review_ratio 대신 action_ratio
def draw_action_ratio(
        writer, args, agents, returns, costs, rewards, actions, highests, total_beta_lists, likes, episode, name):
    writer.add_scalars("action_ratio", {name + "action_ratio": sum(actions) / ((args.range_endeavor - 1) * len(agents))}, episode)


# """x축: episode"""
# reward, return, cost, and like
def draw_about_reward(
        writer, args, agents, returns, costs, rewards, actions, highests, total_beta_lists, likes, episode, name):
    res_dict = {}
    for i in range(len(agents)):
        res_dict[name + 'agent_' + str(i) + '_reward'] = rewards[i]
        res_dict[name + 'agent_' + str(i) + '_return'] = returns[i]
        res_dict[name + 'agent_' + str(i) + '_cost'] = costs[i]
        res_dict[name + 'agent_' + str(i) + '_like'] = likes[i]

    res_dict[name + '/average_reward'] = sum(rewards) / len(rewards)
    res_dict[name + '/average_return'] = sum(returns) / len(returns)
    res_dict[name + '/average_cost'] = sum(costs) / len(costs)
    res_dict[name + '/average_like'] = sum(likes) / len(likes)

    writer.add_scalars("about_reward", res_dict, episode)


# """x축: episode"""
# weighted_endeavor
def draw_weighted_endeavor(
        writer, args, agents, returns, costs, rewards, actions, highests, total_beta_lists, likes, episode, name):
    res_dict = {}
    for i in range(len(agents)):
        res_dict[name + 'agent_' + str(i)] = 0
        for j in range(len(total_beta_lists[i])):
            res_dict[name + 'agent_' + str(i)] += total_beta_lists[i][j] * float(j)

    writer.add_scalars("weighted_endeavor", res_dict, episode)


# highest
def draw_highest(
        writer, args, agents, returns, costs, rewards, actions, highests, total_beta_lists, likes, episode, name):
    res_dict = {}
    for i in range(len(agents)):
        res_dict[name + 'agent_' + str(i)] = highests[i]

    writer.add_scalars("highest", res_dict, episode)


# """기타: Use matplotlib"""
# agent별 asset 분포 (pareto)
# endeavor와 real_endeavor의 모양
