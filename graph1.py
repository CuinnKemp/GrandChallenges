# Plot World GDP and World RLI over time
# create a overlaid graph of gdp and rli over time
# create a scatter plot of GDP vs RLI

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

basePath = os.getcwd()

# Read the CSV file into dataframe
Data = pd.read_csv(basePath + "\\world.csv", index_col="Index")

# Create a DataFrame
DF = pd.DataFrame(Data)

# create the x,y1 and x,y2 values
y1 = [float(DF['Value'][str(i)])/(10**13) for i in range(2002, 2022)]
y2 = [float(DF['Value']["RL" + str(i)]) for i in range(2002, 2022)]
x = np.array([i for i in range(2002, 2022)])

#create first axis
fig, ax1 = plt.subplots()

#plot gdp and year
ax1.set_xlabel("Year")
ax1.set_ylabel("World GDP (10^13 USD)", color="tab:blue")
ax1.plot(x, y1, label="World GDP", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")

#create second axis
ax2 = ax1.twinx()

# plot rli and year
ax2.set_ylabel("World RLI", color="tab:orange")
ax2.plot(x, y2, label="World RLI", color="tab:orange")
ax2.tick_params(axis="y", labelcolor="tab:orange", bottom=False)

# Add lines of best fit
coeffs1 = np.polyfit(x, y1, 1)
line_fit1 = np.polyval(coeffs1, x)
ax1.plot(x, line_fit1, linestyle='dashed', color='tab:blue', label='GDP Trend')

coeffs2 = np.polyfit(x, y2, 1)
line_fit2 = np.polyval(coeffs2, x)
ax2.plot(x, line_fit2, linestyle='dashed', color='tab:orange', label='RLI Trend')

ax1.set_xticks(x)
ax1.set_xticklabels(x)
fig.tight_layout()
plt.title("World GDP and RLI Over Time")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.45))

#show plot
plt.show()

#create scatter plot
plt.scatter(y1,y2)
plt.title("World GDP vs RLI")
plt.ylabel("World Red List Index")
plt.xlabel("World GDP (10^13 USD)")

slope, intercept, r_value, p_value, std_err = linregress(y1, y2)
plt.plot(y1, slope * np.array(y1) + intercept, linestyle='dashed')
equation = f'Trend Line: y = {slope:.4f}x + {intercept:.4f} | R-Value: {r_value:.4f}'
plt.text(0.05, 0.1, equation, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')
plt.show()