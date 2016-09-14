import numpy as np
import pandas as pd

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Extract the impact time of all impacts that had an adhesive strength of
# magnitude greater than 2000 Pa.
pa_2000 = df[df['adhesive strength (Pa)'] > -2000]
pa_2000.loc[:, 'impact time (ms)']

# Extract the impact force and adhesive force for all of Frog II's strikes.
df.loc[df['ID']=='II', ['impact force (mN)', 'adhesive force (mN)']]

# Extract the adhesive force and the time the frog pulls on the target
# for juvenile frogs (Frogs III and IV).
df.loc[df['ID'].isin(['III', 'IV']), ['impact time (ms)', 'adhesive force (mN)', 'ID']]

# Extract all of Frog I's impact forces and compute the mean.
mean_1 = np.mean(df.loc[df['ID']=='I', ['impact force (mN)']])

# Do the same for the other three frogs.
# We only want ID's and impact forces, so slice those out
df_impf = df.loc[:, ['ID', 'impact force (mN)']]
# Make a GroupBy object
grouped = df_impf.groupby('ID')
# Apply the np.mean function to the grouped object
df_mean_impf = grouped.apply(np.mean)
# Look at the new DataFrame
df_mean_impf
