# Uses linear regression to forecast demand
def regression(df):
    # Get number of rows
    n = len(df['Demand'])

    # Add rows to calcalate i*D_i
    df['i'] = range(1, len(df['Demand']) + 1)
    df['i*D_i'] = (df['Demand'] * df['i']).astype(float)

    # Calculate relevent values and variables
    sum_D = df['Demand'].sum()
    sum_iDi = df['i*D_i'].sum()
    s_xy = n*sum_iDi - (n * (n + 1) / 2) * sum_D
    s_xx = ((n ** 2) * (n + 1) * (2 * n + 1)) / 6 - (n ** 2 * (n + 1) ** 2) / 4
    b = s_xy / s_xx
    a = (sum_D / n) - (b * (n + 1)) / 2

    # Assign forecast to forecast column
    df['Forecast'] = a + b * df['i']
    return a, b