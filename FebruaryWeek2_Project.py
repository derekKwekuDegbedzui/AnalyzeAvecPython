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

## 3 - Data aggregation, filtering, sorting, grouping

# Create a DataFrame with sample data
data = pd.DataFrame({
    'Name': ["Anna", "Karen", "John", "Alice", "Kevin", "Sanna", "Bob", "Emily"],
    'Age': [35, 30, 57, 65, 25, 19, 20, 65],
    'Salary': [20000, 60000, 145000, 170000, 30000, 10000, 220000, 120000],
    'Department': ["Tech", "Tech", "Tech", "Healthcare", "Operations", "Operations", "Tech", "Tech"]
})

print(data)

# ascending
print(data.sort_values(by='Salary', ascending=True))

# descending
print(data.sort_values(by='Salary', ascending=False))

# group data
print(data.groupby("Department").count())
print(data.groupby("Department")["Name"].count())
print(data.groupby("Department")["Salary"].mean())
print(data.groupby("Department")["Salary"].min())
print(data.groupby("Department")["Age"].mean())

# filtering: boolean, isin
print(data[data["Salary"] > 100000])
print(data[(data["Salary"] > 100000) & (data["Salary"] < 200000)])

print(data[data["Age"].isin([20, 65])])

## 4 - Descriptive statistics

import numpy as np
from scipy import stats

data = [100, 20, 5, 20, 45, -100, 46]
cur_mean = np.mean(data)
print(f'Mean: {cur_mean}')
# if mean != median, data is skewed
cur_median = np.median(data)
print(f'Median: {cur_median}')
cur_mode = stats.mode(data)
print(f'Mode: {cur_mode}')
# std = sqrt of variance - average distance between each data point and mean
cur_var = np.var(data)
cur_std = np.std(data)
print(f'Var = {cur_var} | Std = {cur_std}')

# descriptive statistics of pd
print(data_csv.describe())  # 1st quantile 25%, 2nd quantile 50%, 3rd quantile 75%

## Data merging - joins

# Creating 2 dataframes
data1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'value1': [1, 2, 3, 4, 5, 6, 7]
})

data2 = pd.DataFrame({
    'key': ['C', 'D', 'E', 'F', 'G', 'H'],
    'value2': [8, 9, 10, 11, 12, 13]
})
print(data1)
print(data2)

# inner join
merge_innerjoin = pd.merge(data1, data2, on='key', how='inner')
print(merge_innerjoin)

# left join
merge_leftjoin = pd.merge(data1, data2, on='key', how='left')
print(merge_leftjoin)

# right join
merge_rightjoin = pd.merge(data1, data2, on='key', how='right')
print(merge_rightjoin)

# anti-join
# axis = 0: row
# axis = 1: column
merge_anti_join = pd.merge(data1, data2, on='key', how='left', indicator=True)
print(merge_anti_join)
merge_left_anti_join = merge_anti_join[merge_anti_join['_merge'] == 'left_only']
print(merge_left_anti_join)
print(merge_left_anti_join.drop('_merge', axis=1))