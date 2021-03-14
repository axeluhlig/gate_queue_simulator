import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def plot_tipping_point(simulator_func):
    flakiness = np.arange(0, 0.4, 0.01)
    new_elements_per_cycle = np.arange(0, 40, 1)
    cycles = 10000  # high number to ensure reproducable output
    X, Y = np.meshgrid(flakiness, new_elements_per_cycle) 
    zs = np.empty((len(flakiness), len(new_elements_per_cycle)))
    for i, f in enumerate(flakiness):
        print(str(i) + '/' + str(len(flakiness)))
        for j, n in enumerate(new_elements_per_cycle):
            zs[i][j] = int(determine_stability(simulator_func(f, n, cycles, verbosity=False)))
    Z = zs.reshape(X.shape)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.view_init(23,23)
    ax.set_xlabel('Flakyness')
    ax.set_ylabel('New elements per cycle')
    ax.set_zlabel('Stability')

    plt.show()
    fig.savefig("test.png")


def determine_stability(queue_length_over_time):
    if queue_length_over_time[-1] > 1000:
        return False
    return True


def plot_simulation(results, flakiness, new_elements_per_time_interval):
    fig, ax = plt.subplots()
    ax.plot(results)
    title_str = 'Flakiness: ' + \
        str(flakiness) + ', New elements per cylce: ' + \
        str(new_elements_per_time_interval)
    if determine_stability(results):
        title_str += ' - STABLE'
    else:
        title_str += ' - UNSTABLE'
    ax.set(xlabel='cycle', ylabel='queue length', title=title_str)
    ax.grid()
    fig.savefig("test.png")
    plt.show()
