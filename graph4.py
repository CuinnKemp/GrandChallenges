import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from scipy.stats import linregress

basePath = os.getcwd()

Data = pd.read_csv(basePath + "\\GDP-RedList-Growth.csv")

DF = pd.DataFrame(Data, columns=["Country Name", "Country Code",
    "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", 
    "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", 
    "2019", "2020", "2021", "RL2002", "RL2003", "RL2004", "RL2005", "RL2006", 
    "RL2007", "RL2008", "RL2009", "RL2010", "RL2011", "RL2012", "RL2013", 
    "RL2014", "RL2015", "RL2016", "RL2017", "RL2018", "RL2019", "RL2020","RL2021"])

plt.figure(figsize=(10, 4))

color_map = cm.get_cmap('tab20b', len(DF.index))
x = []
y = []
for i in DF.index:
    for j in range(2002, 2022):
        if -20 < DF.loc[i, str(j)] < 20 and -1.5 < DF.loc[i, "RL" + str(j)] < 2:
            x.append(DF.loc[i, str(j)])
            y.append(DF.loc[i, "RL" + str(j)])

plt.hexbin(x, y)

# plt.xlabel("GDP Growth")
# plt.ylabel("Red List Index Growth")
# plt.title("GDP Growth against RLI Growth for All Countries")
# plt.grid(True)

# # Adding a trend line using linear regression
# slope, intercept, r_value, p_value, std_err = linregress(x, y)
# plt.plot(x, slope * np.array(x) + intercept, color='red', linewidth=2)

# # Display the trend line equation
# equation = f'Trend Line: y = {slope:.4f}x + {intercept:.4f}'
# plt.text(0.05, 0.85, equation, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')

plt.show()
