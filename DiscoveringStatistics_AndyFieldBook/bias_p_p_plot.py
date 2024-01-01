import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.graphics.gofplots as sm


def stats_table(dataFrame: pd.DataFrame | pd.Series, title: str):
    dataFrameMean = dataFrame.mean()
    dataFrameMode = dataFrame.mode()
    dataFrameMedian = dataFrame.median()
    dataFrameRange = dataFrame.max() - dataFrame.min()
    dataFrameStandardDeviation = dataFrame.std()
    dataFrameVariance = dataFrame.var()
    dataFrameQuartile = dataFrame.quantile([0.25, 0.5, 0.75])
    dataFrameKurtosis = dataFrame.kurtosis()
    dataFrameSkewness = dataFrame.skew()

    # Print the statistics
    print(title)
    print("\n")
    print("Mean: ", dataFrameMean)
    print("Mode: ", dataFrameMode)
    print("Median: ", dataFrameMedian)
    print("Range: ", dataFrameRange)
    print("Standard Deviation: ", dataFrameStandardDeviation)
    print("Variance: ", dataFrameVariance)
    print("Quartile: ", dataFrameQuartile)
    print("Kurtosis: ", dataFrameKurtosis)
    print("Skewness: ", dataFrameSkewness)
    print("\n")
    print("------------------------------------------------------")
    print("\n")


data_frame = pd.read_spss("./DataSets/DownloadFestival.sav")

day1Data = data_frame["day1"]
day2Data = data_frame["day2"]
day3Data = data_frame["day3"]

day1Data = day1Data.dropna()
day2Data = day2Data.dropna()
day3Data = day3Data.dropna()

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

sns.histplot(
    day1Data,
    kde=True,
    ax=day1Histogram,
    bins=day1bins,
    color="black",
    edgecolor="black",
)

sns.histplot(
    day2Data,
    kde=True,
    ax=day2Histogram,
    bins=day2bins,
    color="black",
    edgecolor="black",
)

sns.histplot(
    day3Data,
    kde=True,
    ax=day3Histogram,
    bins=day3bins,
    color="black",
    edgecolor="black",
)

sm.ProbPlot(day1Data, fit=True).ppplot(line="45", ax=day1p_p_plot)
sm.ProbPlot(day2Data, fit=True).ppplot(line="45", ax=day2p_p_plot)
sm.ProbPlot(day3Data, fit=True).ppplot(line="45", ax=day3p_p_plot)

# Set x-axis label
day1Histogram.set_xlabel("Hygeine (Day 1 Download)")
day2Histogram.set_xlabel("Hygeine (Day 2 Download)")
day3Histogram.set_xlabel("Hygeine (Day 3 Download)")

# Set y-axis label
day1Histogram.set_ylabel("Frequency")
day2Histogram.set_ylabel("Frequency")
day3Histogram.set_ylabel("Frequency")

day1stats = stats_table(day1Data, "Day 1 Stats")
day2stats = stats_table(day2Data, "Day 2 Stats")
day3stats = stats_table(day3Data, "Day 3 Stats")

plt.show()
