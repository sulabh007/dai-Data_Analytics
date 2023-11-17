import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import yfinance as yf

#Initialising the tickers, if not ok: get the right one from yahoo finance
tickers =["TCS.NS",'ICICIBANK.NS','RELIANCE.NS','BHARTIARTL.NS','ITC.NS','MARUTI.NS','BAJFINANCE.NS']

df=yf.download(tickers,period='3y')

close=df.Close

norm=close.div(close.iloc[0].mul(100))

ret=close.pct_change().dropna()

print(ret)
print(ret.cov())
print(ret.corr())

#First correlation
plt.figure(figsize=(15,7))
sns.heatmap(ret.corr(),cmap="Blues")
plt.show()

#First correlation with annotations
plt.figure(figsize=(15,7))
sns.heatmap(ret.corr(),cmap="Blues",annot=True)
plt.plot()
plt.show()

#Add covaraince
plt.figure(figsize=(15,7))
sns.heatmap(ret.cov(),cmap="Blues",annot=True)
plt.show()