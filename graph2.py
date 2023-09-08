# Plot GDP against RLI for all countries
# creates a scatter plot of rli vs gdp

import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm  # Import color map module

basePath = os.getcwd()

Data = pd.read_csv(basePath + "\\GDP-RedList.csv")

DF = pd.DataFrame(Data, columns=["Country Name", "Country Code",
    "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", 
    "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", 
    "2019", "2020", "2021", "RL2002", "RL2003", "RL2004", "RL2005", "RL2006", 
    "RL2007", "RL2008", "RL2009", "RL2010", "RL2011", "RL2012", "RL2013", 
    "RL2014", "RL2015", "RL2016", "RL2017", "RL2018", "RL2019", "RL2020", "RL2021"])

plt.figure(figsize=(10, 4))  # Adjust figure size if needed

# Get a color map with more colors
color_map = cm.get_cmap('tab20b', len(DF.index))

for i in DF.index:
    x = DF.loc[i, "2002":"2021"].values
    y = DF.loc[i, "RL2002":"RL2021"].values
    country_code = DF.loc[i, "Country Code"]
    plt.plot(x, y, color=color_map(i), label=country_code)  # Assign color from the color map

plt.xscale("log")
plt.xlabel("GDP")
plt.ylabel("Red List Index")

# Legend settings with multiple columns
# legend = plt.legend(ncol=6)  # Set the number of columns in the legend
# plt.setp(legend.get_texts(), fontsize='xx-small')  # Set legend font size
# legend.set_bbox_to_anchor((1, 1.02))  # Adjust legend position within the plot

plt.title("GDP vs. Red List Index for All Countries")
plt.grid(True)

# Adjust subplot parameters for better spacing around the plot
# plt.subplots_adjust(left=0.05, right=1, bottom=0.1, top=0.9)

plt.show()
