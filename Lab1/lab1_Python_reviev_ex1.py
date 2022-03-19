import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Data1.csv', index_col=0)

# time series chart
df.plot()

# histogram chart - all parameters
df.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)

# KDE
df.plot.kde()

# # repeated for 2018 year
# df.iloc[365:730] or df.loc['2018-01-01':'2018-12-31']
df.loc['2018-01-01':'2018-12-31'].plot(y = ['theta_1', 'theta_2', 'theta_3', 'theta_4'])

# histogram chart - 4 paramet  ers
df.loc['2018-01-01':'2018-12-31'].hist(column = ['theta_1', 'theta_2', 'theta_3', 'theta_4'], figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)

# KDE
# df.loc['2018-01-01':'2018-12-31'].kde(y = ['theta_1', 'theta_2', 'theta_3', 'theta_4'])
plt.show()