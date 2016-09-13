import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.special

# generate an array of x values. Can add quick command that screens for a
#value of zero and turn it into an arbitrarily low number close to zero.
x = np.linspace(-15, 15, 400)

# Compute the normalized instensity.
norm_I = 4 * (scipy.special.j1(x) / x)**2

# Plot our compuations.
plt.close()
plt.plot(x, norm_I, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$I(x)/I0$')
#plt.show()

#Processing spike data.
data = np.loadtxt('data/retina_spikes.csv', skiprows=2, comments='#', delimiter=',')
t = data[:,0]
V = data[:,1]

#close all otehr plots
plt.close()

#ploting time vs voltage
plt.plot(t, V)
plt.xlabel('t (ms)')
plt.ylabel('V (uV)')
plt.xlim(1395, 1400)
plt.show()
