import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.graphics.gofplots as sm


data_frame = pd.read_spss("./DataSets/DownloadFestival.sav")

# Remove non existant values and outliers where the z-score is greater than 3
day1Data = data_frame["day1"].dropna()
day2Data = data_frame["day2"].dropna()
day3Data = data_frame["day3"].dropna()

day1Data = day1Data[day1Data.between(day1Data.quantile(0.01), day1Data.quantile(0.99))]
day2Data = day2Data[day2Data.between(day2Data.quantile(0.01), day2Data.quantile(0.99))]
day3Data = day3Data[day3Data.between(day3Data.quantile(0.01), day3Data.quantile(0.99))]

figure, (
    (day1_hist, day1_pp_plot),
    (day2_hist, day2_pp_plot),
    (day3_hist, day3_pp_plot),
) = plt.subplots(nrows=3, ncols=2)

day1bins = np.arange(0, max(day1Data) + 0.1, 0.2)
day2bins = np.arange(0, max(day2Data) + 0.1, 0.2)
day3bins = np.arange(0, max(day3Data) + 0.1, 0.2)

day1_data = {
    "Data": day1Data,
    "Histogram": day1_hist,
    "PP Plot": day1_pp_plot,
    "Bins": day1bins,
    "Title": "Day 2",
}

day2_data = {
    "Data": day2Data,
    "Histogram": day2_hist,
    "PP Plot": day2_pp_plot,
    "Bins": day2bins,
    "Title": "Day 2",
}

day3_data = {
    "Data": day3Data,
    "Histogram": day3_hist,
    "PP Plot": day3_pp_plot,
    "Bins": day3bins,
    "Title": "Day 3",
}

combined_data = [day1_data, day2_data, day3_data]

for data in combined_data:
    sns.histplot(
        data["Data"],
        kde=True,
        ax=data["Histogram"],
        bins=data["Bins"],
        color="blue",
        edgecolor="black",
    )

    data["Histogram"].set_xlabel(str.format("Hygeine (%s Download)", data["Title"]))
    data["Histogram"].set_ylabel("Frequency")

    sm.ProbPlot(data["Data"], fit=True).ppplot(line="45", ax=data["PP Plot"])

plt.tight_layout()
plt.show()
