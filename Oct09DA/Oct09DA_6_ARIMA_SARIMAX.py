import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


data = {
        'Month' : pd.date_range(start='2019-01-01',periods=36,freq='M'),
        'Sales' : [100, 120, 130, 150, 200, 220, 250, 230, 210, 180, 160, 140,
                   110, 130, 150, 190, 220, 240, 260, 250, 230, 200, 180, 160,
                   130, 140, 160, 190, 210, 240, 270, 250, 230, 200, 210, 190],
        'AdvertisingSpend' : [50, 60, 70, 80, 90, 100, 110, 110, 120, 130, 140, 150, 160, 
                              60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 70,
                              80, 90, 100, 110, 120, 130, 140, 150, 160, 70, 120]
        }

df = pd.DataFrame(data)
df.set_index('Month' , inplace=True)

#Fit an ARIMA model to the Sales data
order = (2, 1, 1) #(p, d, q) order
model = ARIMA(df['Sales'], order=order)
result = model.fit()

#Forecast future Sales values
forecast_steps = 12
forecast = result.forecast(steps=forecast_steps)

#Plot the original data and the ARIMA forecast
plt.figure(figsize=(12,6))
plt.plot(df['Sales'],label='Actual Sales')
plt.plot(pd.date_range(start=df.index[-1],periods=forecast_steps, freq='M'),
         forecast,label = 'ARIMA Forecast', color = 'red')
plt.xlabel("Month")
plt.ylabel('ARIMA Forecast for Sales')
plt.legend()
plt.show()

#Fit a SARIMAX model to the sales data with AdvertisingSpend as an exogenous variable
from statsmodels.tsa.statespace.sarimax import SARIMAX

"""
SARIMAX allows us to incoporate additional external factors (exogenous variables) that can
influence the time series we are trying to forecast. In this case, we are using 
the 'AdervertisingSpend' varibale as an exogenous variabel. If this variable has a significat
impact on 'Sales' including it in the model can improve the accuracy of the forecast.

SARIMAX includes seasonal components (P, D, Q, s) that can capture seasonality in the data.
If our data exhibits seasonal patterns (e.g., sales are higer during specific months of the year),
SARIMAX can model and forecast these patterns more effectively.

SARIMAX allows us to specify both non-seasonal (p, d, q) and seasonal P, D, Q, s) orders. This
flexibility enables us to tailor the model to the specific charachteristics of our data, In the
provided code, we have chosen an order (2, 1, 1) and seasonal_order of (1, 1, 1, 12), which may 
better capture the data's behaviour compared to the ARIMA order.
"""

order = (2, 1, 1) #(p, d, q)
seasonal_order = (1, 1, 1, 12) #(P, D, Q, s) seasonal order
exog = df['AdvertisingSpend']

model = SARIMAX(df['Sales'], exog=exog, order=order, seasonal_order=seasonal_order)
results = model.fit()

#Forecast future Sales values
forecast_steps = 24 
forecast = result.get_forecast(steps=forecast_steps, exog= df.iloc[-forecast_steps:] ['AdevertisingSpend'])

#Plot the orignal Sales data, Advertising, and the SAR
plt.figure(figsize=(12,6))
plt.plot(df['Sales'], label='Actual Sales')
plt.plot(df.index[-forecast_steps:],df['AdevertisingSpend'][-forecast_steps:],label='AdevertisingSpend',
         linestyle='--',color='red')
plt.xlabel('Month')
plt.ylabel('Sales/ Adevertising Spend ')
























