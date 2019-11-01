import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error


class LinearModel:

    def __init__(self):
        # Learning rate
        self.l_rate = 0.0001

        # Iterations
        self.iterations = 1500

    def SplitData(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        return X_train.T, y_train.T, X_test.T, y_test.T

    def sigmoid(self, Z):
        A = 1 / (1 + (np.exp(-Z)))
        return A

    def initialize_with_zeros(self, dim):
        w = np.zeros((dim, 1))
        b = 0
        return w, b

    def propagate(self, w, b, X, Y):
        m = X.shape[1]

        # forward propogation
        A = self.sigmoid(np.dot(w.T, X) + b)
        cost = (- 1 / m) * np.sum(Y * np.log(A) + (1 - Y) * (np.log(1 - A)))

        # backward propogation
        dw = (1 / m) * np.dot(X, (A - Y).T)
        db = (1 / m) * np.sum(A - Y)

        grads = {
            'dw': dw,
            'db': db
        }

        return grads, cost

    def optimize(self,w, b, X, Y, num_iterations, learning_rate):

        costs = []

        for i in range(num_iterations):
            # Cost and gradient calculation
            grads, cost = self.propagate(w, b, X, Y)

            # Retrieve derivatives from grads
            dw = grads["dw"]
            db = grads["db"]

            # update parameters
            w = w - learning_rate * dw
            b = b - learning_rate * db

            costs.append(cost)

        params = {"w": w,
                  "b": b}

        grads = {"dw": dw,
                 "db": db}

        return params, grads, costs

    def model(self, X_train, y_train, X_test, y_test):

        w, b = self.initialize_with_zeros(X_train.shape[0])

        params, grads, costs = self.optimize(w, b, X_train, y_train, self.iterations, self.l_rate)

        w = params["w"]
        b = params["b"]

        d = {"costs": costs,
             "w": w,
             "b": b}

        return d

    def predict(self, w, b, test):
        val = self.sigmoid(np.dot(w.T, test) + b)
        y_predictions = np.round(val)
        return y_predictions

    def error_rate(self, y_test, y_predictions):
        mae = mean_absolute_error(y_predictions, y_test)
        mse = mean_squared_error(y_predictions, y_test)
        rmse = np.sqrt(mean_absolute_error(y_predictions, y_test))
        return mae, mse, rmse

    def plot_graph(self, cost_list):
        plt.figure(figsize=(7, 8))
        plt.plot(range(self.iterations), cost_list)
        plt.xlabel('Number of Iterations', fontsize=15)
        plt.ylabel('Cost', fontsize=15)
        plt.title('Cost Vs Iterations', fontsize=15, pad=15)
        plt.show()


def main():
    data = pd.read_csv('/Users/ankusmanish/Desktop/single1.csv')

    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    y = np.reshape(y, (len(y), 1))

    L_M = LinearModel()
    X_train, y_train, X_test, y_test = L_M.SplitData(X, y)
    d = L_M.model(X_train, y_train, X_test, y_test)
    y_predictions = L_M.predict(d['w'], d['b'], X_test)
    mae, mse, rmse = L_M.error_rate(y_test, y_predictions)
    L_M.plot_graph(d['costs'])

    print('Parameter values are : ')
    print('W : {}'.format(d['w']))
    print('b : {}'.format(d['b']))
    print('Mean absolute error : {}'.format(mae))
    print('Mean squared error : {}'.format(mse))
    print('Root mean squared error : {}'.format(rmse))


if __name__ == '__main__':
    main()

