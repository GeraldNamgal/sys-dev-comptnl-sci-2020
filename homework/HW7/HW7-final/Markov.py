#!/usr/bin/env python3

import numpy as np
import random


class Markov:
    mappings = {'sunny': 0, 'cloudy': 1, 'rainy': 2, 'snowy': 3, 'windy': 4,
                'hailing': 5}

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
        row = self.mappings[current_day_weather]
        col = self.mappings[next_day_weather]
        return self.data[row][col]

    def __iter__(self):
        return MarkovIterator(self)


# Referenced https://pynative.com/python-weighted-random-choices-with-probability/
class MarkovIterator:
    def __init__(self, markov):
        self.markov = markov
        self.number_list = []
        for key, val in self.markov.mappings:
            self.number_list.append(val)

    def __next__(self):
        row = 1  # TODO: Row should be current day
        col = random.choices(self.number_list, tuple(self.markov.data[row]))
        return self.markov.data[row][col]

    def __iter__(self):
        self
