import matplotlib.pyplot as plt 
import numpy as np


def scatter(x, y):
    fig, ax = plt.subplots()
    ax.tick_params(direction="in", length=4)
    ax.scatter(x, y, color='k')
    plt.show()

np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)

scatter(x, y)

