# Draft

## Intro: Decentrailized Review System
* 어떤 리뷰 시스템을 가지고 있는가?
  * 리뷰를 남기면 호텔에서 선지불한 리워드풀에서 나누어 지급됨
  * 사용자들은 리뷰를 남기는 노고(cost)와 보상을 비교하여 이득이 되는 행동을 한다.
    * 이득이 되는 노력 수준 [0, ..., 9]

* 어떤 이코노미 환경 상에서 사람들이 가장 열심히 리뷰를 작성할까?
  * 전체 리워드풀을 얼마나 줘야하나?
  * 리워드 분배를 어떻게 해야하나?
* 또는, 어떤 이코노미 환경 상에서 사용자들이 어떻게 행동할까?

---

- [ ] Jeffrey
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

---

- [ ] Luke
### functions
* cost
  * 에이전트는 자신의 노력 수준을 통해 cost가 얼마나 드는지 산정 가능.
  * 에이전트의 asset이 많을수록 cost가 높아짐.
  * ```asset```, ```endeavor```, 그리고 ```asset*endeavor``` 항이 있어서, 각 항의 계수를 잘 조정하는 것으로 원하는 cost 양상을 그릴 수 있음.
    * ```asset*endeavor``` 계수를 높이면, 선형적인 특성에서부터 점차 벗어날 수 있음.
  * real_endeavor
    * 노력이 선형적이 아닌 지수적으로 반영됨
      * 노력을 한 단위 올릴 때 들어가는 비용이 더 커짐
      * 일정 수준 이상 가면 올리는 cost가 

* return
  * like
    * 에이전트가 자신의 글이 받을 like를 예상
    * 들인 노력과, 리뷰 히스토리로부터 like가 예상됨
      * 리뷰 히스토리 방법론
        * 0: 과거에 리뷰 썼으면 -> like를 더 받을 것
        * 1: +) 과거에 리뷰 하나도 안 쓰다가 쓰면 정말 빡쳐서 쓴거거나 정말 좋아서 쓴거니 좋아요 많이 받을 것
        * 2: 1번을 더 발전시켜서, 과거 리뷰 갯수와 받는 좋아요 예상이 반대로 감
      * action으로 구함 (real_endeavor 안 씀)
        * 이미 한 액션에 대하여 like를 받게 되므로
    * 예상 좋아요가 정규분포를 따라 랜덤하게 구해짐
    * 내가 받은 like / total 모든 글의 like * reward_pool로 내 리턴이 결정됨
      * 다른 사람들이 얼마나 like를 받을 지 모르므로, 내 return을 예상할 수는 없다.
        * 다른 사람들이 들인 노력을 모르므로

* reward = return - cost


## Analysis

---

- [ ] Jeffrey
### 기준 1) review ratio (action ratio)
* avg 값, 신뢰구간, 각 에이전트의 값
  * 에이전트 0이랑, 에이전트 50이랑, 그리고 에이전트 99
    * 에이전트 분포는 asset이 많은 순에서 적은 순으로 sort됨.
      * 에이전트 에셋 분포 그림
      * pareto

* 각 매커니즘 별 비교
* 참여 에이전트 수에 따라 비교
* 리워드 풀에 따라 비교
* 리뷰 히스토리 반영 방법에 따라 비교
* 리뷰 히스토리 반영 갯수에 따라 비교

---

- [ ] Luke
### 기준 2) endeavor 분포 (with beta table)
* 히트맵 이용
  * GIF
  * 히트맵 1:
    * x축 에이전트, y축 action인 그래프가 episode 시간축을 따라 존재
    * beta table을 색상으로 보여줌
  * 히트맵 2:
    * x축 에이전트, y축이 episode
    * weighted endeavor를 보여줌

## Limitation
* people doesn't make decision based on lucrative reasons, rather on 감정

## Conclusion
* 생태계 지배자의 입맛에 따라 세팅이 달라진다.
  * 리워드풀
  * 유니폼으로 하면 사람들이 노력을 안한다!


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
