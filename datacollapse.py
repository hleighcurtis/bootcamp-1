import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Open the files.
wt_data = np.loadtxt('data/wt_lac.csv', comments='#', skiprows=3, delimiter=',')
m_data = np.loadtxt('data/q18m_lac.csv', comments='#', skiprows=3, delimiter=',')
a_data = np.loadtxt('data/q18a_lac.csv', comments='#', skiprows=3, delimiter=',')

# Define the variables.
IPTG_wt = wt_data[:,0]
fc_wt = wt_data[:,1]

IPTG_a = a_data[:,0]
fc_a = a_data[:,1]

IPTG_m = m_data[:,0]
fc_m = m_data[:,1]

# Close all otehr plots.
plt.close()

# Make a plot of fold change IPTG concentration for each of the three mutants.
plt.loglog(IPTG_wt, fc_wt, linestyle='none', marker='.', markersize=20, alpha=0.5)
plt.loglog(IPTG_a, fc_a, linestyle='none', marker='.', markersize=20, alpha=0.5)
plt.loglog(IPTG_m, fc_m, linestyle='none', marker='.', markersize=20, alpha=0.5)
# plt.semilogx(IPTG_wt, fc_wt, linestyle='none', marker='.', markersize=20, alpha=0.5)
# plt.semilogx(IPTG_a, fc_a, linestyle='none', marker='.', markersize=20, alpha=0.5)
# plt.semilogx(IPTG_m, fc_m, linestyle='none', marker='.', markersize=20, alpha=0.5)
plt.xlabel('IPTG (mM)')
plt.ylabel('Fold Change')
plt.ylim(-0.02, 1.02)
plt.xlim(10e-6, 10e1)
plt.margins(0.2)
plt.title('IPTG titration')
# plt.legend(('Wild-type', 'q18a', 'q18m'), loc='lower right')
# # plt.show()

# Make an array of closely spaced points for the IPTG concentration.
#c = np.linspace(-15, 15, 400)
c = np.logspace(-6, 2, 400) # look at data and emulate range to get values

def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    '''Computes the theoretical fold change. It allows c, the concentration
    of IPTG, to be passed in as a NumPy array or scalar, and RK, the  R/KR/K
    ratio, must be a scalar.
    WT  	141.5 mM −1−1
    Q18A	16.56 mM −1−1
    Q18M	1332 mM −1−1
    c = concentration of IPTG - can be an array or scalar'''

    # I broke the fold change equasion into smaller parts to aviod mistakes.
    A = (1 + (c / KdA))**2
    I = (1 + (c / KdI))**2
    Top = RK * A
    Bottom = A + (Kswitch * I)
    return (1 + (Top / Bottom))**(-1)

# Compute the theoretical fold change based on the given parameters using
# the function you wrote in part (c).
tfc_wt = fold_change(c, 141.5, KdA=0.017, KdI=0.002, Kswitch=5.8)
tfc_a = fold_change(c, 16.56, KdA=0.017, KdI=0.002, Kswitch=5.8)
tfc_m = fold_change(c, 1332, KdA=0.017, KdI=0.002, Kswitch=5.8)

# Add to plot of exp fold change with theoretical fold change for each of the three mutants.
plt.loglog(c, tfc_wt, linestyle='none', marker='.', markersize=10, alpha=0.5)
plt.loglog(c, tfc_a, linestyle='none', marker='.', markersize=10, alpha=0.5)
plt.loglog(c, tfc_m, linestyle='none', marker='.', markersize=10, alpha=0.5)
plt.legend(('Wild-type', 'q18a', 'q18m', 'theo_wt', 'theo_a', 'theo_m'), loc='lower right')
plt.show

# Define the Bohr parameter.
def bohr_fc(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):

    A = (1 + (c / KdA))**2
    I = (1 + (c / KdI))**2
    bottom = A + (Kswitch * I)
    frac = (A / bottom)
    bohr = -(np.log(RK)) - np.log(frac)
    return bohr

bfc_wt = 1/(1 + np.exp(bohr_fc(c, 141.5, KdA=0.017, KdI=0.002, Kswitch=5.8))
bfc_a = 1/(1 + np.exp(bohr_fc(c, 16.56, KdA=0.017, KdI=0.002, Kswitch=5.8))
bfc_m = 1/(1 + np.exp(bohr_fc(c, 1332, KdA=0.017, KdI=0.002, Kswitch=5.8))
