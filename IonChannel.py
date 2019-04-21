from numpy.random import random
from matplotlib import pyplot
from scipy import stats
import seaborn

OPEN = 1
CLOSED = 0

OPEN_TIMES = []
CLOSED_TIMES = []


def main():
    # state of channel
    state = OPEN

    # k*dt=1/100
    k = 10
    dt = 1/1000
    time_in_state = 0

    rnd = 0

    # measure for 10 minutes
    for x in range(1, 10*60*1000):
        # random number in half-open interval [0.0, 1.0)
        rnd = random()
        time_in_state += dt
        if rnd < (k * dt):
            log_interval(state, round(time_in_state, 3))
            state = toggle(state)
            time_in_state = 0

    # creating histogram and fit
    seaborn.set_style('darkgrid')
    seaborn.distplot(OPEN_TIMES,bins=100,fit=stats.expon,kde=False)
    print(stats.expon.fit(OPEN_TIMES))

    pyplot.title("Histogram and exponentional fit of intervals open state")
    pyplot.xlabel("Duration of open state (s)")
    pyplot.ylabel("Occurunces")

    plt.show()


def toggle(state):
    if state == OPEN:
        return CLOSED
    return OPEN

# stores the duration the ion channel was in a state
def log_interval(state, time_in_state):
    if state == OPEN:
        OPEN_TIMES.append(time_in_state)
    else:
        CLOSED_TIMES.append(time_in_state)


if __name__ == "__main__":
    main()
