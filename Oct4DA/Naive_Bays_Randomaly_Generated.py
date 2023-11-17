#Generate a dummy dataset and run navie bays algorithm
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

x,y = make_classification(
        n_features=6,
        n_classes=3,
        n_samples=800,
        n_informative=2,
        random_state=1,
        n_clusters_per_class=1,)

print(x)
print(y)
print(x[:,0])
print(x[:,1])


plt.scatter(x[:,0],x[:,1],c=y, marker='+');
plt.show()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.33, random_state=125)

from sklearn.naive_bayes import GaussianNB
#Build a Guassian Classifier
model = GaussianNB()

model.fit(x_train, y_train)

predicted = model.predict([x_test[6]])

print("Actual Value:", y_test[6])
print("Predicted Value:",predicted[0])

y_pred = model.predict(x_test)

#Now check model accuracy
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score)

accuracy = accuracy_score(y_pred, y_test)
f1 = f1_score(y_pred, y_test, average="weighted")

print("Accuracy:", accuracy)

print("F1 Score:", f1)
