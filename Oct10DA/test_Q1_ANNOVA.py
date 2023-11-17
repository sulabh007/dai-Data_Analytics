"""
Que 1: Apply Hypothisis test to check if AQI if July and August months, all over the 
world, are significantly different or same (5marks)
"""

"""
Analysis of variance: The purpose of ANVOA is to test if there is any significant
difference the means of two or more groups. we asuume

H0 (null hypothesis) : u1 = u2 = u3 =...uk(it implies that the eans of all
"""

from scipy.stats import f_oneway
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('data_date.csv')

print(df.dtypes) #check data types

#convert Date column into datetime type
df['date_modified'] = pd.to_datetime(df['Date'])
print(df.head())
print(df.dtypes)  #check data types

#Now drop the original Date column and rename the new column as Date, then make it the first
#column
df.drop(['Date'],axis = 1, inplace=True)
df.rename(columns = {'date_modified' : 'Date'}, inplace=True)
df = df[['Date','Country','Status','AQI Value']]
print(df.head())
print(df.dtypes)

#Filter only for July and August data
df = df[(df['Date'].dt.month == 7) | (df['Date'].dt.month == 8)]
#group_by_country_date = df.groupby(["Country","Date"])
#print(group_by_country_date.head())

#Group by country and get a list of all the AQI values for that country for July and August
result = df.groupby('Country')['AQI Value'].apply(list)
print(result)

#Run ANOVA
F, p = f_oneway(*result)
print(F)
print(p)

#Conclusion: p = 0. Since the p-value is less than 0.05 hence we would reject the H0.
print("Since p value is < 0.05, we reject the null hypothesis, so there is a difference between the mean AQI values of different countries")

#Draw a histogram
means = df.groupby("Country")["AQI Value"].mean()
plt.bar(means.index.tolist(),means.values.tolist())
plt.xticks(rotation=90)
plt.title('HISTOGRAM COUNTRY V/S AQI Value', color='hotpink')
plt.xlabel('Country~~~~~>',color="navy")
plt.ylabel('AQI Value~~~~~>',color="navy")
plt.show()


















