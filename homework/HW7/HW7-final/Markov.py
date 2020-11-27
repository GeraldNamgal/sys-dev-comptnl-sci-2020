#!/usr/bin/env python3

import numpy as np
import random
from collections import OrderedDict


class Markov:
    mappings = OrderedDict([('sunny', 0), ('cloudy', 1), ('rainy', 2),
                            ('snowy', 3), ('windy', 4), ('hailing', 5)])

    @staticmethod
    def validate_weather(weather):
        try:
            if type(weather) != str:
                raise ValueError('Invalid weather type entered')
            weather = weather.lower()
            if weather not in Markov.mappings:
                raise ValueError('Invalid weather type entered')
            return weather
        except Exception:
            raise

    def __init__(self, day_zero_weather=None):
        self.data = []
        self._current_day = 0
        self.day_zero_weather = day_zero_weather
        self._current_day_weather = day_zero_weather
        if day_zero_weather:
            day_zero_weather = Markov.validate_weather(day_zero_weather)
            self.day_zero_weather = day_zero_weather
            self._current_day_weather = day_zero_weather
        self.days_out = None        # Helper attribute

    # Referenced https://janakiev.com/blog/csv-in-python/
    def load_data(self, file_path='./weather.csv'):
        self.data = np.genfromtxt(file_path, delimiter=",")

    def get_prob(self, current_day_weather, next_day_weather):
        current_day_weather = Markov.validate_weather(current_day_weather)
        next_day_weather = Markov.validate_weather(next_day_weather)
        row = Markov.mappings[current_day_weather]
        col = Markov.mappings[next_day_weather]
        return self.data[row][col]

    # TODO: Supposed to be instance method (no self in HW instructions)?
    def get_weather_for_day(self, day, trials=1):  # TODO: trials default sensible?
        trials_list = []
        for trial in range(trials):
            trials_list.append(self._simulate_weather_for_day(day))
        return trials_list

    # TODO: Supposed to be instance method (no self in HW instructions)?
    def _simulate_weather_for_day(self, day):
        self.days_out = day
        predicted_weather = None
        for day in self:
            # print(day)  # Debugging
            predicted_weather = day
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
            odds_row = Markov.mappings[self.markov.current_day_weather]
            next_day_weather = random.choices(list(Markov.mappings.keys()),
                                              self.markov.data[odds_row])[0]
        self.markov.current_day += 1
        self.markov.current_day_weather = next_day_weather
        return next_day_weather

    def __iter__(self):
        self

# # Debugging
# example = Markov('ClOudy')
# example.load_data(file_path='./weather.csv')
# # print(example.get_prob('sunny', 'clOudy'))  # This line should print 0.3
# # print(example.get_prob('clouDy', 'windy'))  # This line should print 0.08
# trials_list = example.get_weather_for_day(2, 7)
