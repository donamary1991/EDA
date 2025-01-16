# how to handle wrong data
from crypt import methods
from importlib.metadata import files

# height    weight
# 150             70
# 180             85
# 170             60
# 155             75
# 140             45
# 350             89


# school mark==out of 50===wrong data==80
# machine learning wrong data is called outliers
import pandas as pd
from numpy.ma.extras import column_stack

df=pd.read_csv('/home/user/Downloads/missing_data.csv',sep=',')
print(df)
# df.loc[7,'Duration']=45
# print(df)

# if calories above 400 are wrong data,replace it with its mean
x=df['Calories'].mean()
for i in df.index:
    if df.loc[i,'Calories']>400:
        df.loc[i,'Calories']=x
print(df)




# heart.csv

# 1.create a dataframe
df=pd.read_csv('/home/user/Downloads/heart.csv',sep=',')
print(df)
# 2.print shape of dataframe
print(df.shape)
# 3.print column names of dataframe
print(df.columns)
# 4.print datatypes of each column_stack
print(df.dtypes)
# 5.Find Total number of missing values
print(df.isna().sum())
# 6.Separate x and y y:last column x:remaining columns
x=df.iloc[:,:-1]
print(x)
y=df.iloc[:,-1]
print(y)
# 7.each target count[count desc]
df1=df.groupby('target')['target'].count().sort_values(ascending=False)
print(df1)
# 8.fill the missing value using proper methods
# unique values identified by
print(df['trestbps'].unique())
x=df['trestbps'].mean()

df1=df['trestbps'].fillna(x,inplace=True)
print(df)
# unique values identified by
print(df['trestbps'].unique())
x=df['restecg'].mode()[0]
df['restecg'].fillna(x,inplace=True)
print(df)
# unique values identified by
print(df['thalach'].unique())
x=df['thalach'].mean()
df['thalach'].fillna(x,inplace=True)
print(df)
# unique values identified by
print(df['ca'].unique())
x=df['ca'].mode()[0]
df['ca'].fillna(x,inplace=True)
print(df)

x=df['thal'].mode()[0]
df['thal'].fillna(x,inplace=True)
print(df)

# 9.thalach value above 180==wrong data==,mean fill
x=df['thalach'].mean()
for i in df.index:
    if df.loc[i,'thalach']>180:
        df.loc[i,'thalach']=x
print(df)
print(df.isna().sum())
# to_csv
# after cleaning we have to convert to csv files()
df.to_csv('/home/user/Downloads/heart1',index=False)
# if index=False is not there ,file will show an index column too
df.to_csv('/home/user/Downloads/heart2',index=False,header=None)
