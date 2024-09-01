from sklearn.preprocessing import StandardScaler

def normalize(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data

def moving_average(data, window):
    return data.rolling(window).mean()