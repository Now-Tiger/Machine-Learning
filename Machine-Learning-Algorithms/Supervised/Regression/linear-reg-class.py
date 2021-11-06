#!/usr/bin/env python3


import numpy as np
from numpy.core.fromnumeric import size
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from warnings import filterwarnings
filterwarnings('ignore')

class LinearRegression (object) :
    def fit(self, X, y, intercept = False) :
        if intercept == False :
            ones = np.ones(len(X)).reshape(len(X), 1)
            X = np.concatenate((ones, X), axis = 1)
        self.X = np.array(X)
        self.y = np.array(y)
        self.N, self.D = self.X.shape

        # ------------- estimate parameters -----------------
        XtX = np.dot(self.X.T, self.X)
        XtX_inverse = np.linalg.inv(XtX)
        Xty = np.dot(self.X.T, self.y)
        self.beta_hats = np.dot(XtX_inverse, Xty)

        # ------------ in-sample prediction -----------------
        self.y_hat = np.dot(self.X, self.beta_hats)

        # -------------- Calculate Loss ---------------------
        self.L = .5 * np.sum((self.y - self.y_hat)**2)

    def predict(self, X_test, intercept = True) :
        self.y_test_hat = np.dot(X_test, self.beta_hats)    


# ----------------------- Load data ----------------------------

data = load_boston()
X = data['data']
y = data['target']
model = LinearRegression()
model.fit(X, y, intercept = False)

plt.style.use('seaborn-whitegrid')
plt.figure(figsize = (12, 6), dpi = 80)
sns.scatterplot(model.y, model.y_hat, color = 'green' )
plt.xlabel(r'$y$', size = 16)
plt.ylabel(r'$\hat{y}$', rotation = 0, size = 16, labelpad = 15)
plt.title(r'$y$ vs. $\hat{y}$', size = 20, pad = 10)
plt.show()

