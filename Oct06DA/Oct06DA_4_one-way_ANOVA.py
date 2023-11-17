import numpy as np
import pandas as pd
from scipy.stats import f_oneway

#Example data for threee groups (teaching mehtods A, B, and C)
method_A = [85,88,91,78,82]
method_B = [75,79,80,82,78]
method_C = [90,85,88,92,87]

#Perform one-way ANOVA
f_statistic, p_value = f_oneway(method_A, method_B,method_C)

#Print the results
print('F-Statistic:', f_statistic)
print("P-Value:", p_value)

#Interept teh results
alpha = 0.05 #Significance level
if p_value < alpha:
    print("Reject the null hypothesis: There are siginificant differnences in the means.")
else:
    print("Fail to Reject the null hypothesis: No siginificant differnences in the means.")