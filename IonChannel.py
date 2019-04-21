import numpy

OPEN = 1
CLOSED = 0

OPEN_TIMES = []
CLOSED_TIMES = []


def main():
    # state of channel
    state = OPEN

    # k*dt=1/100, with k the chance to switch state and dt the set time between meassurements
    k = 10
    dt = 1 / 1000
    time_in_state = 0

    rnd = 0

    # measure for a minute
    for x in range(1, 60 * 1000):
        # random number in half-open interval [0.0, 1.0)
        rnd = numpy.random.random()
        time_in_state += dt
        if rnd < (k * dt):
            state = toggle(state)

            log_interval(state, round(time_in_state,3))
            time_in_state = 0

    print(OPEN_TIMES)


def toggle(state):
    if state == OPEN:
        return CLOSED
    return OPEN


def log_interval(state, time_in_state):
    if state == OPEN:
        OPEN_TIMES.append(time_in_state)
    else:
        CLOSED_TIMES.append(time_in_state)


if __name__ == "__main__":
    main()
