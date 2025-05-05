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