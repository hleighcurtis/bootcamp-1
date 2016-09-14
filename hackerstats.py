import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data.
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

#perfroming a bootstrap one time.
# bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
# bs_replicate = np.mean(bs_sample)
# bs_sample12 = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
# bs_replicate12 = np.mean(bs_sample12)

# Generating a whole bunch of bootstrap replicates for 1975.
n_reps = 100000 # Generally, 1000 reps is the min.
bs_replicates_1975 = np.empty(n_reps)

for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    bs_replicates_1975[i] = np.mean(bs_sample)

# Comute the confidence intervial.
conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])

# Generating a whole bunch of bootstrap replicates for 2012.
n_reps = 100000
bs_replicates_2012 = np.empty(n_reps)

for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    bs_replicates_2012[i] = np.mean(bs_sample)

# Comute the confidence intervial.
conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

# # Defining the variables.
# x_1975, y_1975 = ecdf(bd_1975)
# x_2012, y_2012 = ecdf(bd_2012)
# x_1975_bs, y_1975_bs = ecdf(bs_sample)
# x_2012_bs, y_2012_bs = ecdf(bs_sample2)
#
# plt.plot(x_1975, y_1975, marker='.', linestyle='none', markersize=8)
# # plt.plot(x_2012, y_2012, marker='.', linestyle='none', markersize=8)
#
# plt.xlabel('Beak depth (mm)')
# plt.ylabel('EDCF')
# plt.legend('1975', 'boostrap', loc='lower right')
# plt.show()
