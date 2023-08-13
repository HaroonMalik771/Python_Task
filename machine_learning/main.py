import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
df = pd.read_csv("D:/Python/Python_Task/machine_learning/USA_Housing.csv")
print(df.columns)
# print(df.info())
# print(df.head())
# print(df.describe())
sns.pairplot(df)
# print(df.corr())
# heat map
# sns.heatmap(df.corr(),annot=True)
# plt.show()
