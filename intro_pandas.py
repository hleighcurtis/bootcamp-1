import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# The structures of numpy can be somewhat limiting. Pandas allows you to use
# your loaded data more like a dictionary and call using keywords.
import pandas as pd

# Load data - problem if there isn't header is that the first data point is
# convereted into a header unless you specificy header=None
df_high = pd.read_csv('data/xa_high_food.csv', comment='#', header=None)
df_low = pd.read_csv('data/xa_low_food.csv', comment='#', header=None)

wc_dict = {'Klose': 16,
            'Ronaldo': 15,
            'Muller': 14,
            'Fontaine': 13,
            'Pele': 12,
            'Koscis': 11,
            'Kinsmann': 11}

s_goals = pd.Series(wc_dict)

nation_dict = {'Klose': 'Germany',
            'Ronaldo': 'Brazil',
            'Muller': 'Germany',
            'Fontaine': 'France',
            'Pele': 'Brazil',
            'Koscis': 'Hungary',
            'Kinsmann': 'Germany'}

s_nation = pd.Series(nation_dict)

df_wc = pd.DataFrame({'nation': s_nation, 'goals': s_goals})

df_wc.loc[df_wc['nation']=='Germany', :]
