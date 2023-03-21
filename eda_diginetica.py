import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# read csv and convert datatype
df = pd.read_csv('new_diginetica.csv', sep=';', dtype={'SessionID':str, "ItemID":str})
df['Time']= df['Time'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').timestamp())


df.describe(include='all')
# shape: (1235380,3)
# 310324 unique sessions; max_len = 87
# 122993 unique items; max_len = 1270
# timestamp: 1451578000 ~ 1464710000; about 152 days

session_len = df.groupby('SessionID').size()
session_len.describe(percentiles=[.1,.2,.3,.4,.5,.6,.7,.8,.9])
# ~20% 1
# ~40% 2
# ~50% 3
# ~70% 4
# ~80% 6
# ~90% 9

item_len = df.groupby('ItemID').size()
item_len.describe(percentiles=[.1,.2,.3,.4,.5,.6,.7,.8,.9])
# ~30% 1
# ~40% 2
# ~50% 3
# ~60% 4
# ~70% 6
# ~80% 10
# ~90% 12

'''
fig, axes = plt.subplots(2, 1, figsize=(12,16))
sns.distplot(ax=axes[0], a=session_len.values)
sns.distplot(ax=axes[0], a=item_len.values)

for ax in axes:
    ax.tick_params(axis='x', labelrotation=90)

plt.show()
'''



