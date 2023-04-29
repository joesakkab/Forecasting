import numpy as np
import pandas as pd
from Errors import add_error_columns
from MovingAverage import moving_average
from Regression import regression
from ExponentialSmoothing import expo_smooth
from HoltsMethod import holts
from pathlib import Path

def run(method, df, **kwargs):
    if ("Moving Average" == method):
        moving_average(df, kwargs['n'])

    elif ("Regression" == method):
        regression(df)
    
    elif ("Exponential Smoothing" == method):
        expo_smooth(df, kwargs['column_name'], kwargs['alpha'], kwargs['start'])

    elif ("Holts Method" == method):
        holts(df, kwargs['alpha'], kwargs['beta'], kwargs['season'])

    add_error_columns(df)
    path = Path('out.csv')
    df.to_csv(path) 