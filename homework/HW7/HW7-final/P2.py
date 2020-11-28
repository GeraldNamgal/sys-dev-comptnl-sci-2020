#!/usr/bin/env python3

import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer


db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")
# TODO: Should the tables have at least one NOT NULL column? --
cursor.execute('''CREATE TABLE model_params (
               id INTEGER,
               desc TEXT,
               param_name TEXT,
               value BLOB)''')  # TODO: BLOB sensible here?
cursor.execute('''CREATE TABLE model_coefs (
               id INTEGER,
               desc TEXT,
               feature_name TEXT,
               value REAL)''')
cursor.execute('''CREATE TABLE model_results (
               id INTEGER,
               desc TEXT,
               train_score REAL,
               test_score REAL)''')
db.commit()


def save_to_database(model_id, model_desc, db, model,
                     X_train, X_test, y_train, y_test):
    # Goes in model_params
    for key, val in model.get_params().items():
        cursor.execute('''INSERT INTO model_params
        (id, desc, param_name, value)
        VALUES (?, ?, ?, ?)''',
                       (model_id, model_desc, key, val))
        db.commit()

    # Goes in model_coefs
    # TODO: Handling intercept correctly?
    cursor.execute('''INSERT INTO model_coefs
    (id, desc, feature_name, value)
    VALUES (?, ?, ?, ?)''',
                   (model_id, model_desc, 'intercept', model.intercept_[0]))
    db.commit()
    for name, num in zip(X_train.columns, model.coef_[0]):
        cursor.execute('''INSERT INTO model_coefs
        (id, desc, feature_name, value)
        VALUES (?, ?, ?, ?)''',
                       (model_id, model_desc, name, num))
        db.commit()

    # Goes in model_results
    cursor.execute('''INSERT INTO model_results
        (id, desc, train_score, test_score)
        VALUES (?, ?, ?, ?)''',
                   (model_id, model_desc, model.score(X_train, y_train),
                    model.score(X_test, y_test)))
    db.commit()


# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

# Fit model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)

# TODO: Debugging...
save_to_database(1, 'Baseline model', db, baseline_model,
                 X_train, X_test, y_train, y_test)

cursor.execute("SELECT * FROM model_params")
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT * FROM model_coefs")
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT * FROM model_results")
for row in cursor.fetchall():
    print(row)


# Referenced:
# https://datascience.stackexchange.com/questions/29131/feature-names-in-logisticregression
# https://stackoverflow.com/questions/57924484/finding-coefficients-for-logistic-regression-in-python
