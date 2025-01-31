# Multivariate data exploration.
# Intent of this file is to analyze data from the National Survey of College Graduates (NSCG) using data regarding 2017 graudates.
# Focus on mechanical engineers.

# Setup:
import math
import collections

import numpy
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import datetime
from matplotlib import style

# Import the 'ME_salaries.csv' file from the data directory

me_sal = pd.read_csv('../../data/ME_salaries.csv', names=['Salary', 'Age', 'Gender'], skiprows=1)
print(me_sal.info())

# Looking at respondents who didn't list their salary, pd.isnull isn't working to find empty arrays of "" recorded for salary.
# However there are 15 respondents who answered having 0 for their salary:
me_no_sal = me_sal.loc[me_sal['Salary'] == 0]

# Therefore it would make sense to remove these responses at outliers, there could be many reasons why someone would list their salary at 0.
me_sal = me_sal.loc[me_sal['Salary'] != 0]
# Need to reset the index after removing some rows:
me_sal.reset_index(drop=True, inplace=True)

# Taking a look at the genders shown in the dataframe:
print(me_sal.Gender.value_counts())

# It appears that 3228 men and 373 women responded with no other possible gender identities being listed.

# With the data imported, plots could provide more insight into each category.
# print(me_sal.Age.value_counts())

# ages = me_sal.sort_values('Age')
age_count = me_sal['Age']

# age_count = age_count.sort_values(ascending=True)
print(age_count)
print(age_count.value_counts().sort_values(ascending=True))
# How many bins should be in the histogram should be equal to the number of unique ages recorded
print(len(me_sal.Age.unique()))
# Plotting the age of mechanical engineers that responded in a histogram.
style.use('ggplot')
plt.hist(me_sal['Age'],
         bins=len(me_sal.Age.unique()))
plt.title('Age of Mechanical Engineers')
plt.xlabel('Age', )
plt.xticks(np.linspace(20, 75, 12))
plt.ylabel('Count')
plt.show()

# A cumulative distribution plot would also be nice:
plt.hist(me_sal['Age'],
         bins=len(me_sal.Age.unique()),
         cumulative=True)
plt.title('Mechanical Engineer Age Cumulative Distribution' )
plt.xlabel('Age in Years')
plt.xticks(np.linspace(20, 75, 12))
plt.ylabel('Count')
plt.show()

# Exploring Gender of mechanical engineers, a barchart would help compare how many of each there are:

me_gender = me_sal.Gender.unique()
me_genderCt = me_sal.Gender.value_counts()
print(me_genderCt)

plt.bar(me_gender,me_genderCt)
plt.title('Gender of Mechanical Engineers')
plt.ylabel('Count')
plt.yticks(numpy.arange(0, 3500, 500))
plt.show()
