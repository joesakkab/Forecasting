from Regression import regression
from ExponentialSmoothing import expo_smooth
import numpy as np
def holts(df, alpha, beta, season):
    # Get values of a and b from regression 
    a, b = regression(df)

    # Setup first value of S_t
    df['S_t'] = 0
    df['S_t'][season - 1] = a + b * (season - 1)

    # Setup first vale of G_t
    df['G_t'] = 0
    df['G_t'][season - 1] = b

    # Assign the rest of the values
    for i in range(season, len(df)):
        df['S_t'][i] = alpha * df['Demand'][i] + (1 - alpha) * (df['S_t'][i - 1] + df['G_t'][i - 1])

        df['G_t'][i] = beta * (df['S_t'][i] - df['S_t'][i - 1]) + (1 - beta) * df['G_t'][i - 1]

    # Assign forecast values
    df['Forecast'] = df['S_t'] + df['G_t']

    # Replace 0 values with NaN
    df['S_t'] = df['S_t'].replace({0:np.nan})
    df['G_t'] = df['G_t'].replace({0:np.nan})