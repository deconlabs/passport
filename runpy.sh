#!/usr/bin/env bash
# python3
python run.py --mechanism="proportional" --n_agent=100 --reward_pool=500 --review_history=0 --window=5
python run.py --mechanism="exponential" --n_agent=100 --reward_pool=500 --review_history=0 --window=5
python run.py --mechanism="uniform" --n_agent=100 --reward_pool=500 --review_history=0 --window=5
