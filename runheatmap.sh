#!/usr/bin/env bash
#####################
# python3
# review_history=0, window=5
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=500 --review_history=0 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=500 --review_history=0 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=500 --review_history=0 --window=5
# change n_agent 100->70
python store_heatmap.py --mechanism="proportional" --n_agent=70 --reward_pool=500 --review_history=0 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=70 --reward_pool=500 --review_history=0 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=70 --reward_pool=500 --review_history=0 --window=5
# change n_agent 100->50
python store_heatmap.py --mechanism="proportional" --n_agent=50 --reward_pool=500 --review_history=0 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=50 --reward_pool=500 --review_history=0 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=50 --reward_pool=500 --review_history=0 --window=5
# change n_agent 100->20
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=500 --review_history=0 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=500 --review_history=0 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=500 --review_history=0 --window=5
# change n_agent 20, reward_pool 500->200
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=200 --review_history=0 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=200 --review_history=0 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=200 --review_history=0 --window=5
# change n_agent 20, reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=100 --review_history=0 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=100 --review_history=0 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=100 --review_history=0 --window=5
# change reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=100 --review_history=0 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=100 --review_history=0 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=100 --review_history=0 --window=5
# change reward_pool 500->700
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=700 --review_history=0 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=700 --review_history=0 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=700 --review_history=0 --window=5
# change reward_pool 500->1000
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=1000 --review_history=0 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=1000 --review_history=0 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=1000 --review_history=0 --window=5
#####################
# review_history=0, window=20
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=500 --review_history=0 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=500 --review_history=0 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=500 --review_history=0 --window=20
# change n_agent 100->70
python store_heatmap.py --mechanism="proportional" --n_agent=70 --reward_pool=500 --review_history=0 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=70 --reward_pool=500 --review_history=0 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=70 --reward_pool=500 --review_history=0 --window=20
# change n_agent 100->50
python store_heatmap.py --mechanism="proportional" --n_agent=50 --reward_pool=500 --review_history=0 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=50 --reward_pool=500 --review_history=0 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=50 --reward_pool=500 --review_history=0 --window=20
# change n_agent 100->20
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=500 --review_history=0 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=500 --review_history=0 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=500 --review_history=0 --window=20
# change n_agent 20, reward_pool 500->200
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=200 --review_history=0 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=200 --review_history=0 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=200 --review_history=0 --window=20
# change n_agent 20, reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=100 --review_history=0 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=100 --review_history=0 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=100 --review_history=0 --window=20
# change reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=100 --review_history=0 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=100 --review_history=0 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=100 --review_history=0 --window=20
# change reward_pool 500->700
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=700 --review_history=0 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=700 --review_history=0 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=700 --review_history=0 --window=20
# change reward_pool 500->1000
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=1000 --review_history=0 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=1000 --review_history=0 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=1000 --review_history=0 --window=20
#####################
# review_history=0, window=50
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=500 --review_history=0 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=500 --review_history=0 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=500 --review_history=0 --window=50
# change n_agent 100->70
python store_heatmap.py --mechanism="proportional" --n_agent=70 --reward_pool=500 --review_history=0 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=70 --reward_pool=500 --review_history=0 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=70 --reward_pool=500 --review_history=0 --window=50
# change n_agent 100->50
python store_heatmap.py --mechanism="proportional" --n_agent=50 --reward_pool=500 --review_history=0 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=50 --reward_pool=500 --review_history=0 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=50 --reward_pool=500 --review_history=0 --window=50
# change n_agent 100->20
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=500 --review_history=0 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=500 --review_history=0 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=500 --review_history=0 --window=50
# change n_agent 20, reward_pool 500->200
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=200 --review_history=0 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=200 --review_history=0 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=200 --review_history=0 --window=50
# change n_agent 20, reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=100 --review_history=0 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=100 --review_history=0 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=100 --review_history=0 --window=50
# change reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=100 --review_history=0 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=100 --review_history=0 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=100 --review_history=0 --window=50
# change reward_pool 500->700
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=700 --review_history=0 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=700 --review_history=0 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=700 --review_history=0 --window=50
# change reward_pool 500->1000
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=1000 --review_history=0 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=1000 --review_history=0 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=1000 --review_history=0 --window=50
#####################
# review_history=1, window=5
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=500 --review_history=1 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=500 --review_history=1 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=500 --review_history=1 --window=5
# change n_agent 100->70
python store_heatmap.py --mechanism="proportional" --n_agent=70 --reward_pool=500 --review_history=1 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=70 --reward_pool=500 --review_history=1 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=70 --reward_pool=500 --review_history=1 --window=5
# change n_agent 100->50
python store_heatmap.py --mechanism="proportional" --n_agent=50 --reward_pool=500 --review_history=1 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=50 --reward_pool=500 --review_history=1 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=50 --reward_pool=500 --review_history=1 --window=5
# change n_agent 100->20
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=500 --review_history=1 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=500 --review_history=1 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=500 --review_history=1 --window=5
# change n_agent 20, reward_pool 500->200
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=200 --review_history=1 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=200 --review_history=1 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=200 --review_history=1 --window=5
# change n_agent 20, reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=100 --review_history=1 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=100 --review_history=1 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=100 --review_history=1 --window=5
# change reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=100 --review_history=1 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=100 --review_history=1 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=100 --review_history=1 --window=5
# change reward_pool 500->700
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=700 --review_history=1 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=700 --review_history=1 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=700 --review_history=1 --window=5
# change reward_pool 500->1000
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=1000 --review_history=1 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=1000 --review_history=1 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=1000 --review_history=1 --window=5
#####################
# review_history=1, window=20
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=500 --review_history=1 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=500 --review_history=1 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=500 --review_history=1 --window=20
# change n_agent 100->70
python store_heatmap.py --mechanism="proportional" --n_agent=70 --reward_pool=500 --review_history=1 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=70 --reward_pool=500 --review_history=1 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=70 --reward_pool=500 --review_history=1 --window=20
# change n_agent 100->50
python store_heatmap.py --mechanism="proportional" --n_agent=50 --reward_pool=500 --review_history=1 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=50 --reward_pool=500 --review_history=1 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=50 --reward_pool=500 --review_history=1 --window=20
# change n_agent 100->20
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=500 --review_history=1 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=500 --review_history=1 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=500 --review_history=1 --window=20
# change n_agent 20, reward_pool 500->200
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=200 --review_history=1 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=200 --review_history=1 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=200 --review_history=1 --window=20
# change n_agent 20, reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=100 --review_history=1 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=100 --review_history=1 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=100 --review_history=1 --window=20
# change reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=100 --review_history=1 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=100 --review_history=1 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=100 --review_history=1 --window=20
# change reward_pool 500->700
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=700 --review_history=1 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=700 --review_history=1 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=700 --review_history=1 --window=20
# change reward_pool 500->1000
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=1000 --review_history=1 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=1000 --review_history=1 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=1000 --review_history=1 --window=20
#####################
# review_history=1, window=50
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=500 --review_history=1 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=500 --review_history=1 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=500 --review_history=1 --window=50
# change n_agent 100->70
python store_heatmap.py --mechanism="proportional" --n_agent=70 --reward_pool=500 --review_history=1 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=70 --reward_pool=500 --review_history=1 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=70 --reward_pool=500 --review_history=1 --window=50
# change n_agent 100->50
python store_heatmap.py --mechanism="proportional" --n_agent=50 --reward_pool=500 --review_history=1 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=50 --reward_pool=500 --review_history=1 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=50 --reward_pool=500 --review_history=1 --window=50
# change n_agent 100->20
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=500 --review_history=1 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=500 --review_history=1 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=500 --review_history=1 --window=50
# change n_agent 20, reward_pool 500->200
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=200 --review_history=1 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=200 --review_history=1 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=200 --review_history=1 --window=50
# change n_agent 20, reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=100 --review_history=1 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=100 --review_history=1 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=100 --review_history=1 --window=50
# change reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=100 --review_history=1 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=100 --review_history=1 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=100 --review_history=1 --window=50
# change reward_pool 500->700
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=700 --review_history=1 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=700 --review_history=1 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=700 --review_history=1 --window=50
# change reward_pool 500->1000
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=1000 --review_history=1 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=1000 --review_history=1 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=1000 --review_history=1 --window=50
#####################
# review_history=2, window=5
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=500 --review_history=2 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=500 --review_history=2 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=500 --review_history=2 --window=5
# change n_agent 100->70
python store_heatmap.py --mechanism="proportional" --n_agent=70 --reward_pool=500 --review_history=2 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=70 --reward_pool=500 --review_history=2 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=70 --reward_pool=500 --review_history=2 --window=5
# change n_agent 100->50
python store_heatmap.py --mechanism="proportional" --n_agent=50 --reward_pool=500 --review_history=2 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=50 --reward_pool=500 --review_history=2 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=50 --reward_pool=500 --review_history=2 --window=5
# change n_agent 100->20
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=500 --review_history=2 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=500 --review_history=2 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=500 --review_history=2 --window=5
# change n_agent 20, reward_pool 500->200
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=200 --review_history=2 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=200 --review_history=2 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=200 --review_history=2 --window=5
# change n_agent 20, reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=100 --review_history=2 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=100 --review_history=2 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=100 --review_history=2 --window=5
# change reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=100 --review_history=2 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=100 --review_history=2 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=100 --review_history=2 --window=5
# change reward_pool 500->700
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=700 --review_history=2 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=700 --review_history=2 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=700 --review_history=2 --window=5
# change reward_pool 500->1000
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=1000 --review_history=2 --window=5
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=1000 --review_history=2 --window=5
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=1000 --review_history=2 --window=5
#####################
# review_history=2, window=20
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=500 --review_history=2 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=500 --review_history=2 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=500 --review_history=2 --window=20
# change n_agent 100->70
python store_heatmap.py --mechanism="proportional" --n_agent=70 --reward_pool=500 --review_history=2 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=70 --reward_pool=500 --review_history=2 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=70 --reward_pool=500 --review_history=2 --window=20
# change n_agent 100->50
python store_heatmap.py --mechanism="proportional" --n_agent=50 --reward_pool=500 --review_history=2 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=50 --reward_pool=500 --review_history=2 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=50 --reward_pool=500 --review_history=2 --window=20
# change n_agent 100->20
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=500 --review_history=2 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=500 --review_history=2 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=500 --review_history=2 --window=20
# change n_agent 20, reward_pool 500->200
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=200 --review_history=2 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=200 --review_history=2 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=200 --review_history=2 --window=20
# change n_agent 20, reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=100 --review_history=2 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=100 --review_history=2 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=100 --review_history=2 --window=20
# change reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=100 --review_history=2 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=100 --review_history=2 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=100 --review_history=2 --window=20
# change reward_pool 500->700
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=700 --review_history=2 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=700 --review_history=2 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=700 --review_history=2 --window=20
# change reward_pool 500->1000
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=1000 --review_history=2 --window=20
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=1000 --review_history=2 --window=20
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=1000 --review_history=2 --window=20
#####################
# review_history=2, window=50
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=500 --review_history=2 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=500 --review_history=2 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=500 --review_history=2 --window=50
# change n_agent 100->70
python store_heatmap.py --mechanism="proportional" --n_agent=70 --reward_pool=500 --review_history=2 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=70 --reward_pool=500 --review_history=2 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=70 --reward_pool=500 --review_history=2 --window=50
# change n_agent 100->50
python store_heatmap.py --mechanism="proportional" --n_agent=50 --reward_pool=500 --review_history=2 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=50 --reward_pool=500 --review_history=2 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=50 --reward_pool=500 --review_history=2 --window=50
# change n_agent 100->20
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=500 --review_history=2 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=500 --review_history=2 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=500 --review_history=2 --window=50
# change n_agent 20, reward_pool 500->200
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=200 --review_history=2 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=200 --review_history=2 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=200 --review_history=2 --window=50
# change n_agent 20, reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=20 --reward_pool=100 --review_history=2 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=20 --reward_pool=100 --review_history=2 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=20 --reward_pool=100 --review_history=2 --window=50
# change reward_pool 500->100
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=100 --review_history=2 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=100 --review_history=2 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=100 --review_history=2 --window=50
# change reward_pool 500->700
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=700 --review_history=2 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=700 --review_history=2 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=700 --review_history=2 --window=50
# change reward_pool 500->1000
python store_heatmap.py --mechanism="proportional" --n_agent=100 --reward_pool=1000 --review_history=2 --window=50
python store_heatmap.py --mechanism="exponential" --n_agent=100 --reward_pool=1000 --review_history=2 --window=50
python store_heatmap.py --mechanism="uniform" --n_agent=100 --reward_pool=1000 --review_history=2 --window=50
