import numpy as np

#Part 1
def roll_dice():
    #Simulation of rolling a dice twice, minimum number we get is 1, max is 6
    #Add the results of the two simlations, so possible value will be:
    #(1, 1) or (1, 2)... (6,6)...Sum will be between 2 and 12
    #Run multiple times to verify
    return np.sum(np.random.randint(1, 7, 2))

print(roll_dice())

#Part 2
#Someone spproches us saying I will give you 5 dollars if you get 
#   and take 1 dollor if you get a number other than 
#How do you we know what will happen?
#Our own "Monte Carlo Simulation" like function
def monte_carlo_simulation(runs=1000):
    results = np.zeros(2) #An array, results[0] and result [1] initialized to two zeroes
    for _ in range(runs): #Run 100 times
        if roll_dice() == 7:
            results[0] += 1
        else: 
            results[1] += 1
    return results

#Test 2-3 times and calculate how much you will win verses lose
print(monte_carlo_simulation())
print(monte_carlo_simulation())
print(monte_carlo_simulation())

#Part 3
#Now do this 1000 times
#Takes some time

results = np.zeros(1000)

for i in range(1000):
    results[i] = monte_carlo_simulation()[0]
    
print(results)

#Let us plot it
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(results, bins=15)

plt.show()

#Our win/loss
print(results.mean())               #Genreal mean
print(results.mean()*5)             #What will get as win on an average
print(1000 - results.mean())        #What we will pay on an average
print(results.mean()/1000)          #Probability of the 'we will pay' result
#The last probability should be close to the therotical probability of getting
#   a 7 when we throw two dice




























