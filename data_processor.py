from sklearn.preprocessing import StandardScaler

def normalize(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data

def moving_average(data, window):
    return data.rolling(window).mean()

def moving_std(data, window):
    return data.rolling(window).std()

def cumulative_average(data):
    return data.expanding().mean()

def exponential_moving_average(data, span):
    return data.ewm(span).mean()

def bollinger(data, window):
    result = data.copy()
    for col_name, col_data in result.items():
        result[f"{col_name} - Middle band"] = col_data.rolling(window).mean()
        result[f"{col_name} - Lower band"] = col_data.rolling(window).mean() - col_data.rolling(window).std()
        result[f"{col_name} - Upper band"] = col_data.rolling(window).mean() + col_data.rolling(window).std()
    return result