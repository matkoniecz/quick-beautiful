import matplotlib.pyplot as plt
import numpy as np
import sys
import collections
import functools

def main():
    plt.rcParams["figure.figsize"] = [10, 10]
    # https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
    # see 02 file for more investigation
    plt.style.use('fivethirtyeight') # affects all charts, 'seaborn-v0_8-whitegrid' is also nice
    plt.grid(True)
    make_graph()
    make_bargraph()
    make_bargraph_with_merged_bars()


def make_bargraph_with_merged_bars():
    plt.clf()
    plt.hist([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1,
            1, 2, 3, 4, 5, 6, 1, 0, 10], bins=11)
    plt.savefig("bargraph_with_merged_bars.png")
    plt.show()


def make_graph():
    D = [2, 4, 6, 8, 10]
    A = [d*d*d for d in D]
    plt.clf()
    plt.xlabel('Ants')
    plt.ylabel('Potatoes')
    plt.title("Plot the estimate and real data, note drastic difference.")
    plt.plot(D, [120*d+790 for d in D], 'r-') # r instructs to make red line
    plt.plot(D, A, 'kD') # D instructs to make dots
    # bo gives blue circle markers
    # see
    # plot(x, y, 'go--', linewidth=2, markersize=12)
    # plot(x, y, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
    # giving the same outcome
    # see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
    plt.savefig('line_and_points.png')
    plt.show()


def make_bargraph():
    objects = ('Six', 'Four', 'Two', 'Ten', 'One')
    y_pos = np.arange(len(objects))
    performance = [6, 4, 2, 10, 1]
    plt.clf()
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Value')
    plt.title('Useless bar graph')
    plt.savefig('bargraph.png')
    plt.show()


main()