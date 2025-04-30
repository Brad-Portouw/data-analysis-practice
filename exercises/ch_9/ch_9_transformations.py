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
import matplotlib.ticker as mtick
import datetime


"""
chapter 9 Exercise:

This exercise is practice at transforming and visualizing data and fitting a distribution to a set of data. Note that much of the code needed to complete this exercise 
can be adapted from (https://smogdr.github.io/edar_coursebook/transform.html#ch-9-exercises), which is a R programming textbook, but can be translated to Python

The data is from the NSF Survey of College Graduates, with a focus on salaries by college major, specifically political science students
"""

# To begin, Figure 9.8 from the text has 3 EDA plots that are recreated below, but with a log scale x-axis for payscale.

# First import the salary_ch9.csv form the data directory:
salaries = pd.read_csv('../../data/salary_ch9.csv')
print(salaries.info)
# The dataframe 'salaries' contains 2410 responses for salary, sex and major for recent college graduates in 2018.
# Because of logrithmic scaling, the salaries are divided by 1000 for clarity:
salaries['salary'] = salaries['salary'].map(lambda x: x/1000)
total_responses= len(salaries)
# Some salaries would be considered outliers, like someone making more than $500k or less than $10K
salaries= salaries[(salaries['salary']> 10) & (salaries['salary']<500)]
print(f'There were {total_responses-len(salaries)} outliers removed, either above $500k or below $10k')
# Finally make a log scaled salary column in the df
salaries['log_salary'] = salaries['salary'].map(lambda x: math.log(x,10))

# Building some basic descriptive stats grouped by sex:
salaries_gen = salaries.groupby('sex', sort=True, group_keys=True)

# First is a salary boxplot to compare salaries between men and women.
# It isn't clar that a boxplot made from a groupby object can be made horizontally, so two separate df's are made to
# generate this boxplot
salaries_m = salaries.loc[salaries['sex'] == 'M']
salaries_f = salaries.loc[salaries['sex'] == 'F']
# Putting both of these Df's into a list for the boxplot:
d = [salaries_f['salary'], salaries_m['salary']]

plt.style.use('ggplot')
EDA_plots, ax = plt.subplots(nrows=2, ncols=2)
boxplot_sal = ax[0,0].boxplot(d, vert=0, widths=0.5, tick_labels=['F', 'M'], patch_artist=True)
# boxplot_sal = plt.boxplot(d, vert=0, widths=0.5, tick_labels=['F', 'M'], patch_artist=True)
ax[0,0].set_xlabel('Salary')
ax[0,0].set_ylabel('Sex')
fmt = '${x:.0f}K'
ax[0,0].xaxis.set_major_formatter(fmt)
ax[0,0].set_xticks(np.linspace(0,400,9))

for median in boxplot_sal['medians']:
    median.set(color='chocolate',
               linewidth = 3)

colors =['salmon','cadetblue']
for patch, color in zip(boxplot_sal['boxes'], colors):
    patch.set_facecolor(color)


# plt.show()

# Next is a histogram with the data in a stacked bar orientation with 30 bins
n_bins = 30
# hist_sal, ax = plt.subplots()
hist_sal = ax[0,1].hist(d, n_bins, histtype='barstacked')
ax[0,1].set_xlabel('Salary')
ax[0,1].legend(['F','M'], title='Sex', bbox_to_anchor=(1.04, 0.5), loc='center left')
ax[0,1].set_ylabel('Count')
ax[0,1].xaxis.set_major_formatter(fmt)

# plt.show()

# Finally the cumulative distribution plot
# Need to make a cumulative probability for the plot:
cfd_sal_f = salaries_f.sort_values('salary')
cfd_sal_m = salaries_m.sort_values('salary')
# Setting each individual response as a fraction of all responses for either men or women
y_f = np.arange(1, len(cfd_sal_f)+1)/len(cfd_sal_f)
y_m = np.arange(1, len(cfd_sal_m)+1)/len(cfd_sal_m)

y = [y_f, y_m]
cfd = [cfd_sal_f['salary'], cfd_sal_m['salary']]

# With x and y(cfd) values
cumulative, ax3 = plt.subplots()
ax[1,0].plot(cfd[0],y[0], linewidth=3)
ax[1,0].plot(cfd[1],y[1], linewidth=3)
ax[1,0].legend(['F', 'M'], title='Sex',  bbox_to_anchor=(1.04, 0.5), loc='center left')
ax[1,0].set_xlabel('Salary')
ax[1,0].set_ylabel('Quantile')
ax[1,0].set_yticks([0, 0.25, 0.50, 0.75, 1.00])
ax[1,0].xaxis.set_major_formatter(fmt)

EDA_plots.suptitle('Salaries of Political Science Graduates', fontsize=20)
EDA_plots.delaxes(ax[1,1])

plt.show()

# plt.subplot(1,2,2)
# plt.plot(cfd[0],y[0])
# plt.plot(cfd[1],y[1])