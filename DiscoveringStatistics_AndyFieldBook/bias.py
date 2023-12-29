from matplotlib import axes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_spss("./DataSets/DownloadFestival.sav")

# Print entire data_frame
print(data_frame)

data = data_frame["day1"]

histogram: axes.Axes = plt.subplot2grid((2, 1), (0, 0))
boxplot: axes.Axes = plt.subplot2grid((2, 1), (1, 0))

#####################################
#       Histogram               #####
#####################################

# Generate historgram of all scores arranged into 0.5 bins from 0 to just beyond the maximum score
bins = np.arange(0, max(data) + 0.5, 0.5)
histogram.hist(data, bins, edgecolor="black")

# Set x-axis label
histogram.set_xlabel("Hygeine (Day 1 Download)")

# Set y-axis label
histogram.set_ylabel("Frequency")

#####################################
#       Boxplot               #######
#####################################

# Generate boxplot of all scores and note the value of outliers
box = plt.boxplot(data, vert=True)

# Set x-axis label
boxplot.set_xlabel("Hygeine (Day 1 Download)")

# Set y-axis label
boxplot.set_ylabel("Frequency")

# Get outliers
outliers = box["fliers"][0].get_data()[1]

# Add text value to each outlier by
for outlier in outliers:
    boxplot.text(1.02, outlier, outlier)

plt.show()

#####################################
#       Z-scores               ######
#####################################

data = data_frame["day2"]
mean = np.mean(data)
std = np.std(data)

print("mean of the dataset is", mean)
print("std. deviation is", std)

# Convert all scored into z-scores
z_scores = [(y - mean) / std for y in data]

# Create thresholds for outliers at z-scores of 1.96, 2.58, and 3.29
thresholds = [1.96, 2.58, 3.29]

# Count outliers at each threshold and print the percentage frequency in table format
for threshold in thresholds:
    outliers = [y for y in z_scores if y > threshold or y < -threshold]
    print(
        "Outliers at threshold",
        threshold,
        "are",
        len(outliers),
        "out of",
        len(data),
        "or",
        len(outliers) / len(data) * 100,
        "%",
    )
