# Passport

Simulation of Incentive Design

- [Part 1: 보상 시스템 설계 문제 및 시뮬레이션 환경 소개](https://medium.com/decon-lab/simulation-of-incentive-design-어떤-보상-시스템이-가장-적합한가-part-1-b0160ee611b1)   
- [Part 2: 히트맵을 통한 시뮬레이션 결과 오버뷰](https://medium.com/decon-lab/simulation-of-incentive-design-어떤-보상-시스템이-가장-적합한가-part-2-d7c02966cb70)   
- [Part 3: 시뮬레이션 결과 분석](https://medium.com/decon-lab/simulation-of-incentive-design-어떤-보상-시스템이-가장-적합한가-part-3-166b33411689)   


## Abstract

* We use a Bandit algorithm.   
* Running 240 cases takes less than a day.
* ```run.py``` saves \*.pkl (pickle) files which contain all simulation results.
* We use tensorboardX and matplotlib for visualization.

## How to Use

### Run
```bash
python3 run.py [--<arg1>=<value1>] [--<arg2>=<value2>] ...
```

```bash
python3 run.py --mechanism="proportional" --n_agent=100 --reward_pool=500 --review_history=False --window=5
```

*or*
```bash
/bin/sh runpy.sh
```

### View Tensorboard
```bash
tensorboard --port=6021 --logdir <path>
```

### Visualization
```bash
python3 store_heatmap.py [--<arg1>=<value1>] [--<arg2>=<value2>] ...
python3 store_tfevent.py [--<arg1>=<value1>] [--<arg2>=<value2>] ...
```

## Trouble Shooting

### Check Flake8 Convention
```bash
autopep8 -i graph_generate.py
flake8 --ignore E501
```

## Author
[@Aiden](https://github.com/belepi93)   
[@Jeffey](https://github.com/jsrimr)   
[@Luke](https://github.com/twodude)   
