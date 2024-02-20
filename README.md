# bee-health-calculation-model-bgood-wp2
Bee health calculation model B-GOOD WP2
This code was developed by Luke Chamberlain at Nottingham Trent University with the support of the B-GOOD project: https://b-good-project.eu/.

# Description
Calculates the cumulative weight anomaly based on input weight data of two or more hives in JSON array format. Returns the first principal component score of each hive.
A principal component analysis is done on the normalized cumulative sum of the daily mean weight of each hive.

## Running the model
### 1. Install dependencies
- Python3: https://www.python.org/downloads/
- Numpy: https://numpy.org/
- Pandas: https://pypi.org/project/pandas/
- Scipy: https://scipy.org/
### 2. Run the model
```
python3
```
```json
data=[
    {
    "time": "2023-11-16T00:00:00Z",
    "weight_1": 54.166666666666666,
    "weight_2": 52.125,
    "weight_3": 51.125
    },
    {
    "time": "2023-11-16T00:13:55Z",
    "weight_1": 46.166666666666666,
    "weight_3": 53.125
    },
    {
    "time": "2023-11-16T02:11:10Z",
    "weight_1": 43.446666666666666,
    "weight_2": 50.125
    }
]
```
```
cumulative_weight_anomaly(data)
```

# Author
Luke Chamberlain
luke.chamberlain@ntu.ac.uk

# Input data
## Measurement
- net_weight_kg (weight excluding beekeeper actions)
- cumulative weight per day (set to 0 at midnight)

## Data interval
- 15 min average

## Data period
- relative interval of 7 * 24 hours

## Data items
- all hives of the apiary as a single data stream

# Output data
- PCA of data (https://github.com/laxip/PCAphp)
- deviation of comparison of each hive feature
