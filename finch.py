import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)


#Load the data.
df_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
df_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
df_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
df_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
df_2012 = pd.read_csv('data/grant_2012.csv', comment='#')

# First, change the name of the yearband column of the 1973 data to year.
# Also, make sure the year format is four digits, not two!
df_1973 = df_1973.rename(columns={'yearband' :'year',
                            'beak length': 'beak length (mm)',
                            'beak depth': 'beak depth (mm)'})
df_1973['year']=1973


# Add year to other files
df_1975['year']=1975
df_1987['year']=1987
df_1991['year']=1991
df_2012['year']=2012


# Change the column names so that all the DataFrames have the same column
# names. I would choose column names
df_1975 = df_1975.rename(columns={'Beak length, mm' : 'beak length (mm)',
                            'Beak depth, mm':'beak depth (mm)'})
df_1987 = df_1987.rename(columns={'Beak length, mm' : 'beak length (mm)',
                            'Beak depth, mm':'beak depth (mm)'})
df_1991 = df_1991.rename(columns={'blength' : 'beak length (mm)',
                            'bdepth':'beak depth (mm)'})
df_2012 = df_2012.rename(columns={'blength' : 'beak length (mm)',
                            'bdepth':'beak depth (mm)'})


# Concatenate the DataFrames into a single DataFrame. Be careful with indices!
# If you use pd.concat(), you will need to use the ignore_index=True kwarg.
# Concatinating data (axis = one means turn into columns rather than rows)
df_grant = pd.concat((df_1973, df_1975, df_1987, df_1991, df_2012), ignore_index=True)
# This time the index is ignored becasue it is arbitary numbering but would mess up the merge.
# IF they had indexed by the band name instead it would have been a different story....


# Delete duplicate birds from the same year.
df_grant = df_grant.drop_duplicates(subset=['year', 'band'])


# Save CSV file.
df_grant.to_csv('grant_combined.csv', index=False)


# Plot an ECDF of beak depths of Geospiza fortis specimens measured in 1987.
# Plot an ECDF of the beak depths of Geospiza scandens from the same year. T
# These ECDFs should be on the same plot. On another plot, plot ECDFs of beak
# lengths for the two species in 1987. Do you see a striking phenotypic difference?
fortis_1987dep = df_grant.loc[(df_grant['year']==1987) & (df_grant['species']=='fortis'), 'beak depth (mm)']
scandens_1987dep = df_grant.loc[(df_grant['year']==1987) & (df_grant['species']=='scandens'), 'beak depth (mm)']
# Bug: if you take out series (single column) you dont put [],
# This is an example of a sematic error ....

x_fortis87, y_fortis87 = bootcamp_utils.ecdf(fortis_1987dep)
x_scan87, y_scan87 = bootcamp_utils.ecdf(scandens_1987dep)

# plt.plot(x_fortis87, y_fortis87, marker='.', linestyle='none', alpha=0.5)
# plt.plot(x_scan87, y_scan87, marker='.', linestyle='none', alpha=0.5)
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.show()


# For the 1987 data, plot beak depth vs. beak width for Geospiza fortis as blue
# dots, and for Geospiza scandens as red dots. Can you see the species demarcation?
fortis_87len = df_grant.loc[(df_grant['year']==1987) & (df_grant['species']=='fortis'), 'beak length (mm)']
scandens_87len = df_grant.loc[(df_grant['year']==1987) & (df_grant['species']=='scandens'), 'beak length (mm)']

plt.close()
# plt.plot(fortis_1987dep, fortis_87len, marker='.', linestyle='none', alpha=0.5)
# plt.plot(scandens_1987dep, scandens_87len, marker='.', linestyle='none', alpha=0.5)
# plt.xlabel('beak depth (mm)')
# plt.ylabel('width')
# plt.show()


# Do above again for all years. Describe what you see. Do you see the changes
# in the differences between species (presumably as a result of hybridization)?
# In your plots, make sure all plots have the same range on the axes.
fortis_len = df_grant.loc[(df_grant['species']=='fortis'), 'beak length (mm)']
scandens_len = df_grant.loc[(df_grant['species']=='scandens'), 'beak length (mm)']
fortis_dep = df_grant.loc[(df_grant['species']=='fortis'), 'beak depth (mm)']
scandens_dep = df_grant.loc[(df_grant['species']=='scandens'), 'beak depth (mm)']

plt.plot(fortis_dep, fortis_len, marker='.', linestyle='none', alpha=0.5, markersize=15)
plt.plot(scandens_dep, scandens_len, marker='.', linestyle='none', alpha=0.5, markersize=15)
plt.plot(fortis_1987dep, fortis_87len, marker='.', linestyle='none', alpha=0.5)
plt.plot(scandens_1987dep, scandens_87len, marker='.', linestyle='none', alpha=0.5)
plt.xlabel('beak depth (mm)')
plt.ylabel('width')
plt.show()
