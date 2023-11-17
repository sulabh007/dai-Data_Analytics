import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

advert = pd.read_csv('Advertising.csv')
advert.head()

#Covariance coefficient
print(advert['TV'].cov(advert['Newspaper']))
#Or
print(advert.TV.cov(advert.Newspaper))

#Covarinace matrix
print(advert.cov())

#fmt ='g' means use general format for numbers, not scientific notation

dataplot = sns.heatmap(advert.cov(),annot=True, fmt='g')
plt.show()