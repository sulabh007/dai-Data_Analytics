import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('MS_Dhoni_ODI_record.csv')

#Basic cheks
print(df.head())
print(df.tail())

#Data cleaning - Opposition name says 'v Aus' etc, we can remove 'v '

df['opposition'] = df['opposition'].apply(lambda x:x[2:])
print(df.head())

#Add a 'feature' - 'year' column using the match date column
#First convert date column into datetime format
df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df['year'] = df['date'].dt.year.astype(int)
print(df.head())

#The appy method is pandas allows us to apply a fucntion to each element
df['score'] = df['score'].apply(str)
df['not_out'] = np.where(df['score'].str.endswith('*'),1,0)

#dropping the odi_number feature beacause it adds no value to the analysis
df.drop(columns='odi_number',inplace=True)

#dropping those innings where Dhoni did not bat and storing in a new DataFrame
#Take all the columns, starting with runs_scored
df_new = df.loc[((df['score'] != 'DNB') & (df['score'] != 'TDNB')), 'runs_scored':]
print(df_new.head())

#fixing the data types of numerical columns
df_new['runs_scored'] = df_new['runs_scored'].astype(int)
df_new['balls_faced'] = df_new['balls_faced'].astype(int)
df_new['strike_rate'] = df_new['strike_rate'].astype(float)
df_new['fours'] = df_new['fours'].astype(int)
df_new['sixes'] = df_new['sixes'].astype(int)

#Careeer stat
first_match_date = df['date'].dt.date.min().strftime('%B %d,%Y') #first match
print('first match :', first_match_date)
last_match_date = df['date'].dt.date.max().strftime('%B %d, %Y')
#last match
print('Last match:',last_match_date)

number_of_matches = df.shape [0] #number of matches played in career
print('Number of mathes played: ', number_of_matches)
number_of_inns = df.shape [0] #number of innings
print('Number of innings played: ', number_of_inns)

not_outs = df_new ['not_out'].sum() #number of not outs in career
print('Not outs: ' ,not_outs)

runs_scored = df_new ['runs_scored'].sum() #runs in scored in career
print('Runs in scored in career: ' ,runs_scored)
balls_faced = df_new ['balls_faced'].sum() #Balls faced in rcareer
print('Balls faced in career: ' ,balls_faced)

career_sr = (runs_scored / balls_faced)*100#career strike rate
print('Career strike rate: {:.2f}'.format(career_sr))

career_avg = (runs_scored / (number_of_inns - not_outs)) #carrer average
print("Career average: {:.2f}".format(career_avg))

higest_score_date = df_new.loc[df_new.runs_scored == df_new.runs_scored.max(),'date'].values[0]

higest_score = df.loc[df.date == higest_score_date,'score'].values[0]#highest socre
print('Higest score in career:', higest_score)

hundreds = df_new.loc[df_new['runs_scored'] >= 100].shape[0]#number of 100s
print('Number of 100s: ', hundreds)

fifties = df_new.loc[(df_new['runs_scored'] >= 50) &( df_new['runs_scored']<100)].shape[0]#number of 50s
print('Number of 50s: ', fifties)


df_new['is_hundred'] = np.where((df_new['runs_scored'] >= 100),1,0)
df_new['is_fifty'] = np.where(((df_new['runs_scored'] >= 50) & (df_new['runs_scored'] <= 99)) ,1,0)


fours = df_new['fours'].sum()#Number of fours in career
print('Number of 4s :', fours)

sixes = df_new['sixes'].sum()#Number of sixes in career
print('Number of 4s :', sixes)

#number of matches played against different oppositons
df['opposition'].value_counts().plot(kind='bar',title='Number of matches against different oppostions',figsize=(8,5));
plt.show()

#Run socred against each team
runs_scored_by_opposition = pd.DataFrame(df_new.groupby('opposition')['runs_scored'].sum())
runs_scored_by_opposition.plot(kind='bar',title='Runs scored against different oppositions',figsize=(8,5))
plt.xlabel(None)
plt.show()

#This line groups the DataFrame df_new by the "oppositon"
innings_by_opposition = pd.DataFrame(df_new.groupby('opposition')['date'].count())
print(innings_by_opposition)

#Similarly this line groups teh DataFrame by "opposition" 
not_outs_by_oppostion = pd.DataFrame(df_new.groupby('opposition')['not_out'].sum())

temp = runs_scored_by_opposition.merge(innings_by_opposition,left_index=True,right_index=True)
print(temp)


average_by_opposition = temp.merge(not_outs_by_oppostion,left_index=True,right_index=True)

average_by_opposition.rename(columns = {'date':'innings'}, inplace=True)

average_by_opposition['ef_num_of_inns'] = average_by_opposition['innings'] - average_by_opposition['not_out']


average_by_opposition['average'] = average_by_opposition['runs_scored'] / average_by_opposition['ef_num_of_inns']

average_by_opposition.replace(np.inf,np.nan,inplace=True)

major_nations = ['Australia','England','New Zealand','Pakistan', 'South Africa','Sri Lanka','West Indies']

plt.figure(figsize=(8,5))

plt.plot(average_by_opposition.loc[major_nations,'average'].values, marker='o')

plt.plot([career_avg]*len(major_nations),'--')

plt.title('Average against major teams')

plt.xticks(range(0,7),major_nations)

plt.ylim(20, 70)

plt.legend('Avg against oppostions','Career avergae')

plt.show()

#Year-wise record
df['year'].value_counts().sort_index().plot(kind='bar',title='Matches played by year',figsize=(8,5))
plt.xticks(rotation=0)
plt.show()

#Run scored year-wise
df_new.groupby('year')['runs_scored'].sum().plot(kind='line',marker='o', title='Runs scored by year', figsize=(8,5))
years=df['year'].unique().tolist()
plt.xticks(years)
plt.xlabel(None)
plt.show()





























