#!/usr/bin/env python3

from sklearn import datasets
from sklearn.model_selection import train_test_split
import regression.Regression as RegrModuleAlias


dataset = datasets.load_boston()           # Get Boston data

# Do train-test split on the data...
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)

# Score the models...
alpha = 0.1
models = [RegrModuleAlias.LinearRegression(alpha),
          RegrModuleAlias.RidgeRegression(alpha)]
high_score = 0                             # Initialize high_score
model_idx = None                           # Index of model (for highest scorer)
for idx, model in enumerate(models):
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(type(model).__name__, "model's R-squared score is:", score)
    if score > high_score:                 # Is the current highest score?
        high_score = score
        model_idx = idx
if high_score > 0:                         # If highest score is > 0
    high_scorer = models[model_idx]
    print(f'The parameters for the best model ({type(high_scorer).__name__}) are:')
    for key, val in high_scorer.get_params().items():
        print(f"'{key}' = {val}")


# References:
# - https://www.codegrepper.com/code-examples/delphi/python+return+index+in+for+loop
