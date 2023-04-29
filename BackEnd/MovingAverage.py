# Method that returns the moving average of demand
def moving_average(df, window_size):
    # Get only demand column
    data = df.loc[:, 'Demand'].astype(float)

    # Get the window of series of observations of specified window size
    windows = data.rolling(window_size)

    # Create a series of moving averages of each window and round
    moving_averages = windows.mean().round(2)
    df['Forecast'] = moving_averages