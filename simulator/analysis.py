import matplotlib.pyplot as plt


def determine_stability(queue_length_over_time):
    if queue_length_over_time[-1] > 1000:
        return False
    return True


def plot_simulation(results, flakiness, new_elements_per_time_interval):
    fig, ax = plt.subplots()
    ax.plot(results)
    title_str = 'Flakiness: ' + str(flakiness) + ', New elements per cylce: ' + str(new_elements_per_time_interval)
    if determine_stability(results):
        title_str += ' - STABLE'
    else:
        title_str += ' - UNSTABLE'
    ax.set(xlabel='cycle', ylabel='queue length',title=title_str)
    ax.grid()
    fig.savefig("test.png")
    plt.show()
