import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv('StudentsPerformance.csv')

print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum)
print(df.describe())

"""
From our data summery, we can see that there are no null value indicating we are
working with a clean dataset. Addetionallym, teh socres is math, reading and writing contain
very similar averages.
"""
#Create fuction to display distribution pariplot
def distribution(dataset, variable):
    """
    Args:
        dataset: Include the DataFrame here
        variable: Include the column from dataframe used for color encoding
    Returns:
        sns pariplot with color encoding
    """
    g = sns.pairplot(data= dataset, hue=variable)
    g.fig.suptitle('Graph showing distribution between scores and {}'.format(variable), fontsize=20)
    g.fig.subplots_adjust(top=0.9)
    return g

print(df.columns)
distribution(df, 'gender')
plt.show()
#Female perform higer in reading and writing while males perform higer on math.

#Score and race
distribution(df, 'race/ethnicity')
plt.show()

#Score and parental education level
distribution(df, 'parental level of education')
plt.show()
#There appears to be trend in parental education level and student's score. The
#variance between the different categorical data indicates this is not an major 
#factor

#Score and lunch
distribution(df, 'lunch')
plt.show()
#Students who ate the standard lunch on average tested higer in all three subjects.

#Score and test preparation score
distribution(df, 'test preparation course')
plt.show()

#Students who completed  a test preparation cource on average tested higher in
#all three subjects.

"""
Finding correlation between categorical variables and test scores using 1-way ANOVA
1-Way ANOVA hypothesis:

Null hypothesis (H0): There is no differnece between groups and equlity between
means
Alternative hypothesis (H1): There is a differnece between the means and groups
"""

#Clean up column names of StatsModels
df.columns = ['gender', 'race', 'parental_edu', 'lunch', 'test_prep_course', 'math_score', 'reading_score'
              , 'writing_score']


#Create anova test fuction
def anova_test(data, variable):
    """
    Args:
        data = (DataFrame)
        variable = Categorical column used for 1-way ANOVA test
    Returns: Nothing
    """
    x = ['math_score', 'reading_score', 'writing_score']
    for i,k in enumerate(x):
        lm = ols('{} ~ {}'.format(x[i], variable), data= data).fit()
        table = sm.stats.anova_lm(lm)
        print("P-value for 1-way ANOVA test between {} amd {} is".format(x[i], variable),
              table.loc[variable,'PR(>F)'])
        
#Gender ANOVA
anova_test(df, 'gender')#below 0.05, score is releated to gender

#The p-values are below 0.05 indicating we can reject the null hypothesis. This 
#confirmation shows us there is statistical correlation between test scores and gender.

#Parental education ANOVA
#The p-values are below 0,05 indicating we can reject the null hypothesis
anova_test(df, 'parental_edu') #below 0.05, score is releated to PE


#Lunch ANOVA
anova_test(df,'lunch')#below 0.05, score is releated to lunch

#Test Prep ANOVA
anova_test(df, 'test_prep_course')#below 0.05, score is releated to prep


#Although we saw statsitical significance on parent level of education and student's
#scores, our pairplot showed us this differnece was almost negligible. we will use a 
#countplot below to take a further look at this data

#Create countplot for parental education and student socres
plt.figure(figsize=(12,5))
sns.countplot(data=df, x = 'parental_edu', hue='gender')
plt.show()

#Our dataset included a very low number of parints with a master's degree
#or bachlor's degree. Due to the low sample size we can not confidently say
#that students with highely educated parents will score better.


"""
Conclusion:
Females perform higer in reading and writing and subjects.
Male perorm higher in math
Parental education level has a negligible diffenence in student's test perfomance.
Students who ate the standard lunch tested higer than thoes who ate a free/reduced meal.
Students who completed a test preparation cource scored higher than thoes who did not.
All categorical data was statistically tested against the exam scores useing a 1-way ANOVA test.
This test allows us to accurately confirm whether a category of data is correlated to the 
numerical outocme. Using a 95% confidence internal we achieved p-values < 0.05 for each category of
data. This allows us to reject our null hypothesis and summize that the catergorical data in this 
dataset is correlated to the reading, writing, and math socres.
"""
















































