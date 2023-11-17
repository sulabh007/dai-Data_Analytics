import pandas as pd

import numpy as np
from scipy import stats

data = pd.read_csv('data_date.csv')
data['Month'] = pd.to_datetime(data['Date']).dt.month

jul_aug_aqi = 

population_mean = 12.0 #Hypothesized population mean

alpha = 0.05

t_statistic, p_value = stats.ttest_2samp(data,population_mean)

if p_value < alpha:
    print("Reject the null hypothesis")
else :
    print("Fail to reject the null hypothesis")
    
print(f"t-statistics: {t_statistic}")
print(f"p-value: {p_value}")


