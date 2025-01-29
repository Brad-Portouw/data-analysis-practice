# Multivariate data exploration.
# Intent of this file is to analyze data from the National Survey of College Graduates (NSCG) using data regarding 2017 graudates.
# Focus on mechanical engineers.

# Setup:
import math
import collections
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import datetime
from matplotlib import style

# Import the 'ME_salaries.csv' file from the data directory

ME_sal = pd.read_csv('../../data/ME_salaries.csv', names=['Salary', 'Age', 'Gender'], skiprows=1)
print(ME_sal)