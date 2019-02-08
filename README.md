# Passport

Simulation of Incentive Design

- [Part 1: 보상 시스템 설계 문제 및 시뮬레이션 환경 소개](https://medium.com/decon-lab/simulation-of-incentive-design-어떤-보상-시스템이-가장-적합한가-part-1-b0160ee611b1)   
- [Part 2: 히트맵을 통한 시뮬레이션 결과 오버뷰](https://medium.com/decon-lab/simulation-of-incentive-design-어떤-보상-시스템이-가장-적합한가-part-2-d7c02966cb70)   
- [Part 3: 시뮬레이션 결과 분석](https://medium.com/decon-lab/simulation-of-incentive-design-어떤-보상-시스템이-가장-적합한가-part-3-166b33411689)   


# Abstract

* We use a Bandit algorithm.   
* Running 240 cases takes less than a day.   
* ```run.py``` saves \*.pkl (pickle) files which contain all simulation results.   
* We use tensorboardX and matplotlib for visualization.   
* Following Flake8 convention, openai-gym style APIs.   


# Details

## action_space
에이전트가 가질 수 있는 행동의 모음

## agent_assets
자산 분배의 **비율**   
초기 구현에서는 total_asset이라는 실제 자산의 양을 설정하고 이를 배분했으나, 그럴 경우 참여 에이전트 수에 따라 배분받는 total_asset이 현저하게 차이날 수 있으므로, 실제 자산을 배분하는 것이 아닌 비율만 산정하는 것으로 변경함.   
- 자산에 영향을 받는 cost 함수에서, asset이 포함된 항의 계수에 n_agent를 곱해줘야 함: 정규화   
정규분포보다 현 사회를 잘 반영할 수 있는 모델로 pareto 분포를 사용함.   
- 빌프레도 파레토는 파레토 분포를 사회에서 부의 분포를 나타내기 위해 사용하였다.   
- 사회에서는 부의 불공평한 분포로 인해 대부분의 부가 소수에 의해 소유되는데 (파레토 법칙), 파레토 분포는 이를 효과적으로 나타낸다.   
> Pareto, Vilfredo, Cours d’Économie Politique: Nouvelle édition par G.-H. Bousquet et G. Busino, Librairie Droz, Geneva, 1964, pages 299–345.   
    - 정규화 과정을 거침   
    - 자산이 많은 사람이 앞에(빠른 인덱스 번호) 오도록 정렬   

## real_endeavor
노력을 실제 계산(cost 함수 등)에 반영할 때, 정수 값을 그대로 반영하는 것이 아니라 가공하여 적용.   
- 실제 들어가는 노력은 선형적으로 증가하는 것이 아니라 지수적으로 증가함을 가정.   
시작점이 0, 끝 점이 n임은 동일하나, 본래 선형적으로 증가하던 endeavor와는 달리 지수적으로 증가함.   

## review_history
최근의 r 에피소드에서 얼마나 리뷰를 작성했었는가를 나타내는 지표.   
과거 에피소드의 리뷰 작성 여부가 현재 에이전트가 받는 좋아요 등에 영향을 끼칠 수 있음.   
리뷰를 작성했을 경우 1, 아닐 경우 0으로 기록한다.   
- 최근 r 에피소드를 기록   
  - r은 args.window에서 설정   
  - default: 5   

## review_history로부터 score를 도출하는 방법론

### Case 0
args.review_history=0   
과거에 리뷰를 더 많이 쓸 수록 받는 좋아요가 많음   
- 리뷰 작성의 경험이 풍부하면 더 좋은 리뷰를 작성할 가능성이 크다.   
- 더 많은 호텔을 경험했으면 보다 객관적일 것이라는 판단   

### Case 1
args.review_history=1   
과거에 리뷰를 작성하지 않다가 갑자기 작성했을 경우에 대한 판단   
리뷰를 안 쓰던 사람이 썼을 정도이니까   
- 완전히 좋거나, 완전히 나쁘거나 할 것이다.   
- 리뷰에 대한 신뢰도 UP   
    - 좋아요 많이 받음   

### Case 2
args.review_history=2   
과거에 리뷰를 더 많이 쓸 수록 받는 좋아요가 적음   
- Case 1을 보다 확장   
- 리뷰를 안 쓰던 사람이 갑자기 리뷰를 쓴 것이니, 믿을 수 있다.   

## review_ratio & action_ratio

### review_ratio
리뷰 작성의 비율. 에이전트 중 몇 명이 리뷰를 작성하였는가를 나타내는 지표이다.    
0일때만 0이고, 0보다 크면 무조건 1이기에 값의 분포가 충분히 반영되지 못한다.   

### action_ratio
action의 크기가 반영된 review_ratio   
agent들의 양상을 보다 정확히 반영할 수 있다.   


## action & highest

### action
get_action으로 각 에이전트의 action을 갱신함.   
- default: deterministic=False이므로 확률적으로 action이 결정된다.   

### highests
highests: 가장 확률이 높은 값   
- deterministic=True   
- 만일 가장 확률이 높은 값이 두 개 이상이라면 그 중에 하나 랜덤 결정   


# How to Use

## Run
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


## View Tensorboard
```bash
tensorboard --port=6021 --logdir <path>
```


## Visualization
```bash
python3 store_heatmap.py [--<arg1>=<value1>] [--<arg2>=<value2>] ...
python3 store_tfevent.py [--<arg1>=<value1>] [--<arg2>=<value2>] ...
```


# Trouble Shooting

## Check Flake8 Convention
```bash
autopep8 -i graph_generate.py
flake8 --ignore E501
```


# Author
[@Aiden](https://github.com/belepi93)   
[@Jeffey](https://github.com/jsrimr)   
[@Luke](https://github.com/twodude)   


# License
TBA
