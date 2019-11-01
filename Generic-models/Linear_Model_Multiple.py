#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:30:39 2019

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
        self.l_rate = 0.001

        # Iterations
        self.iterations = 3000

    def SplitData(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        return X_train, y_train, X_test, y_test

    def Model(self, X_train, y_train):
        np.random.seed(10)
        theta = np.random.rand(X_train.shape[1])
        theta = np.reshape(theta, (len(theta), 1))
        cost_list = []
        # length of the data
        l = X_train.shape[0]
        for i in range(self.iterations):
            y_pred = np.dot(X_train, theta)
            error = y_pred - y_train
            cost = np.dot(error.T, error) / (2 * l)
            # print(np.squeeze(cost))
            cost_list.append(np.squeeze(cost))
            theta = theta - ((self.l_rate * (1 / l) * np.dot(X_train.T, error)))
        return theta, cost_list

    def predictions(self, X_test, theta):
        y_predictions = np.dot(X_test, theta)
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
    data = pd.read_csv('/Users/ankusmanish/Desktop/multi_linear.csv')

    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    y = np.reshape(y, (len(y), 1))

    L_M = LinearModel()
    X_train, y_train, X_test, y_test = L_M.SplitData(X, y)
    theta, cost_list = L_M.Model(X_train, y_train)
    y_predictions = L_M.predictions(X_test, theta)
    mae, mse, rmse = L_M.error_rate(y_test, y_predictions)
    L_M.plot_graph(cost_list)

    print('Parameter values for different features : ')
    print(theta)
    print('Mean absolute error : {}'.format(mae))
    print('Mean squared error : {}'.format(mse))
    print('Root mean squared error : {}'.format(rmse))


if __name__ == '__main__':
    main()





