# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
#print(data.head())

# Do not forget inplace=True
data.rename(index=str, columns={'Total' : 'Total_Medals'}, inplace=True)
print(data.head(10))


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', 'Winter'))
#print(data.head())

better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
#print(data.head())
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
#print(top_countries.tail())

top_countries.drop(top_countries.tail(1).index,inplace=True)
#print(top_countries.tail())

def top_ten(top_countries, column):
    country_list = []
    country_list = list(top_countries.nlargest(10, column)['Country_Name'])    
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
#print(top_10_summer)
top_10_winter = top_ten(top_countries, 'Total_Winter')
#print(top_10_winter)
top_10 = top_ten(top_countries, 'Total_Medals')
#print(top_10)

common = []

for element in top_10:
    if(element in top_10_summer and element in top_10_winter):
        common.append(element)

print(common)



# --------------
#Code starts here

summer_df = data[ data['Country_Name'].isin(top_10_summer) ]

winter_df = data[ data['Country_Name'].isin(top_10_winter) ]

top_df = data[ data['Country_Name'].isin(top_10) ]

summer_df.plot(x='Country_Name', y='Total_Medals', kind='bar', label='Summer')

winter_df.plot(x='Country_Name', y='Total_Medals', kind='bar', label='Winter')

top_df.plot(x='Country_Name', y='Total_Medals', kind='bar', label='Top')




# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
#print(summer_df)
summer_max_ratio = summer_df['Golden_Ratio'].max()
#print(summer_max_ratio)

max_idx = summer_df['Golden_Ratio'].idxmax()
#print(max_idx)
summer_country_gold = summer_df.at[max_idx, 'Country_Name']
#print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.at[ winter_df['Golden_Ratio'].idxmax(), 'Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.at[ top_df['Golden_Ratio'].idxmax(), 'Country_Name']





# --------------
#Code starts here
data_1 = data.copy()
data_1.drop(data_1.tail(1).index, inplace=True)
print(data_1.head())

data_1['Total_Points'] = 3*data_1['Gold_Total'] + 2*data_1['Silver_Total'] + 1*data_1['Bronze_Total']

most_points = data_1['Total_Points'].max()
print(most_points)
best_country = data_1.at[ data_1['Total_Points'].idxmax(), 'Country_Name']
print(best_country)




# --------------
#Code starts here

best = data[ data['Country_Name'] == best_country ]
#print(best)

best = best[['Gold_Total', 'Silver_Total', 'Bronze_Total']]

best.plot.bar()

plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


