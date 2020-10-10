#!/usr/bin/env python3

from sklearn import datasets
from sklearn.model_selection import train_test_split
import regression.Regression as RegrModuleAlias
from matplotlib import pyplot as plt


dataset = datasets.load_boston()                               # Get Boston data

# Do train-test split on the data...
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)

# Score the models...
alpha = .1
linear_regr = RegrModuleAlias.LinearRegression(alpha)  # Instantiate linea model
ridge_regr = RegrModuleAlias.RidgeRegression(alpha)    # Instantiate ridge model
linear_scores = []
ridge_scores = []
ridge_alphas = [.01, 1.12, 2.23, 3.34, 4.45, 5.56, 6.67, 7.78, 8.89, 10]
linear_regr.fit(X_train, y_train)                # Fit and score linear model...
linear_score = linear_regr.score(X_test, y_test)
for alpha in ridge_alphas:                        # Fit and score ridge model...
    ridge_regr.set_params(alpha=alpha)
    ridge_regr.fit(X_train, y_train)
    ridge_scores.append(ridge_regr.score(X_test, y_test))       # Save scores...
    linear_scores.append(linear_score)      # (Linear model's score is constant)

# Plot the results (R-squared scores vs. alphas)
plt.plot(ridge_alphas, linear_scores, label='Linear Model')
plt.plot(ridge_alphas, ridge_scores, label='Ridge Model')
plt.title('R-squared Scores Vs. Alphas of Regression Models')
plt.xlabel('alpha')
plt.ylabel('R-squared score')
plt.legend()
plt.show()

# References
# - https://howtothink.readthedocs.io/en/latest/PvL_H.html
