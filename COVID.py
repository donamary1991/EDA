# 1. Download raw dataset
import pandas as pd
# 2. Loading dataset and extracting date list
confirmed_df = pd.read_csv('/home/user/Downloads/time_series_covid19_confirmed_global.csv')
deaths_df = pd.read_csv('/home/user/Downloads/time_series_covid19_deaths_global.csv')
recovered_df = pd.read_csv('/home/user/Downloads/time_series_covid19_recovered_global.csv')
print(confirmed_df)
print(deaths_df )
print(recovered_df)
print(confirmed_df.columns)
print(confirmed_df.columns[4:])
dates = confirmed_df.columns[4:]
# we need to use melt() to unpivot DataFrames from current wide format into long format.
# In other words, we are kinda transposing all date columns into values.

confirmed_df_long = confirmed_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    value_vars=dates,
    var_name='Date',
    value_name='Confirmed'
)
deaths_df_long = deaths_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    value_vars=dates,
    var_name='Date',
    value_name='Deaths'
)
recovered_df_long = recovered_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    value_vars=dates,
    var_name='Date',
    value_name='Recovered'
)
# print(recovered_df_long[recovered_df_long['Country/Region']=='Canada'])
print(confirmed_df_long)
print(deaths_df_long)
print(recovered_df_long)
# we have to remove recovered data for Canada due to mismatch issue
# (🤷‍♂ Canada recovered data is counted by Country-wise rather than Province/State-wise).
recovered_df_long = recovered_df_long[recovered_df_long['Country/Region']!='Canada']

# 3. Merging Confirmed, Deaths and Recovered

# Merging confirmed_df_long and deaths_df_long
full_table = confirmed_df_long.merge(
  right=deaths_df_long,
  how='left',
  on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']

)# Merging full_table and recovered_df_long

full_table = full_table.merge(
  right=recovered_df_long,
  how='left',
  on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)
print(full_table)

print(full_table.columns)
# 4. Performing Data Cleaning
#
# There are 3 tasks we would like to do
#
#     Converting Date from string to datetime
#     Replacing missing value NaN
#     Coronavirus cases reported from 3 cruise ships should be treated differently
#
# You probably already notice that the values in the new Date column are
# all string with m/dd/yy format. To convert Date values from string to datetime,

full_table['Date'] = pd.to_datetime(full_table['Date'])

# Missing values NaN can be detected by running
print(full_table.isna().sum())
# NaNs in Recovered and let’s replace them with 0.
full_table['Recovered']=full_table['Recovered'].fillna(0)
# print(full_table)
# And here is how we extract the ship data.

# Pandas Series.str.contains() function is used to test
# if pattern or regex is contained within a string of a Series or Index.
# The function returns boolean Series or
# Index based on whether a given pattern or regex is contained within a string of a Series or Index.
ship_rows = full_table['Province/State'].str.contains('Grand Princess') \
                                         | full_table['Province/State'].str.contains('Diamond Princess') \
                                         | full_table['Country/Region'].str.contains('Diamond Princess') \
                                         | full_table['Country/Region'].str.contains('MS Zaandam')
print(f'ship rows are{ship_rows}')
full_ship = full_table[ship_rows]
print(ship_rows)
print("full_table[ship_rows]",full_table[ship_rows])
# And to get rid of ship data from full_table :
full_table = full_table[~(ship_rows)]
# to drop a column
# full_table = full_table.drop('Country/Region',axis=1)
# print(full_table)
# 5. Data Aggregation
# add an active cases column Active, which is calculated by active = confirmed — deaths — recovered .
# full_table['Active']=full_table['Confirmed']- full_table['Deaths']-full_table['Recovered']
full_table['Active'] = full_table['Confirmed'] - full_table['Deaths'] - full_table['Recovered']
print(full_table)
    # sum() is to get the total count of ‘Confirmed’, ‘Deaths’, ‘Recovered’, ‘Active’ for the given Date and Country/Region.
    # reset_index() reset the index and use the default one, which is Date and Country/Region.
full=full_table[['Date','Country/Region','Confirmed', 'Deaths', 'Recovered', 'Active']]
print("full",full)
full_grouped = full_table.groupby(['Date','Country/Region'])[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum().reset_index()
print(full_grouped)
print(full_table.columns)
full_grouped.to_csv('/home/user/Downloads/COVID-19-time-series-clean-complete.csv')