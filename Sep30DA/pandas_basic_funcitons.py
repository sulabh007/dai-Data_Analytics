import pandas as pd
df= pd.read_csv("Dummy_Sales_Data_v1.csv")

#Getting dataset overview
print(df) #prints the entire DataFrame, which will display all the rows and columns  of the loaded CSV data.
print(df.head())#prints the first 5 rows (by default) of the DataFrame 
print(df.tail())#prints the last 5 rows (by default) of the DataFrame 
print(df.sample())#prints a random row from the DataFrame
print(df.info())#prints a concise summery of the DataFrame's information It includes details such as the
#number of non-null entries in each column, data types,and memory usage.
print(df.describe())#prints basic statistics for the DataFrame 

#Force to display everything
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
print(df)

#Reset
pd.reset_option("display.max_rows")
pd.reset_option("display.max_columns")

#Selecting a subset
print(df.query("Quantity  > 95"))

#Get the value at the intersection of the 100th row and the 'Sales_Manager' column
print(df.loc[100,'Sales_Manager'])

#Return a subset of the original DataFrame df containing row 100 and 200 and columns 6 and 3 .We will get a
#DataFrame that includes data from these specific rows and columns based on their integer position.
print(df.iloc[[100,200],[6,3]])

#loc - select by labels
#iloc - select by positions

#Deeper analysis
print(df["Sales_Manager"].unique()) #Values
print(df["Sales_Manager"].nunique()) #Count
print(df.nunique())     #For all columns
print(df.isnull())      #True/False for each column

#Create a DF where product cataegory is missing
df2 = df[df["Product_Category"].isnull()]
print(df2)

#Fill nulls with something
df2.fillna("MissingInfo")

#inplace = True : The inplace parameter, when set to True,indicates that the operation should be performed
#on the DataFrame in place, and it will modify the original df2 DataFrame. If it's set ot 
#Fasle(or not provided), the operaton will return a new DataFrame with the missing values filled,
#and the original df2 will remain unchanged.
df2.fillna("MissingInfo",inplace=True)
print(df2.sample())

#Reset display options
pd.reset_option("all")

#Sorting
df_sorted = df.sort_values(by=['Quantity'], ascending=True)
print(df_sorted.head())

#How many times s column appeared - Similar to COUNT() function in SQL
print(df.value_counts("Sales_Mangaer"))

#get n max/min etc
print(df.nlargest(10,"Delivery_Time(Days)"))
print(df.nsmallest(7, "Shipping_Cost(USD)"))

#Dataset  Modifications
#copy as subset
#Uses the .iloc indexer to select a subset of rows and all colums. Specifiacally, it selects rows from
#index 0(inclusive) to 10 (exclusive), which means it selects the first 10 rows. The colon : is used to 
#select all columns.
df1= df.iloc[0:10,  :]#This is deep copy, meaning df is unchaged, and whatefer changes you make to any of 
#these DataFrame will not be reflected in the other
print(df1)

#Rename columns
df1.rename(columns = {'Shipping_Cost(USD)':"Shipping_Cost",'Delivery_Time(Days)':'DeliveryTime_in_Days'},
           inplace=True)
print(df1)

#attempts to filter rows in the DataFrame df1 where the "Status" column in equal to "Not Shipped." However,
#it does not actually apply the fileter but instead returns a DataFrame of the same shape as df1 with Nan
#values where the condition is not met.
condition = df1["Status"] == "Not Shipped"

#df1.where(condition): This line uses the where method to apply the conditon to df1 .However,it returns
#a DataFrame of the shape as df1 with NaN  values in the rows where the condition is False. Essentially,
#it keeps all rows but replaces the rows that don't meet the condition with NaN values.
print(df1.where(condition)) 

#Drop rows/columns, axis = 0:rows, 1:columns
df.drop(0,axis=0) #This drops the first row (index 0)

df1.drop("OrderCode", axis=1) #Remove OrderCode column
#to remove it forever,you need to make inplace=True in df.drop()
df1.drop("OrderCode",axis=1,inplace=True)

#Change index
df.set_index("Sales_Mangager",inplace=True)
print(df.head)























































