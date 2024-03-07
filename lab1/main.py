import numpy as np
import matplotlib.pyplot as plt

def make_sin(pulsation):
    return (lambda t: np.sin(pulsation * t)), 2 * np.pi / pulsation


def sample_signal(signal, period, num_samples):
    delta_t = period / num_samples
    dirac_d = np.arange(0, 1, delta_t)
    return signal(dirac_d), dirac_d

def main():
    sin, period = make_sin(2 * np.pi)
    samples, dirac_d = sample_signal(sin, period, 8)
    spectrum_sin = np.fft.fft(samples)
    freq_spectrum_sin = np.abs(spectrum_sin)
    phase_spectrum_sin = np.angle(spectrum_sin)

    X_cont = np.arange(0, period, 0.01)
    X_discr = dirac_d * period

    fig, ax = plt.subplots(1, 3)

    ax[0].plot(X_cont, sin(X_cont), "--", color="red")
    ax[0].stem(X_discr, samples, linefmt='k-', markerfmt='o', basefmt='k-')
    ax[0].plot(X_cont, np.zeros(X_cont.shape), color="black")  # line

    ax[1].stem(X_discr, freq_spectrum_sin)

    ax[2].stem(X_discr, phase_spectrum_sin)

    plt.show()



if __name__ == "__main__":
    main()
