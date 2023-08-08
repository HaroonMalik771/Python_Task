import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("D:/Python/Python_Task/tips.csv")
pd.set_option('display.max_columns',81)
print(df.columns)
print(df.info())

sns.barplot(x="total_bill",y="tip",data=df,estimator=np.std)
plt.show()
sns.countplot(x='sex',data=df)
plt.show()

sns.boxplot(x='day',y='total_bill',data=df,hue='smoker')
plt.show()