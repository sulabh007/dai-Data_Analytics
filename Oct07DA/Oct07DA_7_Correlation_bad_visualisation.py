import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("loan.csv")

#Calculate the correlation coefficent
correlation_coefficent = df['income'].corr(df['age'])

print(f'Correlation Coefficent :', {correlation_coefficent})

#Plot a scatter plot to visualize the data
plt.scatter(df['income'], df['age'])
plt.xlabel('income')
plt.ylabel('age')
plt.title(f'Scatter Plot (Correlation: {correlation_coefficent:.2f})')

#Identify potential outliers (e.g., values with residuals greater than 2 times the standard deviation)
residuals = df['age'] - df['income']
print(residuals)

std_deviation = residuals.std()
outliers = df[abs(residuals) > 2 * std_deviation]

#Hightlight potential outliers on the scatter plot
plt.scatter(outliers['income'], outliers['age'], color= 'red',label='Outliers')
plt.legend()
plt.show()