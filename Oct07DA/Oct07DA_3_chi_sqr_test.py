#Here we use stats.chisquare
# Primarily used of conducting a chi-square goodness-of-fit test, which compares
# observed f



import pandas as pd
import numpy as np
from scipy import stats

national = pd.DataFrame(['white']*100000 + ['hispanic']*60000 +['black']*50000
                        + ['asian']*15000 + ['other']*35000)

minnesota = pd.DataFrame(['white']*600 + ['hispanic']*300 +['black']*250
                        + ['asian']*75 + ['other']*150)


print(national)
print(minnesota)
print(national.sample(5))
print(minnesota.sample(5))

#Create frequency tables (crosstabs) for both dataset using pd.crosstab.
#national_table and minnesota_table store the counts of each demographic category.

national_table = pd.crosstab(index=national[0], columns='count')
minnesota_table = pd.crosstab(index=minnesota[0], columns='count')

print('National')
print(national_table)
print(" ")
print("Minnesota")
print(minnesota_table)

observed = minnesota_table

national_ratios = national_table/len(national) #Get population ration

expected = national_ratios * len(minnesota) #Get expected couts

chi_squared_stat = (((observed-expected)**2)/expected).sum()

print("Calculated observed  value")
print(chi_squared_stat)


#Find the critical value for a 95% confidence level with 4 degrees of freedom.

crit = stats.chi2.ppf(q = 0.95,# Find the critical value for 95% confidence*
                      df= 4) #DF = number of variable categories - 1, degree of freedom

print("Critical value")
print(crit)


p_value = 1- stats.chi2.cdf(x=chi_squared_stat, #find the p-value
                           df=4)

print("P value")
print(p_value)


#################
print("Observed value throgh stats library")
print(stats.chisquare(f_obs=observed,#Array of observed counts
                      f_exp=expected))

#The test results agree with the values we calculated above.
























