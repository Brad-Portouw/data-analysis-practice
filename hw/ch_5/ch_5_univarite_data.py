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