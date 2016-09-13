import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#set matplotlib params
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
'axes.titlesize' : 18}
sns.set(rc=rc)

#load the food data.
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

#make the bin boundaries.
    #bins = np.arange(1700, 2500, 50)
#let's find the smallst common...
low_min = np.min(xa_low)
low_max = np.max(xa_low)
high_min = np.min(xa_high)
high_max = np.max(xa_high)
global_min = np.min([low_min, high_min])
global_max = np.max([low_max, high_max])
bins = np.arange(global_min-50, global_max+50, 50)

#Plot the data as a histogram.
    #_ = plt.hist((xa_low, xa_high), bins=bins) #the underscore is a garbage collector
#symbol to silence unneeded prints
    #plt.xlabel('Cross-sectional area (um$^2$)')
    #plt.ylabel('count', rotation='horizontal')
    #plt.show()

#Plot the data as two overlapping histograms.
_ = plt.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
_ = plt.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
plt.xlabel('Cross-sectional area (um$^2$)')
plt.ylabel('frequency', rotation='horizontal')
plt.legend(('low concentration', 'high sconcentration'), loc='upper right')
#plt.show()

#save the figure
plt.savefig('C://Users/Heather Curtis/Documents/git/bootcamp-1/egg_area_histograms.svg', bbox__inches='tight')
plt.show()
