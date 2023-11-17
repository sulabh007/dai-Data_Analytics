import numpy as np
import pandas as pd
from scipy.stats import ttest_ind #just the t-test from scipy.stats
from scipy.stats import probplot
import matplotlib.pyplot as plt
import pylab
import seaborn as sns

shoes = pd.read_csv("women_shoe_prices.csv")

print(shoes.shape)
print(shoes.sample(5))

shoes['midprices'] = (shoes["prices.amountMax"]+shoes['prices.amountMin'])/2

probplot(shoes['midprices'],dist='norm',plot=pylab)

pink = shoes[shoes.colors=='Pink']
notpink = shoes[shoes.colors!='Pink']

print(ttest_ind(pink.midprices,notpink.midprices,equal_var=False))

plt.hist(shoes['midprices'])
plt.show()

shoesreduced = shoes[shoes.midprices < 300]

plt.hist(shoes['midprices'])
plt.show()

probplot(shoes['midprices'],dist='norm',plot= pylab)
plt.show()

pink = shoes[shoes.colors=='Pink']
notpink = shoes[shoes.colors!='Pink']
print(ttest_ind(pink.midprices,notpink.midprices,equal_var=False))

#the p-value is still under 0.01 which shows there is significant that pink shoes
#are different price to other shoes






















