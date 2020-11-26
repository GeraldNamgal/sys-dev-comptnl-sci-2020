#!/usr/bin/env python3

import numpy as np
import random


class Markov:
    mappings = {'sunny': 0, 'cloudy': 1, 'rainy': 2, 'snowy': 3, 'windy': 4,
                'hailing': 5}

    def __init__(self, day_zero_weather=None):
        self.data = []
        self.day_zero_weather = day_zero_weather
        self._current_day = 0
        self._current_day_weather = day_zero_weather

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

    # TODO: Supposed to be instance method (no self in HW instructions)?
    def get_weather_for_day(self, day, trials=3):  # TODO: trials default ok?
        trials_list = []
        for trial in range(trials):
            for day in range(1, day):
                self._simulate_weather_for_day(day)

    # TODO: Supposed to be instance method (no self in HW instructions)?
    def _simulate_weather_for_day(self, day):
        pass

    def __iter__(self):
        return MarkovIterator(self)

    @property
    def current_day(self):
        return self._current_day

    @current_day.setter
    def current_day(self, into):
        self._current_day = into

    @property
    def current_day_weather(self):
        return self._current_day_weather

    @current_day_weather.setter
    def current_day_weather(self, into):
        self._current_day_weather = into


# Referenced https://pynative.com/python-weighted-random-choices-with-probability/
class MarkovIterator:
    def __init__(self, markov):
        self.markov = markov
        self.number_list = []
        for key, val in markov.mappings:
            self.number_list.append(val)

    def __next__(self):
        row = 1  # TODO: Row should be current day
        col = random.choices(self.number_list, tuple(self.markov.data[row]))
        return self.markov.data[row][col]

    def __iter__(self):
        self
