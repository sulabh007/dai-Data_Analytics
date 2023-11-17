import pandas as pd

summer = pd.read_csv("summer.csv",index_col="Athlete")
print(summer)

print(summer.iloc[0])
print(type(summer.iloc[0]))

#Second index value's (first athlete's) record
print(summer.iloc[1])
#Last index value's (last athlete's) record
print(summer.iloc[-1])

#Select the second, third, and fourth (first athelet's) rows
print(summer.iloc[[1,2,3]])

#Select the second to fourth athelete's rows
print(summer.iloc[1:4])

#Select the first five athelet's rows
print(summer.iloc[:5])

#Select the lat five athelet's rows
print(summer.iloc[-5:])

#select all rows
print(summer.iloc[:])

#First row and the first three columns
print(summer.iloc[0,:3])

#First row and selected columns
print(summer.iloc[0,[0,2,5,7]])

#Selected rows and columns
print(summer.iloc[34:39,[0,2,5,7]])

#Is the fourth column country? True/False
print(summer.iloc[:, 4].equals(summer.Country))

#Print athelete name and country
print(summer["Country"])

##############################################################################
group1 = summer.groupby('Country')

l = list(group1)
print(l)
print(group1.head())
print(l)

group2 = summer.groupby(by = ['Country', 'Gender'])
print(group1.head())
l = list(group2)
print(l)











































