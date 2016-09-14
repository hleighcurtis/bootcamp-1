import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ecdf(data):
    """Compute x, y values for emperical distributon function """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)
    return x, y

#Specificy parameters.
# Number of generations.
n_gen = 16

# Chance of having an benifical mutation. Chose an arbitry small number.
# Probablity of successful mutation.
r = 1e-5

# Define the Total number of cells.
n_cells = 2**(n_gen - 1)

# Draw our adaptive immunity samples over a binomial distributon.
ai_samples = np.random.binomial(n_cells, r, size=100000)

# #PLot with bin count
# _ = plt.hist(ai_samples, bins=10) #Not good becasue don't know bins
# counts = np.bincount(ai_samples)
# _ = plt.plot(np.arange(len(counts)), counts, marker='.', linestyle='none')

# Report mean and standar deveiation.
print('Ai mean', np.mean(ai_samples))
print('Ai std', np.std(ai_samples))
print('Ai Fano', np.var(ai_samples) / np.mean(ai_samples))

# Function to draw out the random mutaitons hypothesis.
def draw_random_mutation(n_gen, r):
    """Draw sample under random mutation hypothesis"""

    # Start off with zero mutations
    n_mut = 0

    for g in range(n_gen):
        n_mut = 2*n_mut + np.random.binomial(2**g - 2*n_mut, r)

    #return the new number of mutations
    return n_mut

def sample_random_mutation(n_gen, r, size=1):

    # Initiailze an aray for samples.
    samples = np.empty(size)

    #
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)
    return samples

rm_samples = sample_random_mutation(n_gen, r, size=100000)

# Report mean and standar deveiation.
print('rm mean', np.mean(rm_samples))
print('rm std', np.std(rm_samples))
print('rm Fano', np.var(rm_samples) / np.mean(rm_samples))

x_ai, y_ai = ecdf(ai_samples)
x_rm, y_rm = ecdf(rm_samples)

plt.semilogx(x_ai, y_ai, marker='.', linestyle='none')
plt.semilogx(x_rm, y_rm, marker='.', linestyle='none')
plt.show()
