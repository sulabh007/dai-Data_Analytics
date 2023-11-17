import numpy as np
import pandas as pd

s = pd.Series([4,56,67,6,33,34,23,43,4])

print(s) 

myindex=['USA','Canada','Mexico']

mydata = [1776,1876,1821]

#only index no label
myser = pd.Series(data=mydata)
print(myser)

#Now a label index
myser=pd.Series(data=mydata,index=myindex)
print(myser)

#create a series from a dictionary
ages = {'Sammy':5,'Frank':10,'Spike':7}
ser = pd.Series(ages)
print(ser)


#Use of named/labelled index
#Imaginary sales Data for 1st and 2nd Quarters for Global Company
q1 = {'Japan':80,'China':450,'India':200,'USA':250}
q2 = {'Japan':100,'China':500,'India':210,'USA':260}

#Convert into pandas series
sales_Q1 = pd.Series(q1)
sales_Q2 = pd.Series(q2)

print(sales_Q1)
print(sales_Q1['Japan'])
print(sales_Q1[0])






