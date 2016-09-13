import numpy as np

# Load in data (uploading data should always be done in a text file)
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')


def xa_to_diameter(xa):
    """a function that takes in an array of cross-sectional areas and returns
    an array of diameters."""

    #comupte diamter from area
    #A = (pi(d^2))/4
    diameter = np.sqrt(4* xa / np.pi)

    return diameter

A = np.array([[6.7, 1.3, 0.6, 0.7],
a function that takes in an array of cross-sectional areas and returns an array of diameters.                 [0.1, 5.5, 0.4, 2.4],
                [0.0, 1.5, 3.4, 7.5],
                [1.1, 0.8, 4.5, 1.7]])

b = np.array([1.1, 2.3, 3.3, 3.9])
