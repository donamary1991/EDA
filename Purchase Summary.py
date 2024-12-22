
#txn.txt
import pandas as pd

pandademo/data frame/Assignment2.py:4
df=pd.read_csv('/home/user/Downloads/txn.txt',sep=',',header=None)
df.columns=['id','purchase_date','cust_no','amount','category','product','city','state','payment']
print(df)


# 1. Find Row count
print(df.shape[0])
# 2. jan month oid,cusno,category,product,state
# A. Row count
df1=df.loc[(df['purchase_date']>="01-01-2011")&(df['purchase_date']<="01-31-2011")].shape[0]
print(df1)
# 3. July Month oid,cusno,category,product,state
# B. Row count
df1=df.loc[(df['purchase_date']>="07-01-2011")&(df['purchase_date']<="07-31-2011")].shape[0]
print(df1)

# 4. Each category [count desc sort]
df1=df.groupby('category')['category'].count().sort_values(ascending=False)
print(df1)
# 5 Category full deatils
df1=df.loc[df['category']=='Outdoor Recreation']
print(df1)
# 6 Each paymethod count
df1=df.groupby('payment')['payment'].count()
print(df1)
# 7 jan-july purchase count
print("7**")
df1=df.loc[(df['purchase_date']>="01-01-2011")&(df['purchase_date']<="07-31-2011")]\
       .shape[0]

print(df1)
# 8 Each category total amount
df1=df.groupby('category')['amount'].sum()
print(df1)
# 9 Each category maximum amount
df1=df.groupby('category')['amount'].max()
print(df1)
# 10 Each category avg amount
df1=df.groupby('category')['amount'].mean()
print(df1)
# 11 total amount by cash and credit card
df1=df.groupby('payment')['amount'].sum()
print(df1)
# 12 Indoor games ,total amount

df1=df.loc[df['category']=='Indoor Games'].groupby('category')['amount'].sum()
print(df1)
# 13 Each state count
df1=df.groupby('state')['state'].count()
print(df1)
#



