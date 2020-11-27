#!/usr/bin/env python3

import numpy as np
import random
from collections import OrderedDict


class Markov:
    mappings = OrderedDict([('sunny', 0), ('cloudy', 1), ('rainy', 2),
                            ('snowy', 3), ('windy', 4), ('hailing', 5)])

    def __init__(self, day_zero_weather=None):
        self.data = []
        self._current_day_weather = None
        if type(day_zero_weather) == str:
            self.day_zero_weather = day_zero_weather.lower()
            self._current_day_weather = day_zero_weather.lower()
        self._current_day = 0
        self.days_out = None        # Helper attribute

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
    def get_weather_for_day(self, day, trials=3):  # TODO: trials default sensible?
        trials_list = []
        for trial in range(trials):
            trials_list.append(self._simulate_weather_for_day(day))

        print(trials_list)  # TODO: Debugging

    # TODO: Supposed to be instance method (no self in HW instructions)?
    def _simulate_weather_for_day(self, day):
        self.days_out = day
        predicted_weather = None

        for day in self:
            print(day)  # TODO: Debugging
            predicted_weather = day

        print()  # TODO: Debugging

        return predicted_weather

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

    def __next__(self):
        if self.markov.current_day == 0 and self.markov.days_out == 0:
            next_day_weather = self.markov.current_day_weather
        elif self.markov.current_day >= self.markov.days_out:
            self.markov.current_day = 0
            self.markov.current_day_weather = self.markov.day_zero_weather
            raise StopIteration()
        else:
            odds_row = self.markov.mappings[self.markov.current_day_weather]
            # TODO: Check what random.choices is returning
            next_day_weather = random.choices(list(self.markov.mappings.keys()),
                                              self.markov.data[odds_row])[0]  # TODO: How to get value back not in array?
        self.markov.current_day += 1
        self.markov.current_day_weather = next_day_weather
        return next_day_weather

    def __iter__(self):
        self


# TODO: Debugging
example = Markov('SunNy')
example.load_data(file_path='./weather.csv')
print(example.get_prob('sunny', 'cloudy'))  # This line should print 0.3
example.get_weather_for_day(3, 2)
