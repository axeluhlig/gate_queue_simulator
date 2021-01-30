#!/usr/bin/env python3

import pickle

from simulator import core

# next steps
# - return [t,q_l] instead
# - do n times for every flakiness = [0.01, 0.02, 0.03]
# - plot data


def main():
    sim = core.Simulator()
    print(sim.do_basic_sim(initial_queue_length=5, flakiness=0.01,
                           new_elements_per_time_interval=10, cycle=1000, verbosity=False))


if __name__ == "__main__":
    main()
