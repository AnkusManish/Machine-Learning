#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:48:33 2019

@author: ankusmanish
"""

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
        self.iterations = 10000

    def SplitData(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        return X_train, y_train, X_test, y_test

    def Model(self, X_train, y_train):
        parameters = np.array([0, 1], dtype='d')

        # length of the data
        l = X_train.shape[0]

        for i in range(self.iterations):
            y_pred = parameters[0] + (parameters[1] * X_train)
            parameters[0] = parameters[0] - (self.l_rate * ((1 / l) * sum(y_pred - y_train)))
            parameters[1] = parameters[1] - (self.l_rate * ((1 / l) * (sum((y_pred - y_train) * X_train))))
        return parameters

    def predictions(self, X_test, parameters):
        y_predictions = parameters[0] + (parameters[1] * X_test)
        return y_predictions

    def error_rate(self, y_test, y_predictions):
        mae = mean_absolute_error(y_predictions, y_test)
        mse = mean_squared_error(y_predictions, y_test)
        rmse = np.sqrt(mean_absolute_error(y_predictions, y_test))
        return mae, mse, rmse

    def plot(self, X_test, y_test, y_predictions):
        plt.figure(figsize=(9, 9))
        plt.scatter(X_test, y_test, s=40, c='r', marker='*')
        plt.plot(X_test, y_predictions, c='b')
        plt.show()


def main():
    data = pd.read_csv('/Users/ankusmanish/Desktop/simple_linear.csv')

    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    y = np.reshape(y, (len(y), 1))

    L_M = LinearModel()

    X_train, y_train, X_test, y_test = L_M.SplitData(X, y)
    parameters = L_M.Model(X_train, y_train)
    y_predictions = L_M.predictions(X_test, parameters)
    mae, mse, rmse = L_M.error_rate(y_test, y_predictions)
    L_M.plot(X_test, y_test, y_predictions)

    print(parameters)
    print('Mean absolute error : {}'.format(mae))
    print('Mean squared error : {}'.format(mse))
    print('Root mean squared error : {}'.format(rmse))


if __name__ == '__main__':
    main()

