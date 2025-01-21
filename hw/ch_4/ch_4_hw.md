---
title: 'MECH 476 - Python practice Dr.Volkens'
subtitle: 'Chapter 4: Visualizing Ozone Data'
author: 'Brad Portouw'
date: '1/17/25'
---

# Ozone Data

The corresponding data file (.csv) contains *hourly* ozone data from two sites in Fort Collins. This file is already available in the data folder.

# Preparation
Import important packages such as numpy and pandas for work with dataframes

```python
import math
import collections
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

```
## Import, select, and clean data

Recreating the import of the ozone data from the directory: data '\Python\data-analysis\data\ftc_o3.csv'
```python
# Import CSV into a df
fc_ozone = pd.read_csv('../../data/ftc_o3.csv')
# Then cleanup
fc_ozone = fc_ozone[['sample_measurement', 'datetime']]
fc_ozone.dropna(axis='rows', how='any', inplace=True)
fc_ozone.rename(columns={'sample_measurement': 'ozone_ppm'}, inplace=True)
```

## Examine Data

Examining the structure and contents of the dataframe to confirm the file imported and was manipulated properly.

```r
# Print will show first and last 5 indexes of the df
print(fc_ozone)
```

# Question 1: matplotlib time series
Using matplotlib to create a time series of ozone measruements across time. Ugly plot to start, but it is a good start for looking at the data

```python
plt.plot(fc_ozone['datetime'], fc_ozone['ozone_ppm'])
plt.show
```

With many data points, the plot is very messy and borderline useless, but it did generate.

# Question 3
Here the plot is made into an object for use later:
```python
# As a line chart, this data is messy, especially converting between midnight and 1am. Therefore a scatter plot is a better choice here. With nearly 17,000 data points there is much overlap, so some transparency can allow for a heat map of sorts.

o3_vs_time = plt.scatter(fc_ozone['datetime'], fc_ozone['ozone_ppm'], alpha=0.1)
plt.title("Ozone Concentration 2019 Fort Collins Colorado")
plt.xlabel("Month")
plt.ylabel("Ozone Concentration, ppm")
# The variable datetime is much too verbose to use as the x-axis. The datetime column uses strings that give the date and time instead of date objects. However the data points are collected from Jan 1st, 2019 to Jan 1st 2020. 
# the x-axis should show each month. 
month_ticks = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month_positions = np.linspace(0, len(fc_ozone)/2, num=12)
plt.xticks(month_positions, month_ticks)
plt.show()

```

# Question 4: 