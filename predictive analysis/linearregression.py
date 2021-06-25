import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.set_option('display.width',320)
pd.set_option('display.max_columns', 40)
data=pd.read_csv("C:/Users/abhishek/Downloads/Bangalore.csv")
print(data.head())
print(data.columns)
print(data.shape)
print(data.describe())
print(data.isnull().sum())
print(data.head())
train = data.drop(['Price','Location'], axis=1)
test = data['Price']
X_train,X_test,y_train,y_test=train_test_split(train,test,test_size=0.3,random_state=2)
regr = LinearRegression()
regr.fit(X_train,y_train)
pred = regr.predict(X_test)
print(pred)
print(regr.score(X_test,y_test))
sns.countplot(x='SwimmingPool',hue='Hospital',data=data)
plt.show()
data["No. of Bedrooms"].plot.hist()
sns.countplot(x='No. of Bedrooms',data=data)
data["Price"].plot.hist(bins=20,figsize=(10,5))
plt.show()
data.info()
print(data.isnull())
print(data.isnull().sum())
sns.heatmap(data.isnull(),yticklabels=False,cmap="viridis")
plt.show()