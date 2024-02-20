import json
import numpy as np
import pandas as pd
import scipy


def calculate_cumulative_weight_anomaly(input):
    # sort dataframe time-descending
    weights = pd.DataFrame(input)

    weights['time'] = pd.to_datetime(weights['time'])
    dfsorted = weights.sort_values(by='time', ascending=False)

    # hourly weight average 
    df = dfsorted.groupby(pd.Grouper(key='time', freq='h'), group_keys=True).mean()
    
    # fill missing values with nearest-neighbor interpolation
    df.interpolate(method='nearest', inplace=True)

    # cumulative sum of daily mean weight (reset at midnight) 
    df = df.groupby(pd.Grouper(freq='d')).cumsum()

    # normalize
    df -= df.mean()
    df /= df.std()
    dfnorm = (df - df.min())/(df.max() - df.min())
    A = dfnorm.to_numpy()

    # PCA
    D, V = np.linalg.eig(np.dot(A, A.T))
    idx = np.flip(D.argsort())
    V = V[:,idx]
    scores = np.abs((V @ A))  

    # extract scores
    dfscores = pd.DataFrame(scores)
    outputdf = pd.DataFrame(dfscores.iloc[0], columns=["Hive","Score"])
    outputdf["Score"] = dfscores.iloc[0]
    outputdf["Hive"] = outputdf.index+1

    # output scores as JSON
    #       [{
    #           "Hive": 1,
    #           "Score": 2.0646592326
    #       },
    #       {
    #           "Hive": 2,
    #           "Score": 2.2899991715
    #       }]

    outputJSONstr = outputdf.to_json(orient="records")
    outputJSON = json.loads(outputJSONstr)
    return outputJSON