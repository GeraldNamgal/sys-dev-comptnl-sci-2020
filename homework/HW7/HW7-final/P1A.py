#!/usr/bin/env python3

from Markov import *

# Demo of Markov class
weather_today = Markov()
weather_today.load_data(file_path='./weather.csv')
# print(weather_today.get_prob('sunny', 'cloudy'))  # This line should print 0.3
print(weather_today.get_prob('cloudy', 'windy'))  # This line should print 0.08
