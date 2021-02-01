#!/usr/bin/env python3
import matplotlib.pyplot as plt

from simulator import core

# next steps
# - plot data
# - do n times for every flakiness = [0.01, 0.02, 0.03]
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
    flakiness = 0.02
    new_elements_per_time_interval = 10
    results = sim.do_basic_sim(flakiness,
                               new_elements_per_time_interval, cycle=1000, verbosity=False)
    plot_simulation(results, flakiness, new_elements_per_time_interval)


if __name__ == "__main__":
    main()
