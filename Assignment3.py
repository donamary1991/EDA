
# movies_cleaned_pandas.csv
import pandas as pd
df=pd.read_csv("/home/user/Downloads/movies_cleaned_pandas.csv",sep=',',header=None)
df.columns=['no','movie','year','rating','dur']
print(df)

# 2,The Mummy,1932,3.5,4388.0
#  df.columns=['no','movie','year','rating','dur']
# 1. Find row count
df1=df.shape[0]
print(df1)
# 2. Remove duplicates and find row count
df1=df.drop_duplicates().shape[0]
print(df1)     
# 3.Sort data set by release year in des order
df1=df.sort_values(by='year',ascending=False)
print(df1)
# 4. Find rating mxm 5 movies name,year,rating
df1=df.sort_values(by='rating',ascending=False) [['movie','year','rating']].head()
print(df1)
# 5. Find rating minimum 3 movies name,year,rating
df1=df.sort_values(by='rating') [['movie','year','rating']].head(3)
print(df1)                                                                          
# 6. Find Each year release movie count [count desc order]
df1=df.groupby('year')['year'].count().sort_values(ascending=False)
print(df1)                                                                    
# 7. Each rating count [count desc order]
df1=df.groupby('rating')['rating'].count().sort_values(ascending=False)
print(df1)
# 8. 2008 and rating above 3 [collect]
df1=df.loc[(df['year']==2008)&(df['rating']>3)]
print(df1)
# A. row count
df1=df.loc[(df['year']==2008)&(df['rating']>3)].shape[0]
print(df1)
# 9. Find duration mxm 1 movies name,year,rating,duration
df1=df.sort_values(by='dur',ascending=False)[['movie','year','rating','dur']].head(1)
print(df1)
# 10. Find rating mnm 1 movies name,year,rating,duration
df1=df.sort_values(by='rating') [['movie','year','rating','dur']].head(1)
print(df1)
# 11. Rating above 4 and relase year above 2005
df1=df.loc[(df['rating']>4)&(df['year']>2005)]
print(df1)
# A. Rating mxm movies full data
df1=df1.loc[(df['rating']==4.5)].sort_values(by='rating',ascending=False)
print(df1)
# B. Rating mnm movies full data
df1=df.loc[(df['rating']==4.1)&(df['year']>2005)].sort_values(by='rating')
print(df1)
# 12. 2008 movies count
df1=df.loc[df['year']==2008].shape[0]
print(df1)
# 13. 1975-2000 movies collect
df1=df.loc[(df['year']>=1975)&(df['year']<=2000)]
print(df1)
# A. Row count
df1=df.loc[(df['year']>=1975)&(df['year']<=2000)].shape[0]
print(df1)
# 14. 1975-2000 and rating above 3.5 total row count
df1=df.loc[(df['year']>=1975)&(df['year']<=2000)&(df['rating']>3.5)].shape[0]
print(df1)