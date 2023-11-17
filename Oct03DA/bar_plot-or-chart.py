import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('ex5.csv')
print(df1)

df1.plot.bar(x = 'branch number')
plt.show()

#Show sub plots
df1.plot.bar(x = 'branch number', subplots = True)
plt.show()

#Single column
df1.plot.bar(x = 'branch number', y = 'sale1')
plt.show()