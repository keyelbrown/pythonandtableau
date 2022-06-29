#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:38:01 2022

@author: ko
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read_csv

data = pd.read_csv('transaction.csv')
# variable explorer size 1047588, 1 - means only one column in file
# data is separated by ; instead of , so we need to fix this

data = pd.read_csv('transaction.csv', sep=';')
# now we have 13 columns
# type is DataFrame which just means it's a table

#summary of the data
data.info()
# shift F9 will run script for current selection/line
# object = string, float has decimals within integer
# Python Data Types on page 12 of lecture slides

#Playing around with variables

var = ['apple', 'pear', 'banana']
# list

var = ('apple', 'pear', 'banana')
#tuple - you cannot change items in list

var = range(10)

var = {'name': 'Dee', 'Location':'South Africa'}
#dict {} 

var = {'apple', 'pear', 'banana'}
# set

var = True

# working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11-11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = ProfitPerItem * NumberofItemsPurchased
CostPerTransaction = CostPerItem * NumberofItemsPurchased
SellingPricePerTransaction = NumberofItemsPurchased * SellingPricePerItem

#CostPerTransaction Columm Calculation
 
#CostPerTransaction = CostPerItem * NumberofItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased


#Adding a new column to a data frame

data['CostPerTransaction'] = CostPerTransaction
# or data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales Per Transaction

data['SalesPerTransaction'] = data['NumberOfItemsPurchased'] * data['SellingPricePerItem']

#Profit Calculation: Profit = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']


#Markup: Markup = (Sale-Cost)/Cost
data['MarkupPerTransaction'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'] ) / data['CostPerTransaction']
#or
data['MarkupPerTransaction'] = ( data['ProfitPerTransaction'] ) / data['CostPerTransaction']

#Rounding Markup
roundmarkup = round(data['MarkupPerTransaction'], 2)

data['MarkupPerTransaction'] = round(data['MarkupPerTransaction'],2)
#or
data['MarkupPerTransaction'] = roundmarkup

#Combining data fields

#my_name = 'Keyel'+'Brown'
#my_date = 'Day'+'-'+'Month'+'-'+'Year'

#my_date = data['Day']+'-'
#rec'd error because Day and '-' are different data types

#Checking columns data type
print(data['Day'].dtype)

#Change columns data type
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date


#Using iloc to view specific columns/rows
data.iloc[0] #views the row with index = 0
data.iloc[0:3] #views the first 3 rows
data.iloc[-5:] #views the last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all(:) rows in 2nd column
data.iloc[4,2] #brings in the 4th row of the 2nd column

#Using split to split client_keywords field
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#creating new columns for the split columns in client_keywords
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#Using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#Using the lower function to change item description to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()


#bringing in a new dataset - same as pulling in the trasactions.csv file
seasons = pd.read_csv('value_inc_seasons.csv')
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#How to merge/'join' files
#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')
#key = common table ('Month')
data = pd.merge(data, seasons, on = 'Month')

#Dropping Columns
#df = df.drop('columnname' , axis = 1)
#Year, Month, Day, ClientKeywords

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop('Year', axis = 1)
data = data.drop('Month', axis = 1)
#or as a list
#data = data.drop(['Year', 'Month', 'Day'] , axis = 1)

#Export into csv - index = False excludes index column, = True if you want to include it
data.to_csv('ValueInc_Cleaned.csv', index = False)






















