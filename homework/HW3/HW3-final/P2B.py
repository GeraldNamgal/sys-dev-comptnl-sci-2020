#!/usr/bin/env python3

from regression.Regression import Regression as RegressionAlias
import types

# Get and print all the functions of the Regression class
attributes = dir(RegressionAlias)
print("Functions in Regression class:")
for attribute in attributes:
    if isinstance(getattr(RegressionAlias, attribute), types.FunctionType):
        print(attribute)


# References:
# - https://stackoverflow.com/questions/1091259/how-to-test-if-a-class-attribute-is-an-instance-method
