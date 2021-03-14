#!/usr/bin/env python3

from simulator import core, analysis

# next steps
# - do gate resets not at head, but with decreasing probability
# - write function to search for tipping point in regards of flakiness for given new_elements
# - plot final results: tipping points on flakiness vs new_elements plot


def main():
    sim = core.Simulator()
    analysis.plot_tipping_point(sim.do_basic_sim)


if __name__ == "__main__":
    main()
