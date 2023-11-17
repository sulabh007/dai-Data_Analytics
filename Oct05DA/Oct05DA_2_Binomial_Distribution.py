from scipy.stats import binom

#Hospital records show that of patients suffering from a specific disease, '75%' die of it. What is the
#probability that of six randomly selected Patients, four will recover?
#Here
n=6
k=4
p = 0.25
probab = binom.pmf(k=4,n=6,p=0.25)
print("Probability that of six randomly selected Patients, four will recover :",probab)


###################################### Q2 #####################################
"""A (blindfolded) marksman finds that on the average, he hits the target '4' times out of'5'. 
If he fires '4' shots, what is a probability of (a) more than '2' hits and (b) at least '3' misses"""

#For more than 2 hits, k can be either 3 or 4
#Probability of more than 2 hits i.e. k=3 or 4
print("Probability of more than 2 hits :",binom.pmf(k=3,n=n,p=p)+binom.pmf(k=4,n=n, p=p))
#n 0 or 1 hits i.e. k can be either 0 or 1.
#Probability of at least 3 misses i.e. either 1 hit or 0 hits, so k=0 or 1
print("Probability of more than 3 misses :",binom.pmf(k=0,n=n,p=p)+binom.pmf(k=1,n=n, p=p))
#Same thing, but using CDF instead of PDF
print("Probability of more than 3 misses :",binom.cdf(k=1,n=n,p=p))

###############################################################################
from scipy.special import comb
import seaborn as sns
import matplotlib.pyplot as plt

n= 4 #The number of trials
k= 1 #The number of success
p= 0.33 #Success rate

p_binomial = comb(n,k)*p**k*(1-p)**(n-k)
result = p_binomial * 100

print(p_binomial)
print(result)








