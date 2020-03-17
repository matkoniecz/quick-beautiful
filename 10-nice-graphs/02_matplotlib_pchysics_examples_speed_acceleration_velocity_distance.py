import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import collections
import functools

def main():
    plt.rcParams["figure.figsize"] = [8, 8]
    plt.rcParams["figure.dpi"] = 60
    plt.style.use('fivethirtyeight')
    plt.grid(True)
    resolution = 0.1
    time=10
    datapoint_count = int(time/resolution) + 1
    datapoints = [d*resolution for d in range(datapoint_count)]

    make_graphs("speed=10", datapoints, resolution, [0 for d in range(datapoint_count)], 10, 0)
    make_graphs("speed=0", datapoints, resolution, [0 for d in range(datapoint_count)], 0, 0)
    make_graphs("acc=1", datapoints, resolution, [1 for d in range(datapoint_count)], 0, 0)
    make_graphs("acc=-1, v0=10", datapoints, resolution, [-1 for d in range(datapoint_count)], 10, 0)
    
    time=20
    datapoint_count = int(time/resolution) + 1
    datapoints = [d*resolution for d in range(datapoint_count)]

    start_stop_acceleration=[]
    change_count = int(datapoint_count/4)
    start_stop_acceleration.append(0)
    for i in range(change_count):
        start_stop_acceleration.append(3)
    for i in range(datapoint_count-2*change_count-2):
        start_stop_acceleration.append(0)
    for i in range(change_count):
        start_stop_acceleration.append(-3)
    start_stop_acceleration.append(0)
    make_graphs("acc up and down", datapoints, resolution, start_stop_acceleration, 0, 0)


def make_graphs(name, datapoints, resolution, acceleration_datapoints, speed_initial, distance_initial):
    speed_computed = [speed_initial]
    for index in range(len(datapoints)):
        current = speed_computed[-1]
        speed_computed.append(acceleration_datapoints[index]*resolution + current)
    speed_computed = speed_computed[0:-1]

    distance_computed = [distance_initial]
    for index in range(len(datapoints)):
        current = distance_computed[-1]
        distance_computed.append(speed_computed[index]*resolution + current)
    distance_computed = distance_computed[0:-1]

    plt.clf()
    plt.xlabel('t [s]')
    plt.ylabel('v [m/s]')
    plt.title("v(t)")
    plt.plot(datapoints, speed_computed, 'r-')
    plt.savefig(name + ' speed.png')

    plt.clf()
    plt.xlabel('t [s]')
    plt.ylabel('v [m/s^2]')
    plt.title("a(t)")
    plt.plot(datapoints, acceleration_datapoints, 'r-')
    plt.savefig(name + ' acceleration.png')

    plt.clf()
    plt.xlabel('t [s]')
    plt.ylabel('S [m]')
    plt.title("S(t)")
    plt.plot(datapoints, distance_computed, 'r-')
    plt.savefig(name + ' distance.png')

main()