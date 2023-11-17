import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

#Genrate a normal distibution with 10,000 data points, plot it, and show statistcis
np.random.seed(33)
norm_sample = np.random.randn(10000)
sns.histplot(x = norm_sample, kde = True)
plt.show()

print('mean = ',np.mean(norm_sample))
print('median = ',np.median(norm_sample))
print('std = ',np.std(norm_sample))

skewed_data_R = stats.skewnorm.rvs(10, size=10000)
sns.histplot(x = skewed_data_R, kde = True)
plt.show()

print('mean = ',np.mean(skewed_data_R))
print('median = ',np.median(skewed_data_R))


skewed_data_L = stats.skewnorm.rvs(-10, size=10000, loc =5)
sns.histplot(x = skewed_data_L, kde = True)
plt.show()

print('mean = ',np.mean(skewed_data_L))
print('median = ',np.median(skewed_data_L))

#Q-Q plots
stats.probplot(norm_sample, plot=plt);
plt.show()

stats.probplot(skewed_data_R, plot=plt);
plt.show()

stats.probplot(skewed_data_L, plot=plt);
plt.show()

#print the skewness of each dataset
print(stats.skew(norm_sample))
print(stats.skew(skewed_data_R))
print(stats.skew(skewed_data_L))

#perform a skewness test on each dataset
#return a numerical value representing the skewness of the dataset
print(stats.skewtest(norm_sample))
print(stats.skewtest(skewed_data_R))
print(stats.skewtest(skewed_data_L))

#Output: Statistic: The statistics value is the test statistic calcualted by the
# skewness test. It quantifies the degree of skewness in the dataset.
# If negative, it indicates that the dataset is left-skewed or negatively skewed.

#The p-value measures the evidence against a null hypothesis.
#A small p-value (typically less than 0.05) suggest that there is strong evidence to reject
#the null hypothesis, indicating that the data is significantly skewed.
#A larger p-value (greater than 0.05) suggests that there is not enough evidence to reject 
#the null hypothesis, indicating that the data may not be significantly skewed






















