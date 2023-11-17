import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weight-height.csv")

#Basic information
print(df.Weight)

#Plot weights
plt.hist(df.Weight, bins=20, width=0.8)
plt.xlabel("Weight")
plt.ylabel("Count")
plt.show()

#See summery statistics
df.Weight.describe()

#Visualize outliers
import seaborn as sns
sns.boxplot(df['Weight'])
plt.show()

#Since we are on outlier topic, also draw it ofr height
sns.boxplot(df['Height'])
plt.show

#Back to weight
#Get outlier values
upper= df.Weight.mean() + 3 * df.Weight.std()
lower= df.Weight.mean() - 3 * df.Weight.std()

print(upper)
print(lower)

#Remove outlier values and store the rest in a new dataframe
new_df = df[(df.Weight<upper) & (df.Weight>lower)]

print(new_df.head())
print(new_df.shape) #Earlier, wer had 10,000 rows, now 2 outliers got removed

#Same thing, but now by calculating the Z-score
df['zscore'] = (df.Weight - df.Weight.mean()) / df.Weight.std()

print(df.head(5))

print(df[df['zscore'] > 3])
print(df[df['zscore'] < -3])



















































