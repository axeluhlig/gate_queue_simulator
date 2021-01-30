#!/usr/bin/env python3

import pickle

from simulator import core


def main():
    sim = core.Simulator()
    sim.do_basic_sim(initial_queue_length= 5, flakiness= 0.5, new_elements_per_time_interval= 10, cycle= 1000)


if __name__ == "__main__":
    main()
