import seaborn as sns
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import bootcamp_utils

rc={'lines.linewidth': 2, 'axes.labelsize': 18,
                        'axes.titlesize': 18}

# Load in data (uploading data should always be done in a text file)
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

def ecdf(data):
    """Compute x, y values for emperical distributon function """
    x = np.sort(xa_high)
    y = np.arange(1, 1+len(x)) / len(x)
    return x, y

# # Load in data (uploading data should always be done in a text file)
# xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
# xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')


x_low, y_low = bootcamp_utils.ecdf(xa_low)
x_high, y_high = bootcamp_utils.ecdf(xa_high)

x = np.linspace(1600, 2500, 400)
cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high),
                                    scale=np.std(xa_high))
cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low),
                                    scale=np.std(xa_low))


plt.plot(x_high, y_high, marker='.', linestyle='none',
                                markersize=20, alpha=0.5)
plt.plot(x_low, y_low, marker='.', linestyle='none',
                                markersize=20, alpha=0.5)

plt.plot(x, cdf_high, marker='.', linestyle='none',
                                markersize=10, alpha=0.5)
plt.plot(x, cdf_low, marker='.', linestyle='none',
                                markersize=10, alpha=0.5)
plt.xlabel('Cross-sectional area (um)')
plt.ylabel('eCDF')
plt.legend(('high food', 'low food'), loc='lower right')
plt.show()
