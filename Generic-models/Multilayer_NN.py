import pandas as pd
import warnings
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

warnings.filterwarnings('ignore')


class LinearModel:

    def __init__(self):
        # Learning rate
        self.l_rate = 0.001

        # Iterations
        self.iterations = 5000

    def SplitData(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        return X_train.T, y_train.T, X_test.T, y_test.T

    def sigmoid(self, Z):
        A = 1 / (1 + (np.exp(-Z)))
        return A

    def layer_sizes(self, X, Y):
        n_x1 = X.shape[0]  # size of input layer
        n_h1 = 4  # size of nodes in 1st layer
        n_x2 = 4  # size of the input from 1st hidden layer
        n_h2 = 3  # number of nodes in 2nd layer
        n_y = Y.shape[0]  # size of output layer

        return (n_x1, n_x2, n_h1, n_h2, n_y)

    def initialize_parameters(self, n_x1, n_x2, n_h1, n_h2, n_y):
        np.random.seed(2)

        W1 = np.random.randn(n_h1, n_x1) * 0.01
        b1 = np.zeros((n_h1, 1))
        W2 = np.random.randn(n_h2, n_x2) * 0.01
        b2 = np.zeros((n_h2, 1))
        W3 = np.random.randn(n_y, n_h2) * 0.01
        b3 = np.zeros((n_y, 1))

        parameters = {"W1": W1,
                      "b1": b1,
                      "W2": W2,
                      "b2": b2,
                      "W3": W3,
                      "b3": b3}

        return parameters

    def forward_propagation(self, X, parameters):
        W1 = parameters['W1']
        b1 = parameters['b1']
        W2 = parameters['W2']
        b2 = parameters['b2']
        W3 = parameters['W3']
        b3 = parameters['b3']

        # forward propogation
        Z1 = np.dot(W1, X) + b1
        A1 = np.tanh(Z1)
        Z2 = np.dot(W2, A1) + b2
        A2 = self.sigmoid(Z2)
        Z3 = np.dot(W3, A2) + b3
        A3 = self.sigmoid(Z3)

        cache = {"Z1": Z1,
                 "A1": A1,
                 "Z2": Z2,
                 "A2": A2,
                 "Z3": Z3,
                 "A3": A3}

        return A3, cache

    def compute_cost(self, A3, Y, parameters):
        m = Y.shape[1]

        cost = -(np.sum(np.multiply(np.log(A3), Y) + np.multiply((1 - Y), np.log(1 - A3)))) / m

        return cost

    def backward_propagation(self, parameters, cache, X, Y):
        m = X.shape[1]

        W1 = parameters['W1']
        W2 = parameters['W2']
        W3 = parameters['W3']

        A1 = cache['A1']
        A2 = cache['A2']
        A3 = cache['A3']

        # backward propagation: calculate dW1, db1, dW2, db2, dW3, db3
        dZ3 = A3 - Y
        dW3 = (1 / m) * np.dot(dZ3, A2.T)
        db3 = (1 / m) * np.sum(dZ3, axis=1, keepdims=True)

        dZ2 = A2 - Y
        dW2 = (1 / m) * np.dot(dZ2, A1.T)
        db2 = (1 / m) * np.sum(dZ2, axis=1, keepdims=True)
        dZ1 = np.multiply(np.dot(W2.T, dZ2), 1 - np.power(A1, 2))
        # dZ1 = A1 - Y
        dW1 = (1 / m) * np.dot(dZ1, X.T)
        db1 = (1 / m) * np.sum(dZ1, axis=1, keepdims=True)

        grads = {"dW1": dW1,
                 "db1": db1,
                 "dW2": dW2,
                 "db2": db2,
                 "dW3": dW3,
                 "db3": db3}

        return grads

    def update_parameters(self, parameters, grads):
        W1 = parameters['W1']
        b1 = parameters['b1']
        W2 = parameters['W2']
        b2 = parameters['b2']
        W3 = parameters['W3']
        b3 = parameters['b3']

        dW1 = grads['dW1']
        db1 = grads['db1']
        dW2 = grads['dW2']
        db2 = grads['db2']
        dW3 = grads['dW3']
        db3 = grads['db3']

        # Update parameters
        W1 = W1 - self.l_rate * dW1
        b1 = b1 - self.l_rate * db1
        W2 = W2 - self.l_rate * dW2
        b2 = b2 - self.l_rate * db2
        W3 = W3 - self.l_rate * dW3
        b3 = b3 - self.l_rate * db3

        parameters = {"W1": W1,
                      "b1": b1,
                      "W2": W2,
                      "b2": b2,
                      "W3": W3,
                      "b3": b3}

        return parameters

    def nn_model(self, X, Y):
        cost_lis = []
        np.random.seed(3)
        n_x1 = self.layer_sizes(X, Y)[0]
        n_x2 = self.layer_sizes(X, Y)[1]
        n_h1 = self.layer_sizes(X, Y)[2]
        n_h2 = self.layer_sizes(X, Y)[3]
        n_y = self.layer_sizes(X, Y)[-1]

        parameters = self.initialize_parameters(n_x1, n_x2, n_h1, n_h2, n_y)
        W1 = parameters['W1']
        b1 = parameters['b1']
        W2 = parameters['W2']
        b2 = parameters['b2']
        W3 = parameters['W3']
        b3 = parameters['b3']

        # gradient descent

        for i in range(0, self.iterations):
            A3, cache = self.forward_propagation(X, parameters)

            cost = self.compute_cost(A3, Y, parameters)
            cost_lis.append(cost)

            grads = self.backward_propagation(parameters, cache, X, Y)

            parameters = self.update_parameters(parameters, grads)

        return parameters, cost_lis

    def predict(self, X, parameters):
        A3, cache = self.forward_propagation(X, parameters)
        y_predictions = np.round(A3)
        return y_predictions

    def classification_metrics(self, y_predictions, y_test):
        report = classification_report(y_predictions.T, y_test.T)
        score = accuracy_score(y_predictions.T, y_test.T)
        return report, score

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
    parameters, cost_lis = L_M.nn_model(X_train, y_train)
    y_predictions = L_M.predict(X_test, parameters)

    report, score = L_M.classification_metrics(y_predictions, y_test)
    print('Evaluation metrics are :')
    print('\n Classification Report : \n {}'.format(report))
    print('\n Accuracy Score : \n {}'.format(score * 100))

    L_M.plot_graph(cost_lis)


if __name__ == '__main__':
    main()
