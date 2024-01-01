import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.graphics.gofplots as sm

data_frame = pd.read_spss("./DataSets/DownloadFestival.sav")

day1Data = data_frame["day1"]
day2Data = data_frame["day2"]
day3Data = data_frame["day3"]

day1Data = day1Data.dropna()
day2Data = day2Data.dropna()
day3Data = day3Data.dropna()

day1Data = day1Data[day1Data.between(day1Data.quantile(0.01), day1Data.quantile(0.99))]
day2Data = day2Data[day2Data.between(day2Data.quantile(0.01), day2Data.quantile(0.99))]
day3Data = day3Data[day3Data.between(day3Data.quantile(0.01), day3Data.quantile(0.99))]

k_s_day1 = stats.kstest(day1Data, "norm")
k_s_day2 = stats.kstest(day2Data, "norm")
k_s_day3 = stats.kstest(day3Data, "norm")

# Print count of values in each data set
print("Count of values in Day 1: ", len(day1Data))
print("Count of values in Day 2: ", len(day2Data))
print("Count of values in Day 3: ", len(day3Data))
print("K-S Test for Day 1: ", k_s_day1)
print("K-S Test for Day 2: ", k_s_day2)
print("K-S Test for Day 3: ", k_s_day3)

# Create a table with count and K-S test results for each day
data = {
    "Day": ["Day 1", "Day 2", "Day 3"],
    "Count": [len(day1Data), len(day2Data), len(day3Data)],
    "K-S Test Value": [k_s_day1.statistic, k_s_day2.statistic, k_s_day3.statistic],
    "K-S Test P-Value": [k_s_day1.pvalue, k_s_day2.pvalue, k_s_day3.pvalue],
}

data_frame = pd.DataFrame(data)
print(data_frame)

# Plot the qqplot for each day
figure, axis = plt.subplots(3, 1)
day1p_p_plot = axis[0]
day2p_p_plot = axis[1]
day3p_p_plot = axis[2]

sm.ProbPlot(day1Data, fit=True).qqplot(line="45", ax=day1p_p_plot)
sm.ProbPlot(day2Data, fit=True).qqplot(line="45", ax=day2p_p_plot)
sm.ProbPlot(day3Data, fit=True).qqplot(line="45", ax=day3p_p_plot)

plt.show()
