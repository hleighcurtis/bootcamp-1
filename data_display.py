import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)


# Load the data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Rename impact force column
df = df.rename(columns={'impact force (mN)': 'impf'})

# # Mean impact force of frog I (this is the unecarairly difficult way - use groupby())
# np.mean(df.loc[df['ID']=='I', 'impf'])
#
# mean_impf = np.empty(4)
# sem_impf = np.empty(4)
# for i, frog in enumerate(['I', 'II', 'III', 'IV']):
#     mean_impf[i] = np.mean(df.loc[df['ID']==frog, 'impf'])
#     n = np.sum(df['ID']=='I')
#     sem_impf[i] = np.std(df.loc[df['ID']==frog, 'impf']) / np.sqrt(n)
#
# print(mean_impf)
# print(sem_impf)

# Do the same as above but better (no for loops)
# gb_frog = df.groupby('ID')
# mean_impf = gb_frog['impf'].mean()
# sem_impf = gb_frog['impf'].sem()
#
# print(mean_impf)
# print(sem_impf)

# This is how to plot the histrogram. Never dspay your data this agregeous way...
# plt.bar(np.arange(4), mean_impf, yerr=sem_impf, ecolor='black',
#         tick_label=['I', 'II', 'III', 'IV'], align='center')
# plt.ylabel('impact force (mN)')

# Now we will do the same thing eve nbeter than the second time using seaborn.
# Forget the for loop and the groupby(), all you need is seaborn and a tidy_df (dataframe).
# This still doesnt make bar graphs okay. Much better to plot all data points.
# sns.barplot(data=df, x='ID', y='impf')
# plt.xlabel('')
# plt.ylabel('impact force (mN)')

# # We are going to create the ultimate graph: A bee swarm plot.
# sns.swarmplot(data=df, x='ID', y='impf')
# plt.margins(0.02)
# plt.xlabel('')
# plt.ylabel('impact force (mN)')
# plt.show()
#
# # Gonna make same graph as above but it colors the point by date.
# ax = sns.swarmplot(data=df, x='ID', y='impf', hue='date')
# ax.legend_.remove()
# plt.margins(0.02)
# plt.xlabel('')
# plt.ylabel('impact force (mN)')
# # plt.gca().legend_.remove()
# plt.show()
# # You can see how to experiementer worked, he did one frog, then the second, then the last two.

# What if we hd thousands of data points and needed to display our data differently
# The bar graph is still not a reasonable alternative. Need to use box plot.
sns.boxplot(data=df, x='ID', y='impf')
plt.margins(0.02)
plt.xlabel('')
plt.ylabel('impact force (mN)')
plt.show()
# The line in the middle is the median, the top and botton box are percentiles.
# The heigt of the box is called the interquartile range.
