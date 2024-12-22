import pandas as pd
df=pd.read_csv('/home/user/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','profession','loc']
# Assignment1
# ..................................
# customer
# .................................
# 1. Find Row count
df1=df.shape[0]
print(df1)
print('*'*100)
# 2. Remove duplicates rows and find total row count
df1=df.drop_duplicates().shape[0]
print(df1)
print('*'*100)
# 3. Age maximum 10 fname,lname,prof,loc
df1=df.sort_values(by='age',ascending=False)\
        [['fname','lname','profession','loc']].head(10)
print(df1)
print('*'*100)
# 4. Age minimum 5 employees fname,lname,prof,loc
df1=df.sort_values(by='age')\
        [['fname','lname','profession','loc']].head(5)
print(df1)
print('*'*100)
# 5. Each location count [count desc order]
df1=df.groupby('loc')['loc'].count().sort_values(ascending=False)
print(df1)
print('*'*100)
# 6. Full data
df1=df.loc[df['loc']=='australia'][['id','fname','lname','age','profession']]
print(df1)
print('*'*100)
# 7. Each age group count [age desc order]
df1=df.groupby('age')['age'].count().sort_values(ascending=False)
print(df1)
print('*'*100)
# 8. Each profession count [count desc order]
df1=df.groupby('profession')['profession'].count().sort_values(ascending=False)
print(df1)
print('*'*100)
# 9. India work
# A. Row count
df1=df.loc[df['loc']=='india'].shape[0]
print(df1)
print('*'*100)
# B. Each profession count [count desc order]
df1=df.loc[df['loc']=='india'].groupby('profession')['profession'].count().sort_values(ascending=False)
print(df1)
print('*'*100)
# C. Age mxm 3 employees fname,lname,age,prof
df1=df.loc[df['loc']=='india'].sort_values(by='age',ascending=False)[['fname','lname','age','profession']].head(3)
print(df1)
print('*'*100)
# D. Age minimum 3 employees fname,lname,age,prof
df1=df.loc[df['loc']=='india'].sort_values(by='age')[['fname','lname','age','profession']].head(3)
print(df1)
print('*'*100)
# E. age above 40 full data
df1=df.loc[(df['loc']=="india")&(df['age']>40)]\
       [['fname','lname','age','profession']]
print(df1)
print('*'*100)
# F. age range 30 to 40 [profession count]
print('#'*100)
df1=df.loc[(df['loc']=="india")&((df['age']>=30)&(df['age']<=40))].groupby('profession')['profession'].count()

print(df1)
print('*'*100)
# 10. us work

# A. Row count
df1=df.loc[df['loc']=='us'].shape
print(df1)
print('*'*100)
# B. Each age group count
df1=df.loc[df['loc']=='us'].groupby('age')['age'].count()
print(df1)
print('*'*100)
# C. Each profession count [count desc]
df1=df.loc[df['loc']=='us'].groupby('profession')['profession'].count().sort_values(ascending=False)
print(df1)
print('*'*100)
# D. Civil engineer dept and age above 30
df1=df.loc[(df['loc']=="us")&((df['profession']=='Civil engineer')&(df['age']>30))]\
       [['fname','lname','age','profession']]
print(df1)
print('*'*100)

df1=df.loc[df['loc']=='australia']
print(df1)