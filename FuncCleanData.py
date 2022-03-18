import pandas as pd
import numpy as np

df = pd.read_csv('example.csv')
print(df)
print(df.apply(np.mean, axis=0))

import re

from numpy import NaN
pattern = re.compile('^\$\d*\.\d{2}$')
def my_function (input1, input2):
    #Function Body
    return value
def diff_money(row, pattern):
    icost = row['Initial Cost']
    tef = row['Total Est. Fee']

    if bool(pattern.match(icost)) and bool(pattern.match(tef)):
        icost = icost.replace("$","")
        tef = tef.replace("$","")

        icost = float(icost)
        tef = float(tef)

        return icost - tef
    else:
        return(NaN)

df_subset = pd.read_csv('data_function.csv')
df_subset['diff'] = df_subset.apply(diff_money, axis=1, pattern=pattern)
print(df_subset.head())
