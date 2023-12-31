# -*- coding: utf-8 -*-
"""MLops assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BkryMfPQNukPw95Hkq8NZjaA162Cz-_G
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data=pd.read_csv('/content/Iris.csv')
data.head()

data.isnull().sum()

data.columns

a=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm','Species']
for i in a:
  print(i,data[i].nunique())

x=data.drop('Species',axis=1)
y=data['Species']

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(random_state=42)
model=rf.fit(xtrain,ytrain)
p=model.predict(xtest)

from sklearn.metrics import accuracy_score

accuracy_score(ytest,p)*100



