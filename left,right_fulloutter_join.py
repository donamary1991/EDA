import pandas as pd
dic1={'id':['1','2','3','4','5'],
      'fname':['rajeev','jay','jessy','kerli','genny'],
      'lname':['e','k','r','a','h'],
      'age':['25','26','27','30','34']}
dic2={'id':['4','5','6','7','8'],'prof':['bigdata','python','IT','IT','IT'],'salary':['25000','25000','25000','25000','25000'],'loc':['andra','jammu','kerala','delhi','up']}
df1=pd.DataFrame(dic1)
print(df1)
df2=pd.DataFrame(dic2)
print(df2)

# interview qn=left outter joining
# return complete data from left data frame and matched data values from right data frame or null returned if no matching values
df3=pd.merge(df1,df2,on='id',how='left')
print("left")
print(df3)
# interview qn=right outer joining
# return complete data from right data frame and matched data values from left data frame or null returned if no matching values
df3=pd.merge(df1,df2,on='id',how='right')
print("right")
print(df3)

# full outter
# combination of left outter joining ang right outter joining
df3=pd.merge(df1,df2,on='id',how='outer')
print("outer")
print(df3)