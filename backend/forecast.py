import numpy as np
from sklearn.linear_model import LinearRegression

def forecast_cpu(history):
    # If not enough data, return last known or 0
    if len(history) < 2:
        return round(history[-1], 2) if history else 0

    X = np.arange(len(history)).reshape(-1, 1)
    y = np.array(history)

    model = LinearRegression()
    model.fit(X, y)

    future_step = [[len(history) + 5]]
    return round(float(model.predict(future_step)[0]), 2)
