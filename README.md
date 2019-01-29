# Abstract

## Decentrailized Review System
* 어떤 리뷰 시스템을 가지고 있는가?
  * 리뷰를 남기면 호텔에서 선지불한 리워드풀에서 나누어 지급됨
  * 사용자들은 리뷰를 남기는 노고(cost)와 보상을 비교하여 이득이 되는 행동을 한다.
    * 이득이 되는 노력 수준 [0, ..., 9]
  
* 어떤 이코노미 환경 상에서 사람들이 가장 열심히 리뷰를 작성할까?
  * 전체 리워드풀을 얼마나 줘야하나?
  * 리워드 분배를 어떻게 해야하나?
* 또는, 어떤 이코노미 환경 상에서 사용자들이 어떻게 행동할까?

### Hyperparameters
* 에이전트 수
* 에피소드 횟수
* 평균을 몇 번이나? - 100번 해서 평균을 구했음
* 노력 범위
* 메커니즘
  * proportion
  * exponential
  * uniform
* 과거 review 히스토리 몇 개나 볼 것인가?

### functions


# How to Use

## Run
```bash
python3 run.py [--<arg1>=<value1>] [--<arg2>=<value2>] ...
```
*or*
```bash
/bin/sh runpy.sh
```

### Example
```bash
python3 run.py --mechanism="proportional" --n_agent=100 --reward_pool=500 --review_history=False --window=5
```

## View Tensorboard
```bash
tensorboard --port=6021 --logdir <path>
```

# Trouble Shooting

## Check Flake8 Convention
```bash
autopep8 -i graph_generate.py
flake8 --ignore E501
```
