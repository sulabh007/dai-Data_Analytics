import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import time

#Students performance in Math
students_data = pd.read_csv('student-mat.csv')

print(students_data.describe())

col_str = students_data.columns[students_data.dtypes == object]
print(col_str)

#Convert each category value into a new colunm and assign a 1 or 0 (True/False)
#value to the column. This has the benefit of not weighting a value impoperly. Simplest
#method is using pandas .get_dummies() method
#drop_first = True reduces extara column creation (eg. coint tos, is_head and is_tail: 
#    both are not needed)
students_data = pd.get_dummies(students_data, columns= col_str, drop_first=True)
print(students_data.info())

print(students_data[['G1','G2','G3']].corr())
#Since G1, G2,G3 have very high correlation, we can drop G1,G2

students_data.drop(axis = 1,labels=['G1','G2'])

#Drop the G3 column, because we want to predict it now
lable = students_data['G3'].values
predictor = students_data.drop(axis=1, labels= ['G3']).values
print(students_data.shape)

#Using Linear Regression to predict grades
lr = linear_model.LinearRegression()

#cross_val_score: Used during the testing and validation phase of your machine learning model
#development

#Trains and tests a model over multiple folds of your dataset. This cross validation method
#gives you a better understanding of model performance over the whoel dataset instead of just 
#a single train/test split.

"""
The number of folds is defined, by default this is 5
The dataset is split up according to these folds, where each fold has a unique set of testing data
A model is trained and tested for each fold
Each fold returns a metric for it's test data
The mean and standard deviation of these metrics can then be calcualted to provide a single
metric fot the process
"""
#Returns an array of scores of hte estimator for each run of the coress validation
lr_score = cross_val_score(lr, predictor, lable , cv=5) #Five runs five times
print('LR M0del Cross Validation score :'+ str(lr_score))

#Average of all thoes means
print('LR M0del Cross Validation Mean score :'+ str(lr_score))



#Using PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=len(students_data.columns)-1)
pca.fit(predictor)
variance_ratio = pca.explained_variance_ratio_
print([pca.explained_variance_.shape])

#Now Plot 
import matplotlib.pyplot as plt

#Find cumulative varaince, adding one independent variable at atime
variance_ratio_cum_sum = np.cumsum(variance_ratio)
print(variance_ratio_cum_sum)

#This cumulative explained variance graph helps us to choose the number of desired princepal
#components. If we look at the above print statment's output, we will reliaze that 90% variation
# is the data is explained by the first 6 princepal components. Hence we annotate 6 on the graph.

plt.plot(variance_ratio_cum_sum)
plt.xlabel("Number of componets")
plt.ylabel("Cummulative Explained vairance")





#Anonate 90% variance explained by the first 6 variables only
plt.annotate(6, xy=(6,.90))
plt.show()

#Indivisual explained varaince, instead of cummulative variance
#We see that the first variable causes 


plt.bar(range(41),pca.explained_variance_,alpha=0.5, label='indivisual explained variance')
plt.xlabel('Explained varaince ratio')
plt.ylabel('Principal components')
plt.legend(loc='best')
plt.show()

import seaborn as sns
correlation = pd.DataFrame(predictor).corr()
sns.heatmap(correlation, vmax=1, square=True, cmap='Greens')
plt.title('Correlation between different fetures')
plt.show()

pca=PCA(n_components=6)
pca.fit(predictor)
Transformed_vector = pca.fit_transform(predictor)
print(Transformed_vector)

correlation = pd.DataFrame(Transformed_vector).corr()
sns.heatmap(correlation, vmax=1,square=True,cmap='viridis')
plt.title('Correlation between different features')
plt.show()

#Check the performance with 6 variables
lr_pca = linear_model.LinearRegression()
lr_pca_score = cross_val_score(lr_pca, Transformed_vector,lable,cv=5)
print('PCA Model Corss validation score :' + str(lr_pca_score))
print('PCA Model Corss validation Mean score :' + str(lr_pca_score.mean()))
#We see values similar to the earlier case when we had 40 independet variable
#This means that PCA has indedd reduced 40 variables to 6 without causing any negative impact










































































