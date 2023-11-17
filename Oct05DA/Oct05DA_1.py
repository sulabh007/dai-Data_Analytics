import empiricaldist
from statadict import parse_stata_dict

dict_file = 'GSS.dct'
data_file = 'GSS.dat.gz'

from statadict import parse_stata_dict
stata_dict = parse_stata_dict(dict_file)

import gzip
fp = gzip.open(data_file)

#Covnvert the file into a Pandas DataFrame

import pandas as pd
gss = pd.read_fwf(fp, names = stata_dict.names, colspecs=stata_dict.colspecs)

print(gss.shape)
print(gss.head())

#Distribution of education
print(gss['EDUC'].value_counts().sort_index())

#The values 98 and 99 are special codes for "Don't know" and "NO answer". 
#We'll use replace these codes with NaN.

import numpy as np
educ = gss['EDUC'].replace([98,99],np.nan)

#Visualize it
import matplotlib.pyplot as plt

educ.hist(grid=False)
plt.xlabel('Years of education')
plt.ylabel('Number of respondents')
plt.title('Histogram of education level')
plt.show()

#Looks like the peak is near 12 years of education. But a histogram is not the 
#best way to visulize this

from empiricaldist import Pmf

pmf_educ = Pmf.from_seq(educ, normalize=False)
print(type(pmf_educ))
print(pmf_educ.head())
print(pmf_educ.tail())
print(pmf_educ[20])

#Usually when we make a PMF, we want to know the fraction of 


pmf_educ_norm = Pmf.from_seq(educ, normalize=True)
print(pmf_educ_norm.head())
print(pmf_educ_norm[12]) #Sample for 12 years of experience

#Pmf provides a bar method that plots the values and their probablities as a bar chart
pmf_educ_norm.bar(label="Educ")

plt.xlabel('Years of education')
plt.xticks(range(0,21,4))
plt.ylabel("PMF")
plt.title("Distribution of years of educaton")
plt.legend()
plt.show()

#Exercise: Let's look at the YEAR column in the DataFrame, which represent the 
#year each respondent was interviewed
#Make an unnormalized Pmf for YEAR and display the result.How many reaspondent 
#were intterviewed in 2018?

YEAR = gss['YEAR']

pmf_YEAR = Pmf.from_seq(YEAR, normalize=False)

print(pmf_YEAR)
pmf_YEAR.bar(label="YEARS")

plt.xlabel('Years')
plt.xticks(range(1972,2018,4))
plt.ylabel("PMF")
plt.title("Distribution of years")
plt.legend()
plt.show()


#NOw CDF
from empiricaldist import Cdf

#The values 98 and 99 are special codes for "Don't know" and "NO answer". 
#We'll use replace these codes with NaN.

age = gss['AGE'].replace([98,99],np.nan)

cdf_age = Cdf.from_seq(age)
cdf_age.plot()
plt.xlabel('Age (Years)')
plt.ylabel("CDF")
plt.title("Distribution of age")
plt.show()

q=51
p = cdf_age(q)
print(p)
#about 63% of the respodents are 51 years old or younger

#Inversely, find the age at a certain value of cumulative probabiliy:
p1 = 0.25
q1 = cdf_age.inverse(p1)
print(q1)
#25% pf the respondents are age 31 or less. Another way to say the same thing is
#"age 31 is the 25th percentile of this distribution".


#we can now use 75th percentile to find IQR
#it measures the spread of the ditribution, so it is similar to standard 
#deviation or variance.

p3 = 0.75
q3 = cdf_age.inverse(p3)
print(q3)
print(q3-q1)

#Lab exercise: Using cdf_age, coumpute the fraction of the respondets
#in the GSS dataset that are older than 65.

age = gss['AGE'].replace([98,99],np.nan)

cdf_age = Cdf.from_seq(age)
cdf_age.plot()
plt.xlabel('Age (Years)')
plt.ylabel("CDF")
plt.title("Distribution of age")
plt.show()

q=65
p = cdf_age(q)
print((1-p)*100)
#about 16% of the respodents are older than 65 years


#Exercise:THe distribution of income in almost every country is long-tailed, which 
#means there are a small number of people with very high incomes, converted to 1986 dollars.
# We can get a sense of the shape of this distribution by plotting the CDF.
realinc = gss['REALINC']
cdf_realinc = Cdf.from_seq(realinc)
cdf_realinc.plot()
plt.xlabel('Real Income (USD)')
plt.ylabel("CDF")
plt.title("Distribution of Real Income")
plt.show()


#Now let us compare PMF and CMF

#Create series fro male and female respondents
male = (gss['SEX'] == 1)
female = (gss['SEX'] == 2)

#Select ages
male_age = age[male]
female_age = age[female]

#Plot PMF for each
pmf_male_age = Pmf.from_seq(male_age)
pmf_male_age.plot(label = "Male")

pmf_female_age = Pmf.from_seq(female_age)
pmf_female_age.plot(label = "Female")

plt.xlabel('Age (years)')
plt.ylabel('PMF')
plt.title("Distribution of age by sex")
plt.legend();
plt.show()

#Now CDF for same data file
cdf_male_age = Cdf.from_seq(male_age)
cdf_male_age.plot(label='Male')

cdf_female_age = Cdf.from_seq(female_age)
cdf_female_age.plot(label='Female')

plt.xlabel("Age (Years)")
plt.ylabel("CDF")
plt.title("Distribution of age by sex")
plt.legend();
plt.show()

#Observations:
    


print(cdf_male_age[60],cdf_female_age[60])

#comparing a male and female at the 50th percentile
print(cdf_male_age.inverse(0.5),cdf_female_age.inverse(0.5))

#Lab Exercise: What fraction of men are over 80? what fraction of woman?
print(cdf_male_age[80],cdf_female_age[80])

print(1-cdf_male_age[80])
print(1-cdf_female_age[80])

#Now income analysis
#The varailble REALINC represents household income in 1986 dollers.
pre95 = (gss['YEAR'] < 1995)
post95 = (gss['YEAR'] >= 1995)

income = gss['REALINC'].replace(0, np.nan)

Pmf.from_seq(income[pre95]).plot(label = "Before 1995")
Pmf.from_seq(income[post95]).plot(label = "After 1995")

#Plot PMFs
plt.xlabel("Income (19986 USD)")
plt.ylabel('PMF')
plt.title('Distribution of income')
plt.legend()
plt.show()

#Again the graph is very noisy: exhibits a significant amount of random or usnstructured
#variability or fluctuation

#And now CDF

Cdf.from_seq(income[pre95]).plot(label = "Before 1995")
Cdf.from_seq(income[post95]).plot(label = "After 1995")

plt.xlabel("Income (19986 USD)")
plt.ylabel('CDF')
plt.title('Distribution of income')
plt.legend()
plt.show()

#Below $30000 the CDFs are alomost identical; above that , we can see that the post-1995
#ditribution is shifted to the right. In other words, the fraction of people with high income
#is about the same, but the income of high earners has increased.


#Lab Exercise: In the previous figurek the doller amounts are big enough that the labels
#on the x axis are crowded. Improve the figure by 

#Kernal Density Estimation or Probability Density Function (PDF)
age_data = gss['AGE']

#Create a  histogram to visualize the PDF
plt.hist(age_data, bins = 20, density=True, alpha= 0.6, color='b', label='PDF')
plt.xlabel('Age')
plt.ylabel('Probability Density')
plt.title('PDF of Age in GSS Dataset')
plt.legend()
plt.show()
         
#Corresponding PMF
pmf = age_data.value_counts(normalize=True).sort_index()

#Create a bar plot of the PMF
plt.figure(figsize=(10,6))
plt.bar(pmf.index,pmf.values)
plt.xlabel('Age')
plt.ylabel('Probability')
plt.title('PMF of Age in GSS Dataset')
plt.xticks(rotation=90)
plt.show











































