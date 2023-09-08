import pandas as pd
import os
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np
from matplotlib.colors import ListedColormap, Normalize, LinearSegmentedColormap


basePath = os.getcwd()

# Read the data and map
Data = pd.read_csv(basePath + "\\CorrelationCountry.csv")
map_df = gpd.read_file(basePath + "\\world-administrative-boundaries.shp")

# Merge the data with the map
identifier_column_name = "color_code"
plotCOL = "slope"

DF = pd.DataFrame(Data, columns=["Country Name", "color_code", "slope", "r_value", "p_value"])
kDF = map_df.merge(DF[["color_code", plotCOL]], left_on=identifier_column_name, right_on="color_code", how="left")

# Replace NaN values with 0 (or any other value you prefer)
# kDF[plotCOL].fillna(0, inplace=True)

# Set the background color of the plot
fig, ax = plt.subplots(1, 1, figsize=(10, 12))
fig.patch.set_facecolor((0.50, 0.50, 0.50))  # Set the background color to light grey-blue

# Create a custom diverging color map with reds below 0 and blues above 0
neg_colors = [(1, 0, 0), (1, 1, 1)] # first color is black, last is red
neg_cm = LinearSegmentedColormap.from_list("Custom", neg_colors)

xneg_colors = [(1, 0, 0), (1, 0, 0)] # first color is black, last is red
xneg_cm = LinearSegmentedColormap.from_list("Custom", xneg_colors)

pos_colors = [(0, 0, 1), (0, 0, 1)]
pos_cm = LinearSegmentedColormap.from_list("Custom", pos_colors)

neu_colors = [(1, 1, 1), (0, 0, 1)] # first color is black, last is red
neu_cm = LinearSegmentedColormap.from_list("Custom", neu_colors)

# colors_xneg = plt.cm.get_cmap(xneg_cm)(np.linspace(0, 1, 82))
# colors_neg = plt.cm.get_cmap(neg_cm)(np.linspace(0, 1, 83))
# colors_pos = plt.cm.get_cmap(pos_cm)(np.linspace(0, 1, 220))
# colors_neu = plt.cm.get_cmap(neu_cm)(np.linspace(0, 1, 220))

colors_neg = plt.cm.get_cmap(neg_cm)(np.linspace(0, 1, 110))
colors_neu = plt.cm.get_cmap(neu_cm)(np.linspace(0, 1, 85))
colors = np.vstack((colors_neg, colors_neu))
# colors = np.vstack((colors_xneg,colors_neg, colors_neu, colors_pos))
cmap = ListedColormap(colors)

# Plot the data, coloring countries without data as black
kDF.plot(column=plotCOL, ax=ax, cmap=cmap, edgecolor='black', linewidth=0.3, legend=True)

# Set custom color intervals for the legend
values = kDF[plotCOL].values
norm = Normalize(vmin=values.min(), vmax=values.max())
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])  # This line is necessary for the color bar to work properly

# ax.set_title(plotCOL)
ax.set_axis_off()

plt.subplots_adjust(left=0.05, right=1, bottom=0.1, top=0.9)

plt.show()
print("Negative Slope:")
for index in DF.index:
    if DF["slope"][index] < -0.009:
        print(DF["Country Name"][index])
print()
print("Positive Slope:")
for index in DF.index:
    if DF["slope"][index] > 0.009:
        print(DF["Country Name"][index])
