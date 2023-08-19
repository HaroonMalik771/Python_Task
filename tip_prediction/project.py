import pandas as pd
import numpy as np

df = pd.read_csv("D:/Python/Python_Task/tip_prediction/E_commerce.csv")
pd.set_option('display.max_columns',14)
print(df.columns)
print(df.info())
print(df.head())
print(df.tail())