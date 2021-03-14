#!/usr/bin/env python3

from simulator import core, analysis

# next steps
# - write more advanced simulator: doing n runs per input params, returning percentage of stable results
# - write more advanced simulator: do gate resets not at head, but with decreasing probability
# - multi processing for calling the simulator


def main():
    sim = core.Simulator()
    analysis.plot_tipping_point(sim.do_basic_sim)


if __name__ == "__main__":
    main()
