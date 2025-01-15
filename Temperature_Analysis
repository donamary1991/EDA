import pandas as pd
df=pd.read_csv('/home/user/Downloads/Temperature',sep=' ',header=None)
df.columns=['year','temp']
# max()
df1=df.groupby('year') ['temp'].max()\
       .sort_values(ascending=False)
print(df1)

# min()
df1=df.groupby('year') ['temp'].min()\
       .sort_values(ascending=False)
print(df1)

# sum()
df1=df.groupby('year') ['temp'].sum()\
       .sort_values(ascending=False)
print(df1)
