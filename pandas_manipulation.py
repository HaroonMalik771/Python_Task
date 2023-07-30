import pandas as pd
import numpy as np

# most frequently used data set
# filter result also save in csv file

df = pd.read_csv("D:/Python/Python_Task/fifa.csv")
pd.set_option('display.max_columns',81)
print(df.columns)
print(df.info())
try:
    print(df.head())
except UnicodeEncodeError:
    print(df.head().to_string().encode('utf-8'))

df_filter = df.head()
#df_filter.to_csv('first_5.csv')
print('Total numbers of records',len(df))

# by query method
# df_filter = df.query("shooting > passing ")[['short_name','shooting','passing']]
# print("palyer which have shooting value > passing value\n",df_filter)

# Assuming 'shooting' and 'passing' are columns in the DataFrame

condition = df['shooting'] > df['passing']
df_filter = df.loc[condition, ['short_name', 'shooting', 'passing']]
print("Players who have shooting value > passing value:\n", df_filter)

print("list of countries\n",df.nationality.unique())
print("Total countries\n",df.nationality.nunique())

