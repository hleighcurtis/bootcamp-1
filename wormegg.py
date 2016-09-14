import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# The structures of numpy can be somewhat limiting. Pandas allows you to use
# your loaded data more like a dictionary and call using keywords.
import pandas as pd

# Load data. df stands for 'data frame'
df_high = pd.read_csv('data/xa_high_food.csv', comment='#', header=None)
df_low = pd.read_csv('data/xa_low_food.csv', comment='#', header=None)

df_high.columns = ['High']
df_low.columns = ['Low']

# Concatinating data (axis = one means turn into columns rather than rows)
df = pd.concat((df_low, df_high), axis=1)

# Save a new file for combined data but say index is false casue they don't
#have meaning in this specific situaaion.
df.to_csv('xa_combined.csv', index=False)
# the two data files have different lengths and the empty areas are filled
# with "NaN" but this doesnt interefer with dr.mean() or other statistics.

# There is no relation between the rows so need to tidy up data set.
# One observation, one row. Each column is a feature of each observation.
df_tidy = pd.melt(df, var_name='food density',
                value_name='Cross-sectional area (sq. micron)').dropna()

df_tidy.loc[(df_tidy['food density']=='low') &
                (df_tidy['Cross-sectional area (sq. micron)']), :]
