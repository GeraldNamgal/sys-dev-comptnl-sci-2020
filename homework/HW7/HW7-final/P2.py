#!/usr/bin/env python3

import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer


db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
# cursor.execute('''CREATE TABLE model_params (
#                id INTEGER PRIMARY KEY NOT NULL,
#                desc TEXT,
#                param_name TEXT,
#                value REAL)''')
# cursor.execute('''CREATE TABLE model_coefs (
#                id INTEGER PRIMARY KEY NOT NULL,
#                desc TEXT,
#                feature_name TEXT,
#                value REAL)''')
# cursor.execute('''CREATE TABLE model_results (
#                id INTEGER PRIMARY KEY NOT NULL,
#                desc TEXT,
#                train_score REAL,
#                test_score REAL)''')
# db.commit()

# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

# Fit model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)


def save_to_database(model_id, model_desc, db, model,
                     X_train, X_test, y_train, y_test):
    pass


# TODO: Debugging
cursor.execute("SELECT * FROM model_params")
all_rows = cursor.fetchall()
print(all_rows)
cursor.execute("SELECT * FROM model_coefs")
all_rows = cursor.fetchall()
print(all_rows)
cursor.execute("SELECT * FROM model_results")
all_rows = cursor.fetchall()
print(all_rows)

print("params: ", baseline_model.get_params())
print(X_train.columns)
print(X_test.columns)
print(baseline_model.coef_)  # https://stackoverflow.com/questions/57924484/finding-coefficients-for-logistic-regression-in-python
print(baseline_model.intercept_)
print(baseline_model.score(X_train, y_train))
print(baseline_model.score(X_test, y_test))
