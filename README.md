## How to Use

### Run
```bash
python3 run.py [--<arg1>=<value1>] [--<arg2>=<value2>] ...
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
