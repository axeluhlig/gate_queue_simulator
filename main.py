#!/usr/bin/env python3

from simulator import core, analysis

# next steps
# - do gate resets not at head, but with decreasing probability
# - write function to search for tipping point in regards of flakiness for given new_elements
# - plot final results: tipping points on flakiness vs new_elements plot


def main():
    sim = core.Simulator()
    # if this number is big enough (e.g. 10,000) you  don't need to run the sim n times to get a good result
    cycle = 10000
    flakiness = 0.02
    new_elements_per_time_interval = 10
    results = sim.do_basic_sim(flakiness,
                               new_elements_per_time_interval, cycle, verbosity=False)
    analysis.plot_simulation(results, flakiness, new_elements_per_time_interval)


if __name__ == "__main__":
    main()
