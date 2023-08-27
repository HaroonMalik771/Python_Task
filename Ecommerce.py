import pandas as pd
import numpy as np

df = pd.read_csv("D:/Python/Python_Task/Ecommerce_Purchases.csv")
pd.set_option('display.max_columns',14)
print(df.columns)
print(df.info())
print(df.head())
print(df.tail())
print('list of companies\n',df.Company.unique())
print('Total companies\n',df.Company.nunique())
print('list of Job \n',df.Job.unique())
print('Total Jobs \n',df.Job.nunique())
print('list of language \n',df.Language.unique())
print('Total language \n',df.Language.nunique())
print('Total CC Provider\n',df['CC Provider'].unique())
# Filter customers whose language is English..
english_customers = df[df['Language'] == 'en']

# # Select only the 'language' and 'credit_card_provider' columns for English language
english_customers_info = english_customers[['Language','CC Provider','Email']]

# Print the information
print(english_customers_info)
# simple methods 

filtered_buyers = df[(df['CC Provider'] == 'American Express') & (df['Purchase Price'] > 95)][['Email', 'CC Provider', 'Purchase Price']]

# Print the information
print(filtered_buyers)

# Filter buyers with cc_provider 'American Express' and purchase_price > 95 using query()
filtered_buyers = df.query("`CC Provider` == 'American Express' and `Purchase Price` > 95")[['Email', 'CC Provider', 'Purchase Price']]

# Print the information
print(filtered_buyers)

# sum of all rows of customers having American Express card and did purchase than 95 dollars
# use sum function and value_count() function
# display the record of the customers with credit card expiring in 2025

df['Expiry Year'] = pd.to_datetime(df['CC Exp Date'], format='%m/%y').dt.year

# Filter customers with 'CC Expiry' in 2025
customers_expiring_in_2025 = df[df['Expiry Year'] == 2025]

# Drop the 'Expiry Year' column (optional, if you don't need it)
df.drop(columns=['Expiry Year'], inplace=True)

# Print the information
print(customers_expiring_in_2025)

# RECORDS OF CUSTOMERS HAVING "cc_exp_date" in 2025
# 1-loc method
# df.loc[df['CC_Exp_Date'].str.split('/').str[-1] == '25']
# # 2- query method
# # df.query("CC_Exp_Date.str.split('/').str[-1] == '25'")