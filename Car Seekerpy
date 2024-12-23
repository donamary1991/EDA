import pandas as pd
df=pd.read_csv('/home/user/Downloads/Car_dekho.csv')
print(df)
print(df.columns)
print(df.isna().sum())
# print(df['Name'].unique())
# print(df['mileage'].unique())
mileage_mean = df['mileage'].str.extract('(\d+.\d+)').dropna().astype(float).mean()
print(mileage_mean)
df['engine']=df['engine'].str.extract('(\d+)').astype(float)
print(df['engine'])
df['max_power'] = df['max_power'].str.extract('(\d+)').astype(float)
print(df['max_power'])


df["seats"] = df["seats"].fillna(df["seats"].mode()[0])
print(df['seats'])
df['max_power'] = df['max_power'].fillna(df['max_power'].mean())
df["engine"] = df["engine"].fillna(df["engine"].mean())
df.drop('torque',axis=1,inplace =True)
df['mileage']=df['mileage'].str.extract('(\d+.\d+)').astype(float).fillna(mileage_mean)
print(df['mileage'])
print(df.isna().sum())






