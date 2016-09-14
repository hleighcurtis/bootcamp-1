import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data.
data = np.loadtxt('data/beak_depth_scandens_1975.csv')


def draw_bs_reps(data, func=np.mean, size=100000):
    """Performing a bootstrap operation: Samples data points randomly with
    replacement to repeat the experiment many, many times.
    Returns an array with as many replicates as you choose (default=100000).
    The function can be user called (Options = np.mean, np.std)"""

    # Establish the empty array that will hold the replicates later.
    bs_replicates = np.empty(size)

    # Iterating the bootstrap several times.
    for i in range(size):
        bs_sample = np.random.choice(data, replace=True, size=len(data))
        bs_replicates[i] = func(bs_sample)

    return bs_replicates

def draw_conf_int(data, func=np.mean, size=100000):
    """Comute the confidence intervial. The function can be user called
    (Options = np.mean, np.std)"""
    calls = (data, func, size)
    return np.percentile(draw_bs_reps(calls), [2.5, 97.5])
