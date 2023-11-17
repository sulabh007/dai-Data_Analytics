import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #Useful for statistical visualizations, extends matplotlib features

marketing = pd.read_csv('marketing.csv')

print(marketing.head())

#Understand customer income distribution
plt.boxplot(marketing['Income'])
plt.show()
#Income above 1,20,000 are outliers

























