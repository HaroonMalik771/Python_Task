# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import pandas as pd

# # Generate some sample data
# df = pd.DataFrame(np.random.randint(1,7,6000), columns=['one'])
# df['two']=df['one']+np.random.randint(1,7,6000)

# # Create a histogram with KDE
# sns.histplot(df, bins=30, kde=True, color='blue', alpha=0.5)

# # Add labels and title
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.title('Histogram with KDE and Transparency')

# # Display the plot
# plt.show()

# df=pd.DataFrame(np.random.randint(1,7,6000),columns=['one'])
# df['two']=df['one']+np.random.randint(1,7,6000)
# ax = df.plot.hist(bins=10, density=True, alpha=0.7)
# df.plot.kde(ax=ax, color='red')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde

# Generate some sample data
df = pd.DataFrame(np.random.randint(1, 7, 6000), columns=['one'])
df['two'] = df['one'] + np.random.randint(1, 7, 6000)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot a histogram
ax.hist(df['one'], bins=10, density=True, alpha=0.7, label='Histogram')

# Estimate the kernel density using Gaussian KDE
kde = gaussian_kde(df['one'])
x_vals = np.linspace(df['one'].min(), df['one'].max(), 100)
kde_vals = kde(x_vals)

# Plot the KDE curve
ax.plot(x_vals, kde_vals, color='red', label='KDE')

# Add labels and a legend
ax.set_xlabel('Value')
ax.set_ylabel('Density')
ax.set_title('Histogram with KDE')
ax.legend()

# Display the plot
plt.show()
