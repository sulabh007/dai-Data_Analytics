import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Create list to store samlple means
means = []

#repeat experiment 100 times
for i in range(100):
    #generate a random array of 5 values, with value betweeen 0 and 1
    arr = np.random.rand(5)
    #Calculate mean of random sample
    s_mean = np.mean(arr)
    #add s_mean to list
    means.append(s_mean)
    
#Plot it along with the mean of the distribution
sns.histplot(means, kde=True, #Kernal density estimate smootehnns the plot
             bins = 100, color= 'darkblue')

#plt.show()

#Calculate the mean
mean = sum(means)/len(means)

#Plot the mean over the distribution to get a sense of the central tendency 
plt.axvline(mean, color='k',linestyle='dashed', linewidth=1)

min_ylim , max_ylim = plt.ylim()
plt.text(mean*1.1, max_ylim*0.9, 'Mean :{:.2f}'.format(mean))
plt.title("Sampling distribution of the sample means of randomly generated samples (no of samples = 100)")
plt.xlabel('Sample mean')
plt.ylabel('Frequfency')
plt.show()

#for 1000 times
means = []
for i in range(1000):
    arr = np.random.rand(5)
    s_mean = np.mean(arr)
    means.append(s_mean)

sns.histplot(means, kde=True, #Kernal density estimate smootehnns the plot
             bins = 100, color= 'yellow')

mean = sum(means)/len(means)

#Plot the mean over the distribution to get a sense of the central tendency 
plt.axvline(mean, color='k',linestyle='dashed', linewidth=1)

min_ylim , max_ylim = plt.ylim()
plt.text(mean*1.1, max_ylim*0.9, 'Mean :{:.2f}'.format(mean))
plt.title("Sampling distribution of the sample means of randomly generated samples (no of samples = 1000)")
plt.xlabel('Sample mean')
plt.ylabel('Frequfency')
plt.show()
























































