from numpy import random


random.seed(0)

totals = {20:0,30:0,40:0,50:0, 60:0, 70:0}


purchases = {20:0,30:0,40:0,50:0, 60:0, 70:0}
totalPurchase = 0

for i in range(100000):
    ageDecade = random.choice([20, 30, 40, 50,60,70])
    purchasesProbability = float(ageDecade) / 100.0
    totals[ageDecade] += 1
    
    if (random.random() < purchasesProbability):
        totalPurchase += 1
        purchases[ageDecade] += 1
    
print(totals)
print(purchases)
print(totalPurchase)

#Coditional Probability

PEF = float(purchases[30]) / float(totals[30])
print('P(purchase | 30s): '+ str(PEF))

#P(F) is just probability of being 30 in this data set:
PF = float(totals[30]) / 100000.0
print('P(30s): '+ str(PF))

PEF = float(purchases[70]) / float(totals[70])
print('P(purchase | 70s): '+ str(PEF))

#P(F) is just probability of being 70 in this data set:
PF = float(totals[70]) / 100000.0
print('P(70s): '+ str(PF))

#And P(E) is overall probability fo buying something, regardless of your age:
PE = float(totalPurchase) / 100000.0
print('P(purchase): '+ str(PE))

print('P(purchase): '+ str(PE) + str(float(purchases[30] / 100000.0)))

#Let's also compute the product of P(E) and P(F), P(E)P(F):
print("P(30's)P(Purcase)" + str(PE *PF))

"""
Exercise: Modify the code above such that the purchase probabiliy does NOT vary with age,
making E and F actually independent.
Then, confirm that P(E|F) is about the same as P(E), showing that the conditional probability
of purchase for a given age is not any different than the probabiliy of purchase regardless
 of age."""

totals = {20:0,30:0,40:0,50:0, 60:0, 70:0}


purchases = {20:0,30:0,40:0,50:0, 60:0, 70:0}
totalPurchase = 0

for i in range(100000):
    ageDecade = random.choice([20, 30, 40, 50,60,70])
    purchasesProbability = float(ageDecade) / 100.0
    totals[ageDecade] += 1
    
    if (random.random() < 0.6):
        totalPurchase += 1
        purchases[ageDecade] += 1
    
print(totals)
print(purchases)
print(totalPurchase)

#Coditional Probability

PEF = float(purchases[30]) / float(totals[30])
print('P(purchase | 30s): '+ str(PEF))

#P(F) is just probability of being 30 in this data set:
PF = float(totals[30]) / 100000.0
print('P(30s): '+ str(PF))

PEF = float(purchases[70]) / float(totals[70])
print('P(purchase | 70s): '+ str(PEF))

#P(F) is just probability of being 70 in this data set:
PF = float(totals[70]) / 100000.0
print('P(70s): '+ str(PF))

#And P(E) is overall probability fo buying something, regardless of your age:
PE = float(totalPurchase) / 100000.0
print('P(purchase): '+ str(PE))

print('P(purchase): '+ str(PE) + str(float(purchases[30] / 100000.0)))

#Let's also compute the product of P(E) and P(F), P(E)P(F):
print("P(30's)P(Purcase)" + str(PE *PF))
























