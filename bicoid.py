import numpy as np
import pandas as pd

# We'll use scipy.optimize.curve_fit to do the nonlinear regression
import scipy.optimize

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Import data set
df = pd.read_csv('data/bcd_gradient.csv', comment='#')

# Inspect DataFrame
df.head()

# Import data set
df = pd.read_csv('data/bcd_gradient.csv', comment='#')

# Inspect DataFrame
df.head()

# Rename columns
df = df.rename(columns={'fractional distance from anterior': 'x',
                        '[bcd] (a.u.)': 'I_bcd'})

# Plot experimental Bcd gradient.
plt.close()
plt.plot(df['x'], df['I_bcd'], marker='.', linestyle='none', markersize=10)
# Label axes (no units on x because it's dimensionless)
plt.xlabel('x')
plt.ylabel('I (a.u.)')
plt.show()

def bcd_gradient_model(x, I_0, a, lam):
    """Model for Bcd gradient: exponential decay plus background"""

    assert np.all(np.array(x) >= 0), 'All values of x must be >= 0.'
    assert np.all(np.array([I_0, a, lam]) >= 0), 'All parameters must be >= 0.'

    return a + I_0 * np.exp(-x / lam)

# Specify initial guess
I_0_guess = 0.9
a_guess = 0.2
lam_guess = 1.0

# Construct initial guess array
p0 = np.array([I_0_guess, a_guess, lam_guess])

# Do curve fit, but dump covariance into dummy variable
popt, _ = scipy.optimize.curve_fit(bcd_gradient_model, df['x'], df['I_bcd'], p0=p0)

x_smooth = np.linspace(0, 1, 200)
I_smooth = bcd_gradient_model(x_smooth, *tuple(popt))

plt.plot(x_smooth, I_smooth, color='gray')

# Print the results
print("""
I_0 = {0:.2f}
  a = {1:.2f}
  λ = {2:.2f}
""".format(*tuple(p)))
