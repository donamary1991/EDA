import pandas as pd
df=pd.read_csv('/home/user/Downloads/bike_sales_100k.csv')
print(df.to_string())
print(df.shape[0])

df.drop_duplicates(inplace=True)
print(df.shape[0])
print(df.isna().sum())
df.dropna(subset='Date',inplace=True)
df.dropna(subset='Bike_Model',inplace=True)
df.dropna(subset='Store_Location',inplace=True)
df.dropna(subset='Payment_Method',inplace=True)
df.dropna(subset='Customer_Gender',inplace=True)
print(df.isna().sum())
df1=df[df['Price'].isnull()][['Bike_Model','Price']]
print(df1)
df3=df.groupby('Bike_Model')['Price'].mean()
print(df3)


df2=df.loc[(df['Bike_Model']=='Cruiser')].dropna() [['Price']]
print(df2)
cruiser_mean=round(df2.mean(),2)
print(cruiser_mean)
df3=df.loc[df['Bike_Model']=='Hybrid Bike'].dropna() [['Price']]
print(df3)
HybridBike_mean=round(df3.mean())
print(HybridBike_mean)
# df.loc[df['Bike_Model']=='Hybrid Bike'].
# print(df.isna().sum())
# df.loc[2,'Price'] = float(HybridBike_mean)
# df.loc[1,'Price'] = float(cruiser_mean)
print(df.to_string())
print(df[df['Price'].isnull()].index)


a=df[df['Price'].isnull()].index
print(a)
# df.iloc[1]=df.iloc[1].fillna(cruiser_mean)
# df.iloc[2]=df.iloc[2].fillna(HybridBike_mean)

# df1=df.loc[(df['Bike_Model']=='Hybrid Bike')&(df['Price'].isnull())].fillna(HybridBike_mean)
# print(df1.to_string())
# df.loc[(df['Bike_Model']=='Hybrid Bike')&(df['Price'].isnull())]= df.loc[(df['Bike_Model']=='Hybrid Bike')&(df['Price'].isnull())].fillna(HybridBike_mean)
# print(df.to_string())
