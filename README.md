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
python3 run.py --n_agent=20 --n_episode=5000 --n_average=3 --record_term_1=100 --mechanism="proportional"
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
