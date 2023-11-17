import numpy as np
import matplotlib.pyplot as plt

rev_m = 170
rev_stdev = 20
iterations = 1000

#Create a normal distribution using these
revenue = np.random.normal(rev_m,rev_stdev, iterations)
print(revenue)

#Plot it 
plt.figure(figsize=(15,6))
plt.title('Revenue Simulation')
plt.plot(revenue)
plt.show()

#Now Cost of Goods Sold
#Generally it is about 60% of the revenue with 10% SD
#We already have 1000 revenue record, use them to randomly assign COGS is the above range
COGS = (revenue * np.random.normal(0.6,0.1))

plt.figure(figsize=(15, 6))
plt.title('Cost of Goods Sold Simulation')
plt.plot(COGS)
plt.show()

#Calculate gross profit
Gross_Profit = revenue - COGS
print(Gross_Profit)

plt.figure(figsize=(15, 6))
plt.title('Gross Simulation')
plt.plot(COGS)
plt.show()

#Create a stacked bar chart
numbers = list(range(1, 1001))

plt.figure(figsize=(10, 6))
plt.bar(numbers, revenue, label='Revenue', color='skyblue')
plt.bar(numbers, COGS, bottom=revenue, label='COGS',color='orange')
plt.bar(numbers, Gross_Profit, bottom=[r + c for r, c in zip(revenue, COGS)], 
        label="Gross Profit", color='lightgreen')

plt.xlabel("Number of times")
plt.ylabel('Amount ($)')
plt.title('Revenue, COGS, and Gross Profit using Monte Carlo')
plt.legend()

plt.show()
