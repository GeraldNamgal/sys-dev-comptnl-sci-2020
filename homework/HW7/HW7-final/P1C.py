#!/usr/bin/env python3

from Markov import *
from collections import Counter
from statistics import mode


city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

occurrences_dict = {}
modes_dict = {}

for city, init_weather in city_weather.items():
    weather_markov = Markov(init_weather)
    weather_markov.load_data(file_path='./weather.csv')
    trials_list = weather_markov.get_weather_for_day(7, 100)
    counter = Counter(trials_list)
    weather_dict = {}
    for key, value in counter.items():
        weather_dict[key] = value
    # # Debugging
    # print(weather_dict)
    # print(mode(trials_list))
    # print()
    occurrences_dict[city] = weather_dict
    modes_dict[city] = mode(trials_list)

# Demo
for city, occurrences in occurrences_dict.items():
    print(f'{city}: {occurrences}')
print()
print('Most likely weather in seven days')
print('----------------------------------')
for city, mode in modes_dict.items():
    print(f'{city}: {mode}')
