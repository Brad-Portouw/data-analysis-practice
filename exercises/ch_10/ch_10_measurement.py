'''
This exercise is derived from coursework made by Professor John Volkens at Colorado State University
Title: ch_10_measurement
Written by: Brad Portouw
Created: 5/2/25
output: .py file
'''

# Setup
import math
import collections
import numpy
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import datetime
from datetime import date
from datetime import datetime
import time
import os
from collections import Counter
import statistics
"""
Chapter 10 Exercises:

The following exercise focuses on working with a measurement dataset: 'airlift_mass_repeatability.csv'. 
This data represents repeated measures of "blank" air sampling filters.
"""

# First to import 'airlift_mass_repeatability.csv' into a dataframe called 'blanks'
# then perform some cleanup:
# - retain only the first 3 columns
# - rename the columns with the names 'date' and 'id';
# - convert the 'date' column vector into a date class object
# - convert the 'id' variable to a categorical dtype
# - create a new column vector named 'mass_mg' by rescaling the 'mass_g' data (i.e., convert $g$ to $mg$ by multiplying 'mass_g' by 1000

# import 'airlift_mass_repeatability.csv' form the data directory:
blanks = pd.read_csv('../../data/AIRLIFT_mass_repeatability.csv')
print(blanks)
blanks = blanks[['Date','Filter ID', 'Mass (g)']]

# Renaming the columns: 'date', 'id', and 'mass_mg'
blanks.rename(columns={'Date':'date', 'Filter ID':'id', 'Mass (g)':'mass_g'}, inplace=True)

# Converting date to a datetime object:
df_len = len(blanks)
for j in range(0, df_len):
    blanks.iloc[j, 0] = datetime.strptime(blanks.iloc[j,0],"'%d-%b-%Y'").date()


# Converting the id column into a catgorical type
blanks["id"] = pd.Categorical(blanks.id)

# Now to make a new column for mass in milligrams
blanks['mass_mg'] = blanks['mass_g'].map(lambda x: x*1000)
print(blanks)

# Next checking for any NA data in the DF
print(blanks.isna().sum())
# THere appears to be no NaN values in the data

# Checking the number samples for each unique sensor ID
ID_numbers = Counter(blanks.id).keys()
ID_counts = Counter(blanks.id).values()

date_numbers = Counter(blanks.date).keys()
print(date_numbers)
print(f'There are {len(ID_numbers)} unique filter IDs present in the dataframe')
print('All sensors have 78 samples except sensor 41669 which has 76')

# Checking the period of time the measurements were taken:
print(f'Measurements were taken over {max(blanks.date)-min(blanks.date)} between {min(blanks.date)} and {max(blanks.date)}')

# Grouping the 'blanks data frame by 'id' to calculate the mean, meadian, and standard deviations for each filter ID

blanks_byID = blanks.groupby('id', observed=True)
print(blanks_byID)
print(blanks_byID.mass_mg.describe())
# The describe function doesn't show the median:
print(f'The median of the the mass_mg readings is:')
print(blanks_byID.mass_mg.median())

# Calculating the limit of detection (LOD) for this measurement method.
# Will require standard deviations for each filter, then estimate LOD from -> LOD = mean + 3*SD
mean_byID = blanks_byID.mass_mg.mean()
sd_byID = blanks_byID.mass_mg.agg(np.std,ddof=0)
# With both values in lists, the LOD of each sensor can be calculated.

LOD_mg_upperbound = mean_byID + 3*sd_byID
LOD_mg_lowerbound = mean_byID - 3*sd_byID
# The limit of detection is the difference between both the upper and lower bounds
LOD = LOD_mg_upperbound - LOD_mg_lowerbound
# All info presented in a dataframe:
LOD_df = pd.concat([LOD,LOD_mg_upperbound, LOD_mg_lowerbound], axis=1)
LOD_df.columns = ['LOD', 'mg_upper', 'mg_lower']
print(LOD_df)

# It appears that the actual limits of detection of these sensors probably cannot be determined from this data as the
# range of values is so small. The variance seen could be due to error in the sensor. 