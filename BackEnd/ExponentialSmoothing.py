# import pandas as pd

def expo_smooth(df, column_name, alpha, start):
    # Setup first row
    df[column_name] = 0
    df[column_name][start] = df['Demand'][start]

    # Assign values to the rest of the rows
    for i in range(start + 1, len(df)):
        df[column_name][i] = round((alpha * df['Demand'][i - 1] + (1 - alpha) * df[column_name][i - 1]), 0)

# expo_smooth(pd.read_csv("BackEnd/Sample-Data.csv", index_col="Period"), alpha=0.2)