import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load the data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Take a look
df

# Slice out big forces
df_big_force = df[df['impact force (mN)'] > 1000]
# Look at it
df_big_force

df.loc[42, :]
df.loc[:, ['impact force (mN)', 'adhesive force (mN)']]

# Getting these stats from only frog 1
df['ID']=='1'
df.loc[df['ID']=='1', ['impact force (mN)', 'adhesive force (mN)']]

plt.plot(df['impact force (mN)'], ['adhesive force (mN)'],
                        marker='.', linestyle='none')
df.plot(x='total contact area (mm2)', y='adhesive force (mN)',
                        kind='scatter')

# Find if the graph has a positive or negative correclation.
df.corr()
df.loc[:, ['impact force (mN)', 'adhesive force (mN)']].corr()

# Rename the impact force column
df = df.rename(columns={'impact force (mN)': 'impf'})
# Don't forget to assign this fuction to the varaible for it to
#cause permanet change.
