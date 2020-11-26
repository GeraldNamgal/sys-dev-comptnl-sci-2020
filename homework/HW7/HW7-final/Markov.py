#!/usr/bin/env python3

import numpy as np


class Markov:
    def __init__(self):  # You will need to modify this header line later in Part C
        self.data = []

    # Referenced https://janakiev.com/blog/csv-in-python/
    def load_data(self, file_path='./weather.csv'):
        self.data = np.genfromtxt(file_path, delimiter=",")

    def get_prob(self, current_day_weather, next_day_weather):
        current_day_weather = current_day_weather.lower()
        next_day_weather = next_day_weather.lower()
        try:
            if current_day_weather not in self.mappings\
                    or next_day_weather not in self.mappings:
                raise ValueError('Invalid weather type entered')
        except Exception:
            raise
        return self.data[self.mappings[current_day_weather],
                         self.mappings[next_day_weather]]

    mappings = {'sunny': 0, 'cloudy': 1, 'rainy': 2, 'snowy': 3, 'windy': 4,
                'hailing': 5}
