import numpy as np
import pandas as pd

# Define variable for file name 
sample_data = "BackEnd\Sample-Data.csv"

# Convert file to dataframe
df = pd.read_csv(sample_data)

print(df)

# data = []
# with open(sample_data, 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         data.append(row[1])

# print(data)