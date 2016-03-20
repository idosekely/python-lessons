import pandas as pd
import numpy as np
__author__ = 'sekely'

'''
based on http://pandas.pydata.org/pandas-docs/stable/10min.html
'''

dates = pd.date_range('20160101 1200', periods=10, freq='min')
df = pd.DataFrame(np.random.randn(10,4), index=dates, columns=list('ABCD'))

df.describe()  # returns count, mean, std, min, 25%, 50%, 75%, max for each column

# sorting by column
df.sort_values(by='B')

# selecting a specific column
print df['B']

# selecting rows
print df['20160101 1201':'20160101 1203']

# select column and row
print df.loc['20160101 1201':'20160101 1203', ['B']]

# selecting by boolean expression
print df[df.A > 0]

# creating graphs
plot1 = df.plot()
plot2 = df.plot(kind='bar')
plot1.figure.show()
plot2.figure.show()
