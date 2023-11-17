import pandas as pd

dataset = pd.read_csv('salary.csv')

x = dataset.iloc[:,0].values
y = dataset.iloc[:,1].values

#Step 2: Split data into training and testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3, random_state=0)

#step3: Fit simple Linear Regression to Training Data
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

#Step 4 :  Make Prediction
y_pred = regressor.predict(x_test)
print(y_pred)

#Step 5: Visualize traning set results
import matplotlib.pyplot as plt
#Plot the actual data points of training set
plt.scatter(x_train, y_train, color='red')
#Plot the regression line
plt.plot(x_train, regressor.predict(x_train),color="blue")
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel("Salary")
plt.show()

#Step 6 - Visualize test set results
import matplotlib.pyplot as plt
#Plot the actual data points of test set
plt.scatter(x_test, y_test, color='red')
#plot the regression line (same as above)
plt.plot(x_test, regressor.predict(x_test),color="blue")
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel("Salary")
plt.show()

#Step 7 - Make new prediction
new_salary_pred = regressor.predict([[15]])
print('The predicted salary of a person with 15 years experience is ',new_salary_pred)
new_salary_pred = regressor.predict([[5]])
print('The predicted salary of a person with 5 years experience is ',new_salary_pred)
new_salary_pred = regressor.predict([[25]])
print('The predicted salary of a person with 25 years experience is ',new_salary_pred)
new_salary_pred = regressor.predict([[0]])
print('The predicted salary of a person with 0 years experience is ',new_salary_pred)
new_salary_pred = regressor.predict([[1]])
print('The predicted salary of a person with 1 years experience is ',new_salary_pred)



for i in range(36):
    new_salary_pred = regressor.predict([[i]])
    print(f'The predicted salary of a person with {i} years experience is ',new_salary_pred)

    































