## Weekly Weekend Hands-on Project
# Hands-on Projects with EDA, AB Testing & Business Intelligence
# https://youtu.be/FTpmwX94_Yo?list=PLrpC1AhCG6Yd4BIC-HerhHUvPo1PC9Os8

## 1 - Loading Data
# always check 1st and last

import pandas as pd
import sqlite3

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.reset_option('display.max_columns')
# pd.reset_option('display.max_rows')

data_csv = pd.read_csv("percent_bachelors_degrees_women_usa.csv")
print(data_csv)

data_txt = pd.read_csv("StudentSchools.txt", header=0, sep=',')
print(data_txt)

# connection_db = sqlite3.connect("database_name.db")
# query_1 = 'SELECT col_1 FROM table_name'
# query_2 = 'SELECT * FROM table_name'
# data_sql = pd.read_sql(query_2, connection_db)

## 2 - Data exploration and preprocessing

print(data_csv.head(10))
print(data_csv.tail(10))
print(data_csv.info())

# how to drop missing values: if NaN exist, drop it
# data_csv.dropna()
# data_csv.fillna("NULL")

# drop duplicates
# data_csv.drop_duplicates()

# index: iloc or loc
# iloc: position-based selection: integer positions (zero-based index)
# loc: label-based selection

# feature:      .loc[]          .iloc[]
# selection     label-based     position-based
# indexing      index labels    integer positions
# slicing       + stop index    no stop index
# performance   slightly lower  faster

# get specific row
print(data_csv.iloc[10])
# get specific columns
print(data_csv.loc[10])
print(data_csv.loc[:, 'Biology'])

cur_data = pd.DataFrame({
    'A1': [1, 2, 3],
    'A2': [4, 5, 6],
    'A3': [7, 8, 9]},
    index=['X', 'Y', 'Z'])
print(cur_data)
# Using loc
print(cur_data.loc['X'])
print(cur_data.loc[:, 'A2'])


