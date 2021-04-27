import numpy as np
import matplotlib.pyplot as plt


def defaultX(x):
    return x * 0


def drawGraphic(func1, func2=defaultX):
    plt.title("График")
    x = np.linspace(-5, 5, 100, True)
    plt.plot(x, func1(x))
    plt.plot(x, func2(x))

    if func2 != defaultX:
        plt.plot(x, defaultX(x))

    plt.ylim([-5, 10])
    plt.grid()
    plt.show()
    plt.close('all')
