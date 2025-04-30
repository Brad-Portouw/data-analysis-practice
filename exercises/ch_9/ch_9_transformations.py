'''
This exercise is derived from coursework made by Professor John Volkens at Colorado State University
Title: ch_9_transformations
Written by: Brad Portouw
Created: 4/30/25
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


"""
chapter 9 Exercise:

This exercise is practice at transforming and visualizing data and fitting a distribution to a set of data. Note that much of the code needed to complete this exercise 
can be adapted from (https://smogdr.github.io/edar_coursebook/transform.html#ch-9-exercises), which is a R programming textbook, but can be translated to Python

The data is from teh NSF Survey of College Graduates, with a focus on salaries by college major, specifically political science students
"""

# To begin, Figure 9.8 (3 EDA plots