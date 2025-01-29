---
title: 'Ch.3 Data Analysis Exercise'
subtitle: 'Ch. 3: Fort Collins Ozone, Dr. Volkens, CSU'
author: 'Brad Portouw'
date: '1/16/2025'
output: html_document
---

This markdown is a recreation of an exercise written by Dr. John Volkens at Colorado State University. The orginal exercise was written for use in R, but this attempt is in Python. 

# Ozone Data

The corresponding data file (.csv) for Homework 3 contains *hourly* ozone data
from two sites in Fort Collins

## Background 

Incidentally, the ozone standard is set to 0.07 parts per million (ppm).
Outdoor ozone levels are measured every hour, but the [Environmental Protection Agency](https://www.epa.gov/criteria-air-pollutants/naaqs-table) states that
the limit should be judged against an eight-hour rolling average (a
transformation that is possible in R, but outside the purview of this chapter).
Fort Collins, and most of the Front Range, is in non-attainment for this
standard, which is why you are required to get the emissions checked on your
car every year. 

# Question O: Loading Python Packages

Typically R would use readr, dplyr and tidyverse to manage data, therefore equlvalent packages are needed for Python. numpy and pandas are a likely good start:

```python
import math
import collections
import numpy as np
import pandas as pd
import csv
```

# Question 1: Preparation

## Import, Select, and Clean Data

Import the ftc_03.csv file in the working directory, select the variables below, then drop missing observations. Remember to assign to a tuple object with an informative name. 

Retain the following variables:

- 'sample_measurement' (ozone measurement in ppm)
- 'datetime' (date in YYYY-MM_DD format and time of measurement in HH:MM:SS)

'sample measurement' is a vague variable name so changing it to ozone_ppm describes the ozone measurement is in ppm.

```python
# ozone: import, select, drop missing observations, rename
# Note: Working directory is: 'C:\\Users\\Brad\\Python\\data-analysis-practice'

pd.options.display.max_rows = 16
# This may require cleanup in the form of a comprehension, but for the time being having the code work is more important
# pandas method .read_csv will make a dataframe which will utilize column names if available.
fc_ozone = pd.read_csv('ftc_o3.csv')

# By indexing only sample_measurement and datetime, the new dataframe only keeps those two columns.
fc_ozone = fc_ozone[['sample_measurement', 'datetime']]

# Method exists called .dropna() to drop rows with at least 1 NaN value (Null). Pandas will recognize two potentials as missing data:
# None: None is a python signleton object that often represents missing data
# NaN: (acronym for not a number) is a special floating point value recognized by all systems that use IEEE floting point rep.

fc_ozone.dropna(axis='rows', how='any', inplace=True)

# Note: in order to make a change to the existing dataframe, the argument inplace = True is necessary. It is False by default, making a copy

# Other potential method: just take the rows that are not NaN. I'm assuming that a few measureemnts are missing from sample_measurement column
fc_ozone = fc_ozone[fc_ozone['sample_measurement'].notna()]

# For some reason, this method above keeping all rows that don't have a missing value worked, with some rows removed.

# Finally need to rename the column from sample_measurement to ozone_ppm for clarity using .rename(columns ={'oldName1': 'newName1', 'oldName2': 'newName2'. etc})
fc_ozone.rename(columns={'sample_measurement': 'ozone_ppm'}, inplace=True)
```

## Examining the Data

Looking at the data, the dataframe fc_ozone was created from the csv 'ftc_03.csv'. Then the columns sample_measurement and datetime were kept, with sample_measurement being renamed to ozone_ppm. Finally all rows with NaN values were removed. How many observations were dropped?

```python
# Taking a look at the dataframe after modifing it
print(fc_ozone)

# How many NaN values were there in the orginal DF? Find by comparing the old DF by the new fc_ozone

print(len( pd.read_csv('ftc_o3.csv'))-len(fc_ozone))
```

# Question 2: Extract and compare

Extract the top ten ozone values and assign them to a separate object.

```python
# Extracting the top ten values and save them to a df utilizing the .nlargest(n,'column') method.
# Could also use: df.sort_values(columns, ascending=False).head(n)
top_oz_hourly = fc_ozone.nlargest(10,'ozone_ppm')
print(top_oz_hourly)
```

The bottom 10 ozone values are:
```python
# Similar to above, but utilizing df.nsmallest(n, columns)

bot_oz_hourly = fc_ozone.nsmallest(10,'ozone_ppm')
print(bot_oz_hourly)
```

Looking at the top and bottom 10 ozone values, the highest ozone concentrations seemingly occur between 7pm to 11pm, with the lowest concentrations occuring in the morning between 7am and 11am

Using the output from the prior question, on what day did the highest value occur? The lowest?
```python
# many different ways to index with pandas, but this case its probably easiest to utilize interger-based indexing with .iloc
hi_oz_time = top_oz_hourly.iloc[0,1]
print(f"The highest ozone value in ppm occured at {hi_oz_time}")

low_oz_time = bot_oz_hourly.iloc[0,1]
print(f"While the lowest ozone value occured at {low_oz_time}")
```

# Question 4: Mutate

Here a new variable ('ozone_ugm3') that provides ozone concentration in micrograms per cubic meter (ug/m3) instead of ppm. Without more atmospheric information such as temperature, pressure and humidity this wont be entirely accurate, but it is a good exercise to add a variation on the data. 

Without the real data available the following assumptions are made:

- ozone concentration in parts per million (`ozone_ppm`)
- molecular weight of ozone (47.998 g/mol)
- Celsius to Kelvin temperature conversion (K = 273.15 + C) (will be used twice but in different ways in the numerator and denominator)
- estimated atmospheric pressure in Fort Collins, CO (637 mmHg)
- universal gas constant (22.4136)
- estimated temperature in Fort Collins, CO (10$^\circ$ Celsius)

$$ 
\texttt{ozoneugm3} = 1000*\frac{\Big((\texttt{ozoneppm})(\text{molecular weight of ozone})(\text{Celsius to Kelvin value}) (\text{atmospheric pressure}) \Big)}{\Big((\text{universal gas constant})(\text{Celsius to Kelvin value} + \text{temperature})(\text{atmospheric pressure})\Big)}
$$

```python
# Create new variable of ug/m3 from ppm an doverwrite datatset
ozone_ppm = fc_ozone['ozone_ppm']

def ozoneugm3(ppm):
    # Molecular weight of ozone g/mol
    mol_wt_oz = 47.998
    #estimated temp in Fort Collins, CO, Celsius
    C = 10
    #Celsius to Kelvin Temp conversion:
    C_to_K = 273.15 + C
    #estimated atmospheric pressure in Fort Collins,CO in #mmhg
    air_pressure = 637
    #universal gas constant
    R = 22.4136
    # Conversion
    ozoneugm =  1000*(((ozone_ppm)*(mol_wt_oz)*(C_to_K)*air_pressure)/(R*(C_to_K+C)*air_pressure))
    return(ozoneugm)


# The df.assign() method may be a good use here. 
fc_ozone = fc_ozone.assign(ozone_ppm = ozoneugm3(fc_ozone['ozone_ppm']))

# Then rename the column to reflect the new units
fc_ozone.rename(columns={'ozone_ppm': 'ozone_ug/m3'}, inplace=True)
print(fc_ozone)
