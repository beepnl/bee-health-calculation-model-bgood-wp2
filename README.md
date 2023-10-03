# bee-health-calculation-model-bgood-wp2
Bee health calculation model B-GOOD WP2

# Auhor
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
