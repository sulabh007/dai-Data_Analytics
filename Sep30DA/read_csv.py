import pandas as pd

titanic = pd.read_csv("titanic.csv")

print(titanic.info())

print(titanic.describe())

#Summary only for "Objects" columns, i.e. categorical columns
print(titanic.describe(include = ["O"]))

print(type(titanic))

print(len(titanic))

print(round(titanic,0))

print(min(titanic))

#The shape of  a DataFrame is a tuple of array dimmensions that tells the number of rows and columns a given
#df
print(titanic.shape)

#The size property returns the number of elements in the DataFrame.The number of elements is the number of 
#rows * the number of columns.
print(titanic.size)

#The row labels are called datafarame index
print(titanic.index)

#The column lables, called column names, are usually strings
print(titanic.columns)


#Selecting specific column
print(titanic['age'])

print(type(titanic['age']))

print(titanic[['age','gender']])

print(type(titanic[['age','gender']]))

#using the dot notaion
print(titanic.age)

print(titanic.embarked)

#A Series of True and False values.
print(titanic.gender == 'male')

#select only rows where the 'gender' is "male" and then print the 'fare' column for those rows
print(titanic[titanic.gender == 'male']["fare"])

#same as above
print(titanic.loc[titanic.gender == 'male','fare'])

#create a boolean mask
mask1 = titanic.gender == 'male'

#Create a new DataFrame 'titanic_male' by applying 'mask1' will contain only male passanger's data
titanic_male = titanic.loc[mask1]
print(titanic_male.head())

###############################################################################
print(1912 - titanic.age)
print(titanic.info)
titanic['YOB'] = 1912 - titanic.age
print(titanic.head())

print(titanic.sibsp + titanic.parch)

titanic["relatives"] = titanic.sibsp + titanic.parch
print(titanic.head())

titanic.drop(columns = ['sibsp', 'parch'], inplace=True)
print(titanic.head())

inflation_factor = 10
print(titanic.fare*10)

titanic.fare = titanic.fare*10
print(titanic.head())

cond1 = titanic.gender == "female"
cond2 = titanic.age < 14

print((cond1 | cond2).head())

print(titanic.loc[cond1 | cond2])

print(titanic.loc[cond1 & cond2])

wom_or_chi = titanic.loc[cond1 | cond2, ["survived", "pclass" , "gender",'age']]

print(wom_or_chi.head())
print(wom_or_chi.info())
print(wom_or_chi.describe())

wom_or_chi = titanic.loc[cond1 & cond2, ["survived", "pclass" , "gender",'age']]

print(wom_or_chi.head())
print(wom_or_chi.info())
print(wom_or_chi.describe())












