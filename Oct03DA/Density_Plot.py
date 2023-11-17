import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


marketing = pd.read_csv('marketing.csv')
marketing.head()

marketing['Income'].plot.density()
plt.show()

insurance = pd.read_csv("insurance.csv")
insurance.head()

plt.hist(insurance['age'], edgecolor = 'black')
plt.show()

insurance['age'].plot.density()
plt.show()



