'''
This exercise is derived from coursework made by Professor John Volkens at Colorado State University
Title: ch_8_functionalProgramming
Written by: Brad Portouw
Created: 2/13/25
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
import datetime
from matplotlib import style
import seaborn as sns


#This exercise has a focus on writing functions, mapping them, and cleaning/plotting data

# Writing a function named 'sort_abs()'  that takes a vector of numbers as input, calculated the absolute values of each entry, and then outputs that vector
#sorted from smallest to largest values.

def sort_abs(x):
    y=[]
    for i in x:
        y.append(abs(i))
    return sorted(y)

# While the function currently isn't perfect, it will work with proper inputs. Error alerts can we written later.
print(sort_abs([-1, -5, 2]))

# With a basic function made, the next attempt is more complicated:

# Making a fuction called 'import.w.name()' to import the "date" part of the filename (in addition to the sensor ID).
# Creating a new column variable called "date_created' with this information. Use regex: '"(?<=_)[:alnum:]+(?=\\.)"'

def import_w_name(pathname):
    df = pd.read_csv(pathname)
    return df

path = ('../../data/purpleair/PA019_20181022.csv')

df = import_w_name(path)
print(df)

df.columns
