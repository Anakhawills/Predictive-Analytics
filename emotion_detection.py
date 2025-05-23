# -*- coding: utf-8 -*-
"""Emotion_Detection

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zfqWmHH8A-DQlFmy8i5Lyvexx2VlbfEJ
"""

import pandas as pd
import numpy as np

data=pd.read_csv("https://raw.githubusercontent.com/PoorvaRane/Emotion-Detector/refs/heads/master/ISEAR.csv",names=['emotion','text','unamed'])
data=data.drop(columns=['unamed'])

data["emotion"].unique()

data["emotion"].value_counts()

data=data[data['emotion']!="guit"]

import nltk
nltk.download("punkt_tab")
nltk.download("wordnet")
import string
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
s=set(stopwords.words("english"))

def preprocess(x):
    i=x.lower()
    t=nltk.word_tokenize(i)
    p=[i for i in t if i not in string.punctuation]
    st=[i for i in p if i not in s]
    f=' '.join(st)
    return f

data['text']=data['text'].apply(preprocess)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=8000)
x = vectorizer.fit_transform(data['text'])

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=le.fit_transform(data['emotion'])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=.75,random_state=42)

from sklearn.svm import LinearSVC
model = LinearSVC(dual='auto',random_state=42)

model.fit(x_train,y_train)

pred=model.predict(x_test)

from sklearn.metrics import classification_report
print(classification_report(pred,y_test))

