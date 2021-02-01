#!/usr/bin/env python3
import matplotlib.pyplot as plt

from simulator import core

# next steps
# - do gate resets not at head, but with decreasing probability
# - write function to search for tipping point in regards of flakiness for given new_elements
# - plot final results: tipping points on flakiness vs new_elements plot


def plot_simulation(results, flakiness, new_elements_per_time_interval):
    fig, ax = plt.subplots()
    ax.plot(results)
    ax.set(xlabel='cycle', ylabel='queue length',
           title='Flakiness: ' + str(flakiness) + ', New elements per cylce: ' + str(new_elements_per_time_interval))
    ax.grid()
    fig.savefig("test.png")
    plt.show()


def main():
    sim = core.Simulator()
    # if this number is big enough (e.g. 10,000) you  don't need to run the sim n times to get a good result
    cycle = 10000
    flakiness = 0.01
    new_elements_per_time_interval = 10
    results = sim.do_basic_sim(flakiness,
                               new_elements_per_time_interval, cycle, verbosity=False)
    plot_simulation(results, flakiness, new_elements_per_time_interval)


if __name__ == "__main__":
    main()
