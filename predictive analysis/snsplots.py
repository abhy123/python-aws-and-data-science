import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.width',320)
pd.set_option('display.max_columns', 40)
data=pd.read_csv("C:/Users/abhishek/Downloads/Bangalore.csv")
print(data.head())
print(data.columns)
print(data.shape)
print(data.describe())
print(data.isnull().sum())
print(data.head())
sns.relplot(x='Price', y='Area', hue='Resale', data=data)
plt.show()
