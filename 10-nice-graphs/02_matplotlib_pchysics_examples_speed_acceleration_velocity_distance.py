import matplotlib.pyplot as plt
#import seaborn
import numpy as np
import sys
import collections
import functools

def main():
    #plt.rcParams["figure.dpi"] = 60
    plt.rcParams["figure.autolayout"] = True # https://stackoverflow.com/questions/6774086/why-is-my-xlabel-cut-off-in-my-matplotlib-plot
    
    # https://python-graph-gallery.com/199-matplotlib-style-sheets/
    # https://jakevdp.github.io/PythonDataScienceHandbook/04.11-settings-and-stylesheets.html
    #plt.style.use('fivethirtyeight') # good for display on computer
    #plt.style.use('grayscale') # "artistic"
    plt.style.use('seaborn-whitegrid') # good for printing
    #plt.style.use('seaborn-white')
    
    
    #seaborn.set(rc={'patch.edgecolor':'brown', 'axes.edgecolor':'yellow', 'grid.color':'pink', 'figure.facecolor':'blue', 'axes.facecolor':'red'})
    #style = seaborn.axes_style()
    #style['axes.facecolor'] = "white"
    #seaborn.set(rc=style)
    #seaborn.set(rc={'axes.facecolor':'white', 'grid.color':'#aaaaaa'})
    #print(seaborn.axes_style())


    plt.grid(True)
    resolution = 0.1
    time=10
    datapoint_count = int(time/resolution) + 1
    datapoints = [d*resolution for d in range(datapoint_count)]

    make_graphs("speed=10000", datapoints, resolution, [0 for d in range(datapoint_count)], 10000, 0)
    make_graphs("speed=0.1", datapoints, resolution, [0 for d in range(datapoint_count)], 0.1, 0)
    make_graphs("speed=5", datapoints, resolution, [0 for d in range(datapoint_count)], 10, 0)
    make_graphs("speed=0", datapoints, resolution, [0 for d in range(datapoint_count)], 0, 0)
    make_graphs("acc=1", datapoints, resolution, [1 for d in range(datapoint_count)], 0, 0)

    time = 5
    datapoint_count = int(time/resolution) + 1
    datapoints = [d*resolution for d in range(datapoint_count)]
    make_graphs("speed=10, a=1", datapoints, resolution, [1 for d in range(int(datapoint_count))], 10, 0)

    time = 30
    datapoint_count = int(time/resolution) + 1
    datapoints = [d*resolution for d in range(datapoint_count)]
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
    speed_computed = integrate_data(resolution, acceleration_datapoints, speed_initial)
    distance_computed = integrate_data(resolution, speed_computed, distance_initial)
    make_graph_column_packed(name, datapoints, acceleration_datapoints, speed_computed, distance_computed)

def integrate_data(resolution, input_data, initial_input):
    # for example acceleration datapoints as input_data
    # speed as outpu
    computed = [initial_input]
    for index in range(len(input_data)):
        current = computed[-1]
        computed.append(input_data[index]*resolution + current)
    return computed[0:-1]

def make_graph_row_packed(name, datapoints, acceleration_datapoints, speed_datapoints, distance_datapoints):
    plt.rcParams["figure.figsize"] = [20, 1]
    plt.clf()
    plt.subplot(1,3, 1)
    plt.xlabel('t [s]')
    plt.ylabel('v [m/s]')
    plt.title("v(t)")
    plt.plot(datapoints, speed_datapoints, 'r-')

    plt.subplot(1,3, 2)
    plt.xlabel('t [s]')
    plt.ylabel('v [m/s^2]')
    plt.title("a(t)")
    plt.plot(datapoints, acceleration_datapoints, 'r-')

    plt.subplot(1, 3, 3)
    plt.xlabel('t [s]')
    plt.ylabel('S [m]')
    plt.title("S(t)")
    plt.plot(datapoints, distance_datapoints, 'r-')
    plt.savefig(name + '.png')

def make_graph_column_packed(name, datapoints, acceleration_datapoints, speed_datapoints, distance_datapoints):
    plt.rcParams["figure.figsize"] = [11, 14]
    plt.clf()
    plt.subplot(3,1,1)
    plt.xlabel('t [s]')
    plt.ylabel('v [m/s]')
    plt.title("v(t)")
    plt.plot(datapoints, speed_datapoints, 'r-')

    plt.subplot(3,1,2)
    plt.xlabel('t [s]')
    plt.ylabel('v [m/s^2]')
    plt.title("a(t)")
    plt.plot(datapoints, acceleration_datapoints, 'r-')

    plt.subplot(3,1,3)
    plt.xlabel('t [s]')
    plt.ylabel('S [m]')
    plt.title("S(t)")
    plt.plot(datapoints, distance_datapoints, 'r-')
    plt.savefig(name + '.png')

def make_graphs_separate(name, datapoints, acceleration_datapoints, speed_datapoints, distance_datapoints):
    plt.clf()
    plt.xlabel('t [s]')
    plt.ylabel('v [m/s]')
    plt.title("v(t)")
    plt.plot(datapoints, speed_datapoints, 'r-')
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
    plt.plot(datapoints, distance_datapoints, 'r-')
    plt.savefig(name + ' distance.png')

main()