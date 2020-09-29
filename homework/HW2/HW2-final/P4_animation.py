#!/usr/bin/env python3
import numpy
import matplotlib.pyplot as plt
import datetime


def clock_hand(hand_length):
    def closure(theta):
        theta_radians = theta * (numpy.pi/180)
        x_coord = hand_length * numpy.cos(theta_radians)
        y_coord = hand_length * numpy.sin(theta_radians)
        return x_coord, y_coord
    return closure


fig = plt.figure(figsize=(6, 6))           # Defining figure window to use/reuse
start_time = None                          # Initialize start time of animation
run_duration = 64                          # To be sure to go for at least 1 min
end_time = None                            # Initialize end time of animation

# Running animation...
while True:
    currentDT = datetime.datetime.now()

    if start_time is None:                 # Set timer if not yet set
        start_time = currentDT
        end_time = start_time + datetime.timedelta(seconds=run_duration)
    elif currentDT >= end_time:            # If time's up then end animation
        break

    hour = currentDT.hour
    minute = currentDT.minute
    second = currentDT.second

    theta_hour = 90 - (30 * hour) - (minute / 2)
    theta_min = 90 - (6 * minute)
    theta_sec = 90 - (6 * second)

    length_hour = 1.5
    length_min = 2.7
    length_sec = 2.5

    hour_hand = clock_hand(length_hour)
    x_hour, y_hour = hour_hand(theta_hour)
    point1_hour = [0, 0]
    point2_hour = [x_hour, y_hour]
    x_values_hour = [point1_hour[0], point2_hour[0]]
    y_values_hour = [point1_hour[1], point2_hour[1]]

    min_hand = clock_hand(length_min)
    x_min, y_min = min_hand(theta_min)
    point1_min = [0, 0]
    point2_min = [x_min, y_min]
    x_values_min = [point1_min[0], point2_min[0]]
    y_values_min = [point1_min[1], point2_min[1]]

    sec_hand = clock_hand(length_sec)
    x_sec, y_sec = sec_hand(theta_sec)
    point1_sec = [0, 0]
    point2_sec = [x_sec, y_sec]
    x_values_sec = [point1_sec[0], point2_sec[0]]
    y_values_sec = [point1_sec[1], point2_sec[1]]

    # Plotting...
    plt.plot(x_values_hour, y_values_hour)
    plt.plot(x_values_min, y_values_min)
    plt.plot(x_values_sec, y_values_sec)
    plt.axis('off')                        # Hides axes
    plt.axis([-3.25, 3.25, -3.25, 3.25])   # For consistent aspect ratio
    fig.canvas.draw()
    plt.pause(0.1)
    plt.cla()


# References
# https://www.kite.com/python/answers/how-to-draw-a-line-between-two-points-in-matplotlib-in-python
# https://stackoverflow.com/questions/2130913/no-plot-window-in-matplotlib
# https://stackoverflow.com/questions/9295026/matplotlib-plots-removing-axis-legends-and-white-spaces
# https://stackoverflow.com/questions/100210/what-is-the-standard-way-to-add-n-seconds-to-datetime-time-in-python
