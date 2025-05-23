# -*- coding: utf-8 -*-
"""Predictive Analytics - MLR(cars)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AnfRfnKa8lKfqoOHpqyTOgMh-EJjtLEJ
"""

import pandas as pd

url="/content/drive/MyDrive/Colab Notebooks/cars.csv"

data=pd.read_csv(url)

data.head(6)

data.describe().T

data.isnull().sum()

print(data.duplicated().sum())
data=data.drop_duplicates()
data.shape

data=data[data['Dimensions.Height']>=104]
data=data[data['Dimensions.Width']>=130]
data=data[data['Fuel Information.Highway mpg']<50]

data=data.drop(columns=['Dimensions.Length','Fuel Information.Highway mpg','Engine Information.Engine Type',
                        'Engine Information.Hybrid','Engine Information.Transmission','Identification.ID',
                        'Identification.Make','Identification.Year'])

from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
data['Engine Information.Driveline']=l.fit_transform(data['Engine Information.Driveline'])
data['Fuel Information.Fuel Type']=l.fit_transform(data['Fuel Information.Fuel Type'])
data['Identification.Classification']=l.fit_transform(data['Identification.Classification'])
data['Identification.Model Year']=l.fit_transform(data['Identification.Model Year'])

data.columns

import matplotlib.pyplot as py
import seaborn as sb

py.figure(figsize=(4,3))
sb.kdeplot(data['Dimensions.Height'])
py.show()

py.figure(figsize=(4,3))
sb.kdeplot(data['Dimensions.Width'])
py.show()

py.figure(figsize=(4,3))
sb.kdeplot(data['Engine Information.Engine Statistics.Torque'])
py.show()

py.figure(figsize=(4,3))
sb.kdeplot(data['Engine Information.Engine Statistics.Horsepower'])
py.show()

core=data.corr()
py.figure(figsize=(7,5))
sb.heatmap(core,annot=True)
py.show

data=data.drop(columns=['Engine Information.Driveline','Dimensions.Width',
                        'Engine Information.Number of Forward Gears',
                        'Engine Information.Engine Statistics.Horsepower'])

from scipy.stats import boxcox
data['Dimensions.Height'],_=boxcox(data['Dimensions.Height']+1)
data['Engine Information.Engine Statistics.Torque'],_=boxcox(data['Engine Information.Engine Statistics.Torque']+1)

x=data.drop(columns=['Fuel Information.City mpg']).values
y=data['Fuel Information.City mpg'].values.reshape(-1,1)

from sklearn.preprocessing import StandardScaler
s=StandardScaler()
x_scaled=s.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,train_size=0.75,random_state=42)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)
pred=lr.predict(x_test)

from sklearn.metrics import  mean_squared_error,r2_score
print(mean_squared_error(y_test,pred))
print(r2_score(y_test,pred))

