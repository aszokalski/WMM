import numpy as np

def make_sin(scale):
    return (lambda t: np.sin(scale, t)), 2*np.pi/scale

def main():
    sin, period = make_sin(2*np.pi)
    print(period)

if __name__ == "__main__":
    main()
