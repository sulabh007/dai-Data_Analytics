import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


housing = pd.read_csv('housing.csv')
print(housing.head)

#kde will join the histogram bins
sns.histplot(data= housing, x= 'SalePrice', kde=True)
plt.show()

insurance = pd.read_csv('insurance.csv')
print(insurance.head)

sns.histplot(data= insurance, x= 'bmi', kde=True)
plt.show()

stocks = pd.read_csv('stocks.csv')
print(stocks.head)

sns.histplot(data= stocks, x= 'apple', kde=True, bins = 30)
plt.show()
