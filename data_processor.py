from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

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

def create_sequences(data, time_step):
    X, y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 3]) # column index 3 in the closing price
        y.append(data[i + time_step, 3])
    return np.array(X), np.array(y)

def lstm_prediction(X, y):
    X = X.reshape((X.shape[0], X.shape[1], 1))
    y = y.reshape((y.shape[0], 1))

    

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')

    train_size = int(len(X) * 0.8)

    X_train, y_train = X[:train_size], y[:train_size]
    X_test, y_test = X[train_size:], y[train_size:]

    assert(not np.any(X_train == None))
    assert(not np.any(X_test == None))
    assert(not np.any(y_train == None))
    assert(not np.any(y_test == None))

    print(y.shape)
    print(X_test.shape)

    model.fit(X_train, y_train, epochs=20, batch_size=32)
    model.evaluate(X_test, y_test)
    return model.predict(X_test)
