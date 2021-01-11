import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

apr_data = pd.read_csv("uber/uber-raw-data-apr14.csv")
may_data = pd.read_csv("uber/uber-raw-data-may14.csv")
jun_data = pd.read_csv("uber/uber-raw-data-jun14.csv")
jul_data = pd.read_csv("uber/uber-raw-data-jul14.csv")
aug_data = pd.read_csv("uber/uber-raw-data-aug14.csv")
sep_data = pd.read_csv("uber/uber-raw-data-sep14.csv")

uber_data = pd.concat([apr_data, may_data, jun_data,
                       jul_data, aug_data, sep_data])

print(uber_data.head())

uber_data["Date/Time"] = pd.to_datetime(uber_data["Date/Time"])

# print(uber_data.head())

uber_data["Date"] = uber_data["Date/Time"].apply(lambda x: x.date())
# uber_data["Month"] = uber_data["Date/Time"].apply(lambda x: x.month)
# uber_data["OnlyDate"] = uber_data["Date/Time"].apply(lambda x: x.day)
# uber_data["DayOfTheWeek"] = uber_data["Date/Time"].apply(lambda x: x.dayofweek)
# uber_data["Hour"] = uber_data["Date/Time"].apply(lambda x: x.hour)

uber_data["Base"] = uber_data["Base"].apply(lambda x: int(x.replace('B', '')))

print(uber_data.head())

print(uber_data["Date"])
print(uber_data["Base"])

# my_plot = plt.bar(x=uber_data["Date"], height=uber_data["Base"])
# my_plot.show()
