import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


marketing = pd.read_csv('marketing.csv')
marketing.head()

plt.hist(marketing['Income'])
plt.show()
plt.hist(marketing['Income'], edgecolor = 'black')
plt.show()
plt.hist(marketing['Income'], bins = 15, edgecolor = 'black')
plt.show()

#Using sns

sns.histplot( x = "Income", data = marketing,bins= 15, color = "green")
plt.show()
