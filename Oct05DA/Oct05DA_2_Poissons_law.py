"""
A life insurance salesman sells on the average 3 life insurance policies per week.
use Possin's law to calculate the probability
a. In a given week he will sell some policies
b. In a given week, he will sell between 2 and 5 policies
c. Assuming that per week, there are 5 working days, what is th probability that 
on a given day, he will sell one policy?
"""
from scipy.stats import poisson

mu = 3 #Lambda

#Probability of selling some policies in a week
print("The probabiliy of selling some policies in a week: ",1-poisson.pmf(k=0,mu=mu))

#The probability of selling 2 or more policies but less than 5 polices in a week
print("The probability of selling 2 or more polices but less than 5 polices in a week:",
      sum(poisson.pmf(k=[2,3,4],mu=mu)))

#Assuming that per week, there are '5' working days, what is the probability that on a given day, 
#he will sell one policy?
print("The probability that on a given day, he will sale one policy:", poisson.pmf(k=1,mu=3/5))

#Interesting! It will NOT be 100%
print("The probability of selling three polices in a week:", poisson.pmf(k=3,mu=mu))


