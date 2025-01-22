# Title: "ch_5_univarite_data.py"
# Author: Brad Portouw - derived from Dr. Volkens CSU
# Date: 1/21/25

# Data

# Ozone data was collected in 2019 for the city of Fort Collins, CO, giving ozone concentration in ppm every hour.
# This ozone concentration measurement is considered univariate, thus basic exploratory data analysis approaches can be used to examine the data

# Setup: Load packages

import math
import collections
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import datetime

# Import the csv data from "ftc_o3.csv" in the data directory.
# Then rename the variables:
# - 'sample_measurement' renamed to 'ozone_ppm' for clarity
# - 'datetime' is a string, will be more useful as a date object

# Import CSV into a df
fc_ozone = pd.read_csv('../../data/ftc_o3.csv')
# Then cleanup
fc_ozone = fc_ozone[['sample_measurement', 'datetime']]
fc_ozone.dropna(axis='rows', how='any', inplace=True)
fc_ozone.rename(columns={'sample_measurement': 'ozone_ppm'}, inplace=True)
print(fc_ozone)
# here the datetime column was imported as a string, so utilizing datetime.datetime.strptime to turn into a datetime obj

# Turns out that .datetime may struggle with pandas data frames, but pandas has a similar function. pd.to_datetime()

fc_ozone['datetime']= pd.to_datetime(fc_ozone['datetime'])
# Checking to see if the type is datetime
print(fc_ozone.dtypes)
print(fc_ozone)

plt.scatter(fc_ozone['datetime'], fc_ozone['ozone_ppm'], alpha=0.1)
plt.show()

# From previous work and the scatter plot above the following can be infered at a glance:

# Location: ozone concentrations vary between 0 and 7.5 ppm and will vary depending upon the time of year, with higher values occuring during the summer.
# Dispersion: values seem to have a range of around 0.4 ppm
# Shape: While the varability of the ozone seemingly has a range of 0.4 ppm, the top 0.2 ppm of that range seemingly has higher density.

# Calculating the quartiles of fc_ozone for some basic information

quartile = np.quantile(fc_ozone['ozone_ppm'], [0, 0.25, 0.5, 0.75, 1])

print(quartile)

# The quartiles are:
# Min: 0 ppm,  Max: 0.096 ppm, Median: 0.033 ppm

# A cumulative distribution plot can provide an enumerative representation of the data:

# Starting by building a histogram of the data available with 50 bins for resolution
count, bins_count = np.histogram(fc_ozone['ozone_ppm'], bins=50)


# the probability density function is then found:
pdf_ozone = count/sum(count)

# the cumulative probability function (cdf) can be found from the pdf
cdf_ozone = np.cumsum(pdf_ozone)

# Plotting bins_count vs cdf_ozone will give a cumulative distribution plot

plt.plot(bins_count[1:], cdf_ozone)
plt.grid()
plt.show()
