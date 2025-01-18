# customer1.txt
#customer1.txt
import pandas as pd
df=pd.read_csv('/home/user/Downloads/customer1.txt',sep=',',header=None)
# 4000001,Kristina,Chung,55,Pilot,india
df.columns=['id','fname','lname','age','profession','loc']
print(df)
print('*'*100)
#1. fill the missing values using india
df1=df.fillna('india')
print(df1)
print('*'*100)
#2. india work fname,lname,age,prof
df1=df.loc[df['loc']=="india"]\
       [['fname','lname','age','profession']]
print(df1)
print('*'*100)
#3. Age mxm 5 employee fname,lname,age,prof
df1=df.sort_values(by='age',ascending=False)\
        [['fname','lname','age','profession']].head(5)
print(df1)
print('*'*100)
#4. Age min 3 employee fname,lname,age,prof
df1=df.sort_values(by='age')\
        [['fname','lname','age','profession']].head(3)
print(df1)
print('*'*100)
#5. uk work fname,lname,age

df1=df.loc[df['loc']=="uk"]\
       [['fname','lname','age']]
print(df1)
print('*'*100)
# 6. Age range 40 to 60 fname,lname,age,prof
df1=df.loc[(df['age']>=40)&(df['age']<=60)]\
       [['fname','lname','age','profession']]
print(df1)
print('*'*100)

# #7. india work, age mxm 2e emp fname,lname,age
df1=df.loc[df['loc']=="india"]\
       [['fname','lname','age']].head(2)
print(df1)
print('*'*100)
# #8. india work and prof Doctor fname,lname,age
df1=df.loc[(df['loc']=="india")&(df['profession']=='Doctor')]\
       [['fname','lname','age']]
print(df1)
print('*'*100)
# #9. Pilot prof, age min 1 employee fname,lname,age
df1=df.loc[(df['profession']=='Doctor')].sort_values(by='age')\
       [['fname','lname','age']].head(1)
print(df1)
print('*'*100)
# #10. Actor,age mxm 2 employee fname,lname,age
df1=df.loc[(df['profession']=='Actor')].sort_values(by='age',ascending=False)\
       [['fname','lname','age']].head(2)
print(df1)
print('*'*100)
