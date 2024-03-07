import numpy as np
import matplotlib.pyplot as plt

def make_sin(pulsation):
    return (lambda t: np.sin(pulsation, t)), 2 * np.pi / pulsation


def sample_signal(signal, period, num_samples):
    delta_t = period / num_samples
    dirac_d = np.arange(0, 1, delta_t)
    return signal(dirac_d), dirac_d


def plot(signal, period, sample, dirac_d):
    X_cont = np.arange(0, period)
    X_discr = dirac_d * period

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(X_cont, signal(X_cont), "-")
    ax.plot(X_discr, sample, "o")





def main():
    sin, period = make_sin(2 * np.pi)
    sample, dirac_d = sample_signal(sin, period, 8)
    plot(sin, period, sample, dirac_d)


if __name__ == "__main__":
    main()
