import numpy as np
import pandas as pd
from Errors import calculate_errors, add_error_columns
from MovingAverage import moving_average
from Regression import regression
from ExponentialSmoothing import expo_smooth
from pathlib import Path

def run(method, df, **kwargs):
    if ("Moving Average" == method):
        moving_average(df, kwargs['n'])

    elif ("Regression" == method):
        regression(df)
    
    elif ("Exponential Smoothing" == method):
        expo_smooth(df, kwargs['alpha'])

    add_error_columns(df)
    path = Path('out.csv')
    df.to_csv(path) 