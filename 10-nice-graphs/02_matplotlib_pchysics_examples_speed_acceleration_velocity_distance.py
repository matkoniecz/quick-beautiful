import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import collections
import functools

def main():
    plt.rcParams["figure.figsize"] = [10, 10]
    plt.style.use('fivethirtyeight')
    plt.grid(True)
    resolution = 0.1
    time=10
    datapoint_count = int(time/resolution) + 1
    datapoints = [d*resolution for d in range(datapoint_count)]
    speed = 10
    acceleration_datapoints = [0 for d in datapoints]
    speed_datapoints = [speed for d in datapoints]
    make_graphs(datapoints, resolution, speed_datapoints, acceleration_datapoints, distance_datapoints, 0)

def make_graphs(datapoints, resolution, speed_datapoints, acceleration_datapoints, distance_initial):
    distance_computed = [distance_initial]
    for index in range(len(datapoints)):
        current = distance_computed[-1]
        distance_computed.append(speed_datapoints[index]*resolution + current)
    distance_computed = distance_computed[0:-1]

    plt.clf()
    plt.xlabel('t [s]')
    plt.ylabel('v [m/s]')
    plt.title("v(t)")
    plt.plot(datapoints, speed_datapoints, 'r-')
    plt.savefig('speed.png')

    plt.clf()
    plt.xlabel('t [s]')
    plt.ylabel('v [m/s^2]')
    plt.title("a(t)")
    plt.plot(datapoints, acceleration_datapoints, 'r-')
    plt.savefig('acceleration.png')

    plt.clf()
    plt.xlabel('t [s]')
    plt.ylabel('S [m]')
    plt.title("S(t)")
    plt.plot(datapoints, distance_computed, 'r-')
    plt.savefig('distance_computed.png')
    plt.show()


main()