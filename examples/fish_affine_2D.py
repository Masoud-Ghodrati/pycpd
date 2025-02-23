from functools import partial
import matplotlib.pyplot as plt
from pycpd import affine_registration
import numpy as np
import time

def visualize(iteration, error, X, Y, ax):
    plt.cla()
    X
    ax.scatter(X[:,0] ,  X[:,1], color='red', label='Target')
    ax.scatter(Y[:,0] ,  Y[:,1], color='blue', label='Source')
    plt.text(0.87, 0.92, 'Iteration: {:d}\nError: {:06.4f}'.format(iteration, error), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize='x-large')
    ax.legend(loc='upper left', fontsize='x-large')
    plt.draw()
    plt.pause(0.5)


def main():
    X = np.loadtxt('C:/DS_git/pycpd/data/fish_target.txt')
    Y = np.loadtxt('C:/DS_git/pycpd/data/fish_source.txt')

    fig = plt.figure()
    fig.add_axes([0, 0, 1, 1])
    callback = partial(visualize, ax=fig.axes[0])

    reg = affine_registration(**{ 'X': X, 'Y': Y })
    reg.register(callback)
    plt.show()

if __name__ == '__main__':
    main()
