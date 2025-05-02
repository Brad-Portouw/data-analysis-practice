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


"""
Chapter 10 Exercises:

The following exercise focuses on working with a measurement dataset: 'airlift_mass_repeatability.csv'. 
This data represents repeated measures of "blank" air sampling filters.
"""

# First to import 'airlift_mass_repeatability.csv' into a dataframe called 'blanks'
# then perform some cleanup:
# - retain only the first 3 columns
# - rename the columns with the names 'date', 'id', and 'mass_mg';
# - convert the 'date' column vector into a date class object
# - convert the 'id' variable to a class 'factor'
# - create a new column vector named 'mass_mg' by rescaling the 'mass_g' data (i.e., convert $g$ to $mg$ by multiplying 'mass_g' by 1000

# import 'airlift_mass_repeatability.csv' form the data directory:
blanks = pd.read_csv('../../data/AIRLIFT_mass_repeatability.csv')
print(blanks)
blanks = blanks[['Date','Filter ID', 'Mass (g)']]

print(blanks.head())