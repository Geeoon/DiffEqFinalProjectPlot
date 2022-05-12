from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.xlim(-3 * np.pi, 3 * np.pi)
    plt.ylim(-5, 5)
    ax.grid(True, which='both')
    ax.set_aspect('equal')
    
    x = np.arange(-3 * np.pi, 3 * np.pi, 0.001)
    a0 = -4 / np.pi
    y = a0
    # for n = 1
    y += 8 / (15 * np.pi) * np.cos(x) + 2 * np.sin(x)
    plt.plot(x, y)
    plt.title('Harmonic 1')
    plt.savefig('plots/plot1.png', bbox_inches="tight")

    for n in range(2,51):
        if n != 4:
            an = (2 * (-1) ** (n + 1) - 2) / (n + 1) + (2 + 2 * (-1) ** (n)) / (n - 1) + ((-1) ** (n+1) + 1) / (2 * (n + 4)) + ((-1) ** n - 1) / (2 * (n - 4))
            an /= np.pi
            y += an * np.cos(n * x)
        else:  # for n = 4
            y += 8 / (15 * np.pi) * np.cos(4 * x) + np.sin(4 * x) / 2
        plt.cla()
        plt.title('Harmonic ' + str(n))
        plt.plot(x, y)
        plt.xlim(-3 * np.pi, 3 * np.pi)
        plt.ylim(-5, 5)
        ax.grid(True, which='both')
        ax.set_aspect('equal')
        ax.grid(True, which='both')
        plt.savefig('plots/plot' + str(n) + '.png', bbox_inches="tight")
    
    plt.show()