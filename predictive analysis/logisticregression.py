import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

#Uncomment lines to plot and execute the functions
pd.set_option('display.width',320)
pd.set_option('display.max_columns', 40)
data=pd.read_csv("C:/Users/abhishek/Downloads/Bangalore.csv")
print(data.head())
print(data.columns)
print(data.shape)
print(data.describe())
print(data.isnull().sum())
print(data.head())
X=data.drop("Location",axis=1)
y=data["Resale"]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1)
logmodel=LogisticRegression()
logmodel.fit(X_train,y_train)
predictions=logmodel.predict(X_test)
# classification_report(y_test,predictions)
confusion_matrix(y_test,predictions)
accuracy_score(y_test,predictions)