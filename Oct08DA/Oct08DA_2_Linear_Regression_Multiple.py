"""
Output interpretaion
Value of intercept is 4.3345, which shows that if we keep the money spent on TV, Radion
, and Newspaper for advertisement as 0, the estimated average sales will be 4.3345
A singel rupee increase in th money spent on TV for advertisment increases sales by 0.0538,
the money spent on Radio for advertisement increases sales by 0.1100, and the money spent on 
Newspaper of asdvertisment increase sales by 0.0062.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


dataset = pd.read_csv('sales.csv')

#Setting the value for x and y
x = dataset[['tv', 'radio', 'newspaper']]
y = dataset['sales']

#Splitting the dataset
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3,
                                                    random_state= 100)

#Fitting the Multiple Linear Regression model
from sklearn.linear_model import LinearRegression
mlr = LinearRegression()
mlr.fit(x_train, y_train)

#Intercept and Coefficent
print("Intercept: ",mlr.intercept_)
print("Coefficents:")
"""
zip used to print the coefficents (slopes) of the linear regression model for each
pridictor variable (TV, radio, and newspaper) along with the resprective variable
names. This displays the coefficent in a more organized and intepretable format.
x: This represents the DataFrame x that contains the predictor variables (TV, radio, newspaper).

mlr.coef_: This is an attribue of the trained linear regression nodel mlr that
contains the coefficents for each predictor variable. These coefficients represent




"""

print(list(zip(x, mlr.coef_)))
#Prediction of test set
y_pred_mlr = mlr.predict(x_test)
#Predicted values
print("Predicaton for test set: {}".format(y_pred_mlr))

#Actual value and the pridicted value
mlr_diff = pd.DataFrame({'Actual value': y_test, "Predicted vare": y_pred_mlr})
print(mlr_diff)

#Model Evalution
"""
R Squrared: R Square is the coefficnet of determination. It tells us how many points
fall on the regression line. The value or R Square is 90.11, which indicates that
90.11% of hte data fit the regression model.
Mean Absolute Error: Mean Absolute Error is the abosoule diffenrence between the actual
or true values and the predicted values. The lower the value, the better is the model's
performance. A mean absolute error of 0 means that your model is a perfect predictor of 
the outputs. The mean absolute error obtained for this particular model is 1.277, 
which is pretty good it is close to 0. 
Mean Squre Error: Mean Square Error is calculated by taking the average of the
squre of the difference between the original and predicted values of the data.

Root Mean Square Error:

"""
from sklearn import metrics
meanAbErr = metrics.mean_absolute_error(y_test, y_pred_mlr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))
print('R squared: {:.2f}'.format(mlr.score(x, y)*100))
print('Mean Absolute Error:',meanAbErr)
print('Mean Square Error:',meanSqErr)
print('Root Mean Squrare Error',rootMeanSqErr)

print(y_test)

#Plotting actual vs. predicted values
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred_mlr, color='blue')
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs. Predicted Values (Mulltiple Linear Regression)")
plt.grid(True)
plt.show()












































