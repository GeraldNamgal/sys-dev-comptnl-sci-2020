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
        self.days_out = 0

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
        self.days_out = day
        trials_list = []
        for trial in range(trials):
            weather_list = []
            for day in iter(self):
                # TODO
                self._simulate_weather_for_day(day)
            trials_list.append(weather_list)
        # TODO: Need to reset self.days_out or no need?

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
        if self.markov.current_day > self.markov.days_out:
            # TODO: Reset current_day and current_day_weather to 0 and day zero weather here?
            raise StopIteration()
        row = self.markov.mappings.get(self.markov.current_day_weather)  # TODO: Row should be current day
        col = random.choices(self.number_list, tuple(self.markov.data[row]))
        self.markov.current_day += 1
        self.markov.current_day_weather = col
        return self.markov.data[row][col]

    def __iter__(self):
        self
