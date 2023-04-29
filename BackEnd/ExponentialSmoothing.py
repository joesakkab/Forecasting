# import pandas as pd

def expo_smooth(df, alpha):
    # Setup first row
    df['Forecast'] = 0
    df['Forecast'][0] = df['Demand'][0]
    # print(df)
    for i in range(1, len(df)):
        df['Forecast'][i] = round((alpha * df['Demand'][i - 1] + (1 - alpha) * df['Forecast'][i - 1]), 0)
    #     df['Forecast'] = alpha * df['Demand'].shift(1) - (1 - alpha) * df['Forecast'].shift(1)
        # pass
    # print(df)

# expo_smooth(pd.read_csv("BackEnd/Sample-Data.csv", index_col="Period"), alpha=0.2)