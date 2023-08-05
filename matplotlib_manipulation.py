import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
x = np.linspace(0,5,10)
y = x**2

#functional method of ploting
plt.plot(x,y,'r--')
plt.xlabel('X label')
plt.ylabel('y label')
plt.show()