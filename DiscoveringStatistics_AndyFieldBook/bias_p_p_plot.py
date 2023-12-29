import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_frame = pd.read_spss("./DataSets/DownloadFestival.sav")

day1Data = data_frame["day1"]
day2Data = data_frame["day2"]
day3Data = data_frame["day3"]

figure, axis = plt.subplots(3, 2)

day1Histogram = axis[0, 0]
day2Histogram = axis[1, 0]
day3Histogram = axis[2, 0]

day1p_p_plot = axis[0, 1]
day2p_p_plot = axis[1, 1]
day3p_p_plot = axis[2, 1]

day1bins = np.arange(0, max(day1Data) + 0.5, 0.5)
day2bins = np.arange(0, max(day2Data) + 0.1, 0.1)
day3bins = np.arange(0, max(day3Data) + 0.1, 0.1)

sns.distplot(day1Data, hist=True, kde=True, 
             ax=day1Histogram,
             bins=day1bins, color = 'black', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 1})

sns.distplot(day2Data, hist=True, kde=True, 
             ax=day2Histogram,
             bins=day2bins, color = 'black', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 1})

sns.distplot(day3Data, hist=True, kde=True, 
             ax=day3Histogram,
             bins=day3bins, color = 'black', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 1})

# Set x-axis label
day1Histogram.set_xlabel("Hygeine (Day 1 Download)")
day2Histogram.set_xlabel("Hygeine (Day 2 Download)")
day3Histogram.set_xlabel("Hygeine (Day 3 Download)")

# Set y-axis label
day1Histogram.set_ylabel("Frequency")
day2Histogram.set_ylabel("Frequency")
day3Histogram.set_ylabel("Frequency")

plt.show()
