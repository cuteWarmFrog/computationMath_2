import numpy as np
import matplotlib.pyplot as plt


def defaultX(x):
    return x * 0


def drawGraphic(func1, func2=defaultX):
    plt.title("График")
    x = np.linspace(-2, 3, 100, True)
    plt.plot(x, func1(x))
    plt.plot(x, func2(x))
    plt.show()
    plt.close('all')
