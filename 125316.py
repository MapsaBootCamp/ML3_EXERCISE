import pandas as pd
import numpy as np
train = pd.read_csv('travel_insurance/train.csv')
# 1- Number of rows and column
print(len(train), len(train.columns))
# or
# print(train.shape)
# print(train.columns)

# 2- Anuall income mean
print(int(train["AnnualIncome"].mean()))

# 3- Travel history
print(train['EverTravelledAbroad'].value_counts()['Yes'])

# 4- Private or Govermental:
print((train['Employment Type'].value_counts(
    normalize=True) * 100).round(decimals=2).max())

# 5- Insurance Percentage
print((train['TravelInsurance'].value_counts(
    normalize=True)['Yes'] * 100).round(decimals=2))
