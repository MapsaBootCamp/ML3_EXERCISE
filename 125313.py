import nltk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
supermarket = pd.read_csv('supermarket.csv')
# 1- Number of unique products:
print(supermarket.Product.nunique())

# 2-sale percentage based on dates:
print((supermarket['Date'].value_counts(
    normalize=True)*100).mean().round(decimals=2))

# 3- Number of least bought products:
print(supermarket['Product'].str.split(
    ' ').explode().value_counts().nsmallest(5))

# 4- 5 top customers in 2020:
contain_values = supermarket[supermarket['Date'].str.contains('2020')]
print(contain_values['Customer Id'].value_counts().nlargest(5))

# 5- most day sells:
supermarket['Day'] = (supermarket['Date']).astype('datetime64').dt.day_name()
print(supermarket['Day'].value_counts().nlargest(1))
# 6- 5 most support products:
frequency = supermarket['Product'].str.split(' ').explode().value_counts()
frequency = frequency.rename_axis(
    'item').reset_index(name='counts')
print(frequency)
nltk.download()
