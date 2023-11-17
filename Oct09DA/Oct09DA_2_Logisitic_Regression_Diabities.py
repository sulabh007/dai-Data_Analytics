import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("diabetes.csv")
print(df)

#Split the dataset into predictor vairables X (All columns except "Outcome") and
# the target variable y ("Outcome")

x = df.drop('Outcome', axis='columns')
y = df['Outcome']

print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=1)

from sklearn.linear_model import LogisticRegression
#'liblinear' : This solver is suitable for small to medium-sized datasets.
classifier = LogisticRegression(solver='liblinear')
classifier.fit(x_train,y_train)

y_test_prediction = classifier.predict(x_test)
print(y_test_prediction)

comparison = pd.DataFrame({'Actual': y_test,'Predicted': y_test_prediction})
print(comparison[0:10])

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_test_prediction))

y_train_prediction = classifier.predict(x_train)
print(accuracy_score(y_train,y_train_prediction))

from sklearn.metrics import confusion_matrix
#
conf_mat=confusion_matrix(y_test, y_test_prediction)
print(conf_mat)

#
plt.figure(figsize=(12,6))
sns.heatmap(conf_mat, annot=True,fmt='d')
plt.title("Confusion Matrix of test data")
plt.xlabel("Predicted value")
plt.ylabel("Actual value")
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_test_prediction))

TN=conf_mat[0][0]
FP=conf_mat[0][1]
FN=conf_mat[1][0]
TP=conf_mat[1][1]

recall= TP/(TP+FN)
print("Recall=",recall)
precision=TP/(TP+FP)
print("Precision=",precision)
specificity=TN/(TN+FP)
print("Specificity",specificity)
accuracy=(TP+FN)/(TP+FP+FN+TN)
print("Accuracy:",accuracy)


























