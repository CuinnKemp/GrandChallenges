# Plot world gdp growth and world rli growth over time

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

basePath = os.getcwd()

# Read the CSV file into a DataFrame using "Index" as the index column
Data = pd.read_csv(basePath + "\\world-growth.csv", index_col="Index")

# Create a DataFrame using the "Value" column and the existing index
DF = pd.DataFrame(Data)

y1 = [float(DF['Value'][str(i)]) for i in range(2002, 2022)]
y2 = [float(DF['Value']["RL" + str(i)]) for i in range(2002, 2022)]
x = np.array([i for i in range(2002, 2022)])

fig, ax1 = plt.subplots()

ax1.set_xlabel("Year")
ax1.set_ylabel("World GDP Growth Rate (%)", color="tab:blue")
ax1.plot(x, y1, label="World GDP Growth Rate", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx()

ax2.set_ylabel("World RLI Growth Rate (%)", color="tab:orange")
ax2.plot(x, y2, label="World RLI Growth Rate", color="tab:orange")
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
plt.title("World GDP and RLI Growth over Time")
fig.legend(loc="upper left", bbox_to_anchor=(0.15, 0.3))

plt.show()

