import argparse


def argparser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--mechanism', type=str, default='proportional',
                        help='TBA')

    parser.add_argument('--temperature', type=float, default=10.0,
                        help='temperature value for softmax')
    parser.add_argument('--window', type=int, default=5,
                        help='TBA')
    parser.add_argument('--std_dev', type=float, default=1.0,
                        help='Standard deviation for gaussian distribution in Like')

    parser.add_argument('--reward_pool', type=int, default=100,
                        help='TBA')

    parser.add_argument('--cost', type=float, default=5.0,
                        help='TBA')

    parser.add_argument('--b0', type=float, default=0.0,
                        help='TBA')
    parser.add_argument('--b1', type=float, default=50000,
                        help='TBA')
    parser.add_argument('--b2', type=float, default=10.0,
                        help='TBA')
    parser.add_argument('--b3', type=float, default=0.1,
                        help='TBA')
    parser.add_argument('--like_coef', type=float, default=2.0,
                        help='TBA')

    parser.add_argument('--n_agent', type=int, default=15,
                        help='The number of agents in simulation')

    parser.add_argument('--n_episode', type=int, default=300,
                        help='The number of episodes for simulation')

    parser.add_argument('--tiny_value', type=float, default=0.05,
                        help='TBA')

    parser.add_argument('--total_asset', type=int, default=100,
                        help='Total amount of asset for agents')

    parser.add_argument('--range_endeavor', type=int, default=10,
                        help='TBA')

    parser.add_argument('--lr', type=float, default=1e-2,
                        help='learning rate')

    parser.add_argument('--record_term', type=int, default=100,
                        help='TBA')

    args = parser.parse_args()
    return args
