import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Age' : [20, 30, 25, 35, 18, 28, 33]})

# p(A and B)
p_a_and_b = len(df[(df['Gender'] == 'Female') & (df['Age'] > 30)])/len(df)

#P(B)
p_b = len(df[df['Age'] > 30 ]) / len(df)

#P(A|B)
p_b_given_b = p_a_and_b / p_b

print(p_b_given_b)

#Group the DataFrame by gender
grouped_df = df.groupby('Gender')

#Count the number of people in each group who are over 30
over_30_count = grouped_df['Age'].apply(lambda x: (x>30).sum())

#Count the total number of pepole in each group
total_count = grouped_df['Age'].count()

#Calculate the conditionl probability for each group
conditionl_probabilitis = over_30_count / total_count

#Create a bar chart
plt.bar(conditionl_probabilitis.index, conditionl_probabilitis)

#Add lables and title
plt.xlabel('Gender')
plt.ylabel('Probability')
plt.title("Probablity of being over 30")

#Shoe the plot
plt.show()

#Exercise :Find P(A|B)

# P(B and A)
p_b_and_a = len(df[(df['Age'] > 30) & (df['Gender'] == 'Female')])/ len(df)

#P(A)
p_a = len(df[df['Gender'] == 'Female']) / len(df)

#P(A|B)
p_b_and_a = p_b_and_a / p_a

print(p_b_and_a)

#Group the DataFrame by gender
grouped_df = df.groupby('Gender')

#Count the number of people in each group who are over 30
over_30_count = grouped_df['Age'].apply(lambda x: (x>30).sum())

#Count the total number of pepole in each group
total_count = grouped_df['Age'].count()

#Calculate the conditionl probability for each group
conditionl_probabilitis = over_30_count / total_count

#Create a bar chart
plt.bar(conditionl_probabilitis.index, conditionl_probabilitis)

#Add lables and title
plt.xlabel('Gender')
plt.ylabel('Probability')
plt.title("Probablity of being over 30")

#Shoe the plot
plt.show()






















