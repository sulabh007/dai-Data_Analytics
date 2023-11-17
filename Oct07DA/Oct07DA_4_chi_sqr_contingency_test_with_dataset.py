import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as ws

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
print(df.head())

print("Against Age")
print(chi2_contingency(pd.crosstab(index=df['age'], columns=df["DEATH_EVENT"])))


print("Against Anemia")
print(chi2_contingency(pd.crosstab(index=df['anaemia'], columns=df["DEATH_EVENT"])))

print("Against Diabetes")
print(chi2_contingency(pd.crosstab(index=df['diabetes'], columns=df["DEATH_EVENT"])))

print("Against High Blood Pressure")
print(chi2_contingency(pd.crosstab(index=df['high_blood_pressure'], columns=df["DEATH_EVENT"])))

print("Against Sex")
print(chi2_contingency(pd.crosstab(index=df['sex'], columns=df["DEATH_EVENT"])))

#The only column categorical that has reationchip with Death Event is age,that we can also 
#see in graph below

plt.figure(figsize=(20,6))
title = plt.title('Survival and Deaths by Age', fontsize=20)
title.set_position([0.5,1.15])
ax = sns.countplot(x='age', hue="DEATH_EVENT",data=df)
ax.set_xlabel('Age')
ax.set_ylabel("Count")
a = ax.set_xticklabels(ax.get_xticklabels(),rotation=0,horizontalalignment='center')
plt.show()

#Exercise: Improve this graph

#Exercise: Try it for other variables


print("Against Smoking")
print(chi2_contingency(pd.crosstab(index=df['smoking'], columns=df["DEATH_EVENT"])))