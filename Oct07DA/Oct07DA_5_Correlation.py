from sklearn.datasets import fetch_california_housing

housing, target = fetch_california_housing(as_frame=True, return_X_y=True)
print(housing.head())
print(target.head())

#correlation of all the columns with each other
print(housing.corr())

#Correaltion of two specific columns
corr = housing.corr()
print(corr["MedInc"]["AveRooms"])

#Print the correlation matrix
print(corr)

#Visual view
import seaborn as sns
import matplotlib.pyplot as plt

cmap = sns.diverging_palette(10, 220, as_cmap=True)

sns.heatmap(corr, vmin=-1.0, vmax=1.0, square=True, cmap=cmap)
plt.show()