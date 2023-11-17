import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB

dataset = pd.read_csv("Social_Network_Ads.csv")

#Features: Age,Salary
x = dataset.iloc[:,[2,3]].values
#target variable: Purchased.
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.20, random_state= 0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifier = GaussianNB()
classifier.fit(x_train, y_train)

#Predicting the Test set results
y_pred = classifier.predict(x_test)
print(y_pred) #Our predicted values
print(y_test) #Actual values

from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, f1_score

ac = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred)

print(ac)
print(cm)































