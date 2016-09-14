import seaborn as sns
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

rc={'lines.linewidth': 2, 'axes.labelsize': 18,
                        'axes.titlesize': 18}

data_txt = np.loadtxt('data/collins_switch.csv',
                        skiprows=2, delimiter=',')

# #slice out itpg and gfp.
iptg = data_txt[:,0]
gfp = data_txt[:,1]
#
#plot iptg vs gfp.
plt.semilogx(iptg, gfp, linestyle='none',
                        marker='.', markersize=20)
plt.xlabel('IPTG (mM)')
plt.ylabel('Normalized GFP')
plt.ylim(-0.02, 1.02)
plt.xlim(8e-4, 15)
plt.title('IPTG titration semilog X')

plt.show()

I made everything below this a comment becasue the plots werent
    as good by using 'ctrl' '/'.
#plot iptg vs gfp
plt.loglog(iptg, gfp, linestyle='none',
                        marker='.', markersize=20)
plt.xlabel('IPTG (mM)')
plt.ylabel('Normalized GFP')
plt.title('IPTG titration Log-Log')
plt.margins(0.02)

plt.show()



#define the standar error of the mean.
sem = data_txt[:,2]

# #plot iptg vs gfp
# plt.errorbar(iptg, gfp, linestyle='none',
#                         marker='.', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.xscale('log') #this plotting function is default linear scale so
#     #need to explicitly change it to log.
# plt.title('IPTG titration error')
#
# plt.show()
