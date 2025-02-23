import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('data.csv')
df

df.info()
print(f"The Laptop Price Dataset has {df.shape[0]} rows and {df.shape[1]} columns")
print(df.isnull().sum())

print(df.isnull().sum())

print(df.duplicated().sum())

print(df.columns.to_list())

print(df['brand'].value_counts())


