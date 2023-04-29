def add_error_columns(df):
    # Add error columns
    df['|e|'] = abs(df['Demand'] - df['Forecast'])
    df['e^2'] = round(df['|e|'] ** 2, 0)
    df['%\e'] = round((df['|e|'] / df['Demand']) * 100, 0)

def calculate_errors(df):
    # Calculate error 
    mad = round(df['|e|'].mean(), 0)
    mse = round(df['e^2'].mean(), 0)
    mape = round(df['%\e'].mean(), 0)
    
    # Print errors
    print("MAD is", mad, "MSE is", mse, "MAPE is", mape)