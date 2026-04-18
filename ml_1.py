
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

dff = pd.read_csv("insurance.csv")
print(dff)

"""EDA"""

print(dff.shape)

print(dff.head())

print(dff.info())

print(dff.isnull().sum())

print(dff.describe())

print(dff.columns)

numeric_col = ['age','bmi', 'children','charges']

for col in numeric_col:
  plt.figure(figsize=(6,4))
  hst = sns.histplot(dff[col], kde = True,bins = 20)
  plt.show()
  
print(sns.countplot(x = dff['children']))
plt.show()

print(sns.countplot(x = dff['sex']))
plt.show()

print(sns.countplot(x = dff['smoker']))
plt.show()

print(sns.countplot(x = dff['region']))
plt.show()

for col in numeric_col:
  plt.figure(figsize=(6,4))
  bx = sns.boxplot(x = dff[col])
  plt.show()
