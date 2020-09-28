#!/usr/bin/env python3
import numpy
import matplotlib.pyplot
import datetime
import math

def clock_hand(hand_length):
    def closure(theta):
        theta_radians = theta * (numpy.pi/180)
        x_coord = hand_length * numpy.cos(theta_radians)
    return closure