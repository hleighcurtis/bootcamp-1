#bootcamp_utils: a collection of statistical functions prooved useful
#to 55 students.
import numpy as np

def ecdf(data):
    """Compute x, y values for emperical distributon function """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)
    return x, y
