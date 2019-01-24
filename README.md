# How to Use

## Run
```bash
python3 run.py [--<arg1>=<value1>] [--<arg2>=<value2>] ...
```
*or*
```bash
/bin/sh runpy.sh
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
