import numpy as np
from scipy import stats

data = np.array([11.8,11.7,12.2,11.9,11.5,12.1,12.0,11.8,11.6,12.2,11.9,11.7,
                 12.0,11.8,11.6,11.7,11.9,11.5, 12.1,12.0])

population_mean = 12.0 #Hypothesized population mean

alpha = 0.05

t_statistic, p_value = stats.ttest_1samp(data,population_mean)

if p_value < alpha:
    print("Reject the null hypothesis")
else :
    print("Fail to reject the null hypothesis")
    
print(f"t-statistics: {t_statistic}")
print(f"p-value: {p_value}")

