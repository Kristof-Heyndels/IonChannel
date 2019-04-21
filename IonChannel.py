import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import seaborn as sns

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
        rnd = np.random.random()
        time_in_state += dt
        if rnd < (k * dt):
            log_interval(state, round(time_in_state, 3))
            state = toggle(state)
            time_in_state = 0

    # creating histogram and fit
    sns.set_style('darkgrid')
    sns.distplot(OPEN_TIMES,bins=100,fit=ss.expon,kde=False)
    print(ss.expon.fit(OPEN_TIMES))

    plt.title("Histogram and exponentional fit of intervals open state")
    plt.xlabel("Duration of open state (s)")
    plt.ylabel("Occurunces")

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
