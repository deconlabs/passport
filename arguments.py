import argparse


def argparser():
    parser = argparse.ArgumentParser()

    """Simulation Settings"""
    parser.add_argument('--n_agent', type=int, default=100,
                        help='The number of agents in simulation')

    parser.add_argument('--n_episode', type=int, default=500,
                        help='The number of episodes for simulation')

    parser.add_argument('--n_average', type=int, default=10,
                        help='The number of times which need for calculating average')

    parser.add_argument('--range_endeavor', type=int, default=10,
                        help='The range of endeavor')

    parser.add_argument('--mechanism', type=str, default='proportional',
                        help='Select the mechanism of getting return(gain):'
                             'uniform, exponential, and proportional(default)')

    parser.add_argument('--reward_pool', type=int, default=100,
                        help='The total rewards which reviewers divide up')

    """Visualization"""
    parser.add_argument('--record_term_1', type=int, default=10,
                        help='The term of episodes recording')

    parser.add_argument('--record_term_2', type=int, default=100,
                        help='The term of episodes recording')

    """Coefficients for Like Function"""
    parser.add_argument('--like_coef_1', type=float, default=2.0,
                        help='The value which controls \'like\' distribution')

    parser.add_argument('--like_coef_2', type=float, default=1.0,
                        help='The value which controls \'like\' distribution')

    """Coefficients for Cost Function"""
    parser.add_argument('--b0', type=float, default=1.0,
                        help='The constant term of cost function')

    parser.add_argument('--b1', type=float, default=0.1,
                        help='The asset\'s coefficient of cost function')

    parser.add_argument('--b2', type=float, default=1.0,
                        help='The endeavor\'s coefficient of cost function')

    parser.add_argument('--b3', type=float, default=0.5,
                        help='The asset * endeavor\'s coefficient of cost function')

    """Hyperparameters"""
    parser.add_argument('--window', type=int, default=5,
                        help='The window size of deque which contains past review')

    parser.add_argument('--std_dev', type=float, default=1.0,
                        help='The standard deviation for gaussian distribution in Like')

    parser.add_argument('--temperature', type=float, default=2.0,
                        help='The temperature value for softmax')

    parser.add_argument('--lr', type=float, default=0.01,
                        help='The learning rate')

    args = parser.parse_args()
    return args
