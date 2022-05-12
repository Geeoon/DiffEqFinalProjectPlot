from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.arange(0, 4 * np.pi, 0.001)
    a0 = -4/np.pi
    y = a0
    for n in range(2,100):
        if n != 4:
            an = (2 * (-1) ** (n + 1) - 2) / (n + 1) + (2 + 2 * (-1) ** (n)) / (n - 1) + ((-1) ** (n+1) + 1) / (2 * (n + 4)) + ((-1) ** n - 1) / (2 * (n - 4))
            an /= np.pi
            y += an * np.cos(n * x)
    
    # for n = 1
    y += 8 / (15 * np.pi) * np.cos(x) + 2 * np.sin(x)

    # for n = 4
    y += 8 / (15 * np.pi) * np.cos(4 * x) + np.sin(4 * x) / 2

    plt.plot(x, y)
    plt.show()