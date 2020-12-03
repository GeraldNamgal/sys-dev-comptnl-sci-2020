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
               value BLOB)''')  # TODO: BLOB sensible here? -Johnathan said use text cause values get jumbled
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

    # Note: X_train.columns can also be used instead of data.feature_names
    for name, num in zip(data.feature_names, model.coef_[0]):
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


# Model 1

# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

# Fit model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)

save_to_database(1, 'Baseline model', db, baseline_model,
                 X_train, X_test, y_train, y_test)

# Model 2

feature_cols = ['mean radius',
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]

reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)

save_to_database(2, 'Reduced model', db, reduced_model,
                 X_train_reduced, X_test_reduced, y_train, y_test)

# Model 3

penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)

save_to_database(3, 'L1 penalty model', db, penalized_model,
                 X_train, X_test, y_train, y_test)

# Part C
high_scorer = '''SELECT id, test_score FROM model_results WHERE test_score =
            (SELECT MAX(test_score) FROM model_results)'''
cursor.execute(high_scorer)
tuple = cursor.fetchall()[0]
id_best = tuple[0]
score_best = tuple[1]
print(f'Best model id: {id_best}\nBest validation score: {score_best}')
print('\nBest model\'s features\n---------------------')
features_best = f'''SELECT feature_name, value FROM model_coefs
                    WHERE id = {id_best}'''
cursor.execute(features_best)
features_list = cursor.fetchall()
for feature, val in features_list:
    print(f'{feature}: {val}')

test_model = LogisticRegression(solver='liblinear')
test_model.fit(X_train, y_train)

# Manually change fit parameters
intercept = features_list[0][1]
coef = []
for feature in features_list[1:]:
    coef.append(feature[1])
test_model.coef_ = np.array([coef])
test_model.intercept_ = np.array([intercept])
print()

test_score = test_model.score(X_test, y_test)
print(f'Reproduced best validation score: {test_score}')

# # TODO: Debugging -- View the tables
# cursor.execute("SELECT * FROM model_params")
# for row in cursor.fetchall():
#     print(row)
# cursor.execute("SELECT * FROM model_coefs")
# for row in cursor.fetchall():
#     print(row)
# cursor.execute("SELECT * FROM model_results")
# for row in cursor.fetchall():
#     print(row)

db.commit()
db.close()


# References
# https://datascience.stackexchange.com/questions/29131/feature-names-in-logisticregression
# https://stackoverflow.com/questions/57924484/finding-coefficients-for-logistic-regression-in-python
