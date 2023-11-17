import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Find available dataset names in seaborn
print(sns.get_dataset_names())

df = sns.load_dataset('flights')
print(df.head)
#we get only year and month for the date, we need day also

#Convert the date to a YYYY-MM-DD format in a new column named yearMonth
df['yearMonth'] = '01-'+df['month'].astype(str)+'-'+df['year'].astype(str)
print(df.info())

#yearMonth is of type object - we may have problems later, so convert it into datetime.
df['yearMonth'] = pd.to_datetime("01-"+df['month'].astype(str)+"-"+df['year'].astype(str))
print(df.info())
print(df.head())

#Make yearWorth column as the dataframe index
df.set_index('yearMonth',inplace=True)#inplace will make the chage permanent to the DF
print(df.head())

#Now plot
plt.figure(figsize=(10,5))
sns.lineplot(data=df,x=df.index,y=df.passengers)
plt.show()

#The graph will show pattern (eg. seasonality - data going up and down)
#Refer to this slides for explanation
#We see in our graph two pattern : seasonality and trend

#Calculate and plot rolling mean and standard deviation for 12 months
df['rollMean'] = df.passengers.rolling(window=12).mean()
df['rollStd'] = df.passengers.rolling(window=12).std()

print(df['rollMean'])
print(df['rollStd'])

plt.figure(figsize=(10,5))
sns.lineplot(data=df,x=df.index,y=df.passengers)
sns.lineplot(data=df,x=df.index,y=df.rollMean)
sns.lineplot(data=df,x=df.index,y=df.rollStd)
plt.show()

#Conclusion : Mean is not statinory,SD is stationary; so our data is not stationary
#Now let us perform the ADF test
from statsmodels.tsa.stattools import adfuller

adfTest = adfuller(df['passengers'])
print(adfTest) #Let us interpret these values below by converting into a series

stats = pd.Series(adfTest[0:4],index=['Test Statistics','p-value','#lags used',
                                      'number of observations used'])
print(stats)
for key, values in adfTest[4].items():
    print('criticality', key,':',values)
    
#we will see that our Test statistic > Critical value in all the cases, so we do
#not reject the null hypothesis. It means that our data is not stationary.


def test_stationarity(dataframe, var):
    dataframe['rollMean'] = dataframe[var].rolling(window=12).mean()
    dataframe['rollStd'] = dataframe[var].rolling(window=12).std()
    
    from statsmodels.tsa.stattools import adfuller
    
    adfTest = adfuller(dataframe[var])
    print(adfTest) 
    
    stats = pd.Series(adfTest[0:4],index=['Test Statistics','p-value','#lags used',
                                          'number of observations used'])
    print(stats)
    for key, values in adfTest[4].items():
        print('criticality', key,':',values)
        
    plt.figure(figsize=(10,5))
    sns.lineplot(data=dataframe,x=dataframe.index,y=var)
    sns.lineplot(data=dataframe,x=dataframe.index,y='rollMean')
    sns.lineplot(data=dataframe,x=dataframe.index,y='rollStd')
    plt.show()

#Just get the passnagers column into a new dataframe for easier testing
air_df = df[['passengers']].copy()#Double brackets because it is a list within a list
print(air_df.head())

#By default, shift is by 1 time period (here, one month)
#Create a new column which will contain the shifted value from passnagers column - see slide

air_df['shift'] = air_df.passengers.shift(10)
air_df['shiftDiff'] = air_df['passengers'] - air_df['shift']
print(air_df.head(20))

#Test stationarity
test_stationarity(air_df.dropna(), 'shiftDiff')
#Conclusion : The data has become somewhat stationary


#Create column for one month and one year lagged data
airP = df[['passengers']].copy(deep=True)
airP['firstDiff'] = airP['passengers'].diff()
airP['Diff12'] = airP['passengers'].diff(12)#This will be used later in SARIMAX

print(airP.head())

#Now ARIMA
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_pacf(airP['firstDiff'].dropna(), lags=20)
plt.show()
#Shaded area is insignificant area
#PACF gives us the auto regressive values (i.e. p - Refer to the slides)
#First 'p' is 1 (the x-axis coordinate), whoes value is ~0.31 (the y-axis coordinate)

#So, significant p values are 1, 2, 4, 6, etc)

#Now let us take this value as p and find q, for which we need ACF
plot_acf(airP['firstDiff'].dropna(),lags=20)
plt.show()

# Results of ACF are similar to that of PACF
# Interpretation: We got q. Significant q values are 1, 3, 4, 8, etc) 

# Let us take p = 1, q = 3 (both are significant) and d = 1 (already known)

# Build ARIMA model
train = airP[:round(len(airP)*70/100)] # Take the first 70% data
print(train.tail()) # Just to check where it ends

test = airP[round(len(airP)*70/100):] # Take the last 30% data, starting from 71%
print(test.head()) # Just to check where it starts

model = ARIMA(train['passengers'],order=(1,1,3)) # Parameters: p, d, q
model_fit = model.fit()
prediction = model_fit.predict(start=test.index[0],end=test.index[-1])
airP['arimaPred'] = prediction
print(airP.tail())

# Plot

sns.lineplot(data=airP,x=airP.index,y='passengers')
sns.lineplot(data=airP,x=airP.index,y='arimaPred' ,label="ARIMA pred")
plt.legend()
plt.show()

# Conclusion: The ARIMA prediction is not good


#Now SARIMAX

from statsmodels.tsa.statespace.sarimax import SARIMAX


train = airP[:round(len(airP)*70/100)] # Take the first 70% data
test = airP[round(len(airP)*70/100):] # Take the last 30% data, starting from 71%

# First ARIMA prediction
model = ARIMA(train['passengers'],order=(1,1,3)) # Parameters: p, d, q
model_fit = model.fit()
prediction = model_fit.predict(start=test.index[0],end=test.index[-1])
airP['arimaPred'] = prediction

# Now SARIMAX prediction
model = SARIMAX(train['passengers'],order=(1,1,3),seasonal_order=(2,1,2,12))
model_fit = model.fit()
prediction = model_fit.predict(start=test.index[0],end=test.index[-1])
airP['sarimaxPred'] = prediction
print(airP.tail())
# Data looks better

# Plot
airP.dropna()
print(airP.head())
sns.lineplot(data=airP,x=airP.index,y='passengers')
sns.lineplot(data=airP,x=airP.index,y='sarimaxPred')
sns.lineplot(data=airP,x=airP.index,y='arimaPred')
plt.show()

# Compared to ARIMA, SARIMAX is much better

# Future prediction

# First check the last date in our dataset
print(airP.tail())

# MS: Month Start frequency
# Create a data frame to hold index values from 01.01.61 to 01.12.62
futureDate = pd.DataFrame(pd.date_range(start='1961-01-01', end='1962-12-01',freq='MS'),columns=['Dates'])
futureDate.set_index('Dates',inplace=True)
print(futureDate.head())

# Predict and print
print(model_fit.predict(start=futureDate.index[0],end=futureDate.index[-1]))

# Plot

airP.dropna()
sns.lineplot(data=airP,x=airP.index,y='passengers')
sns.lineplot(data=airP,x=airP.index,y='sarimaxPred')
sns.lineplot(data=airP,x=airP.index,y='arimaPred')
model_fit.predict(start=futureDate.index[0],end=futureDate.index[-1]).plot(color='black')
plt.show()
