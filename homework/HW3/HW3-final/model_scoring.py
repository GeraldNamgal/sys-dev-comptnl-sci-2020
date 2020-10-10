#!/usr/bin/env python3

from sklearn import datasets
from sklearn.model_selection import train_test_split
import regression.Regression as RegressionAlias


# Get Boston data
dataset = datasets.load_boston()

# Train-test split the data
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)

# Score the models
alpha = 0.1
models = [RegressionAlias.LinearRegression(alpha)]
for model in models:
    model.fit(X_train, y_train)
