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
age_count = age_count.sort_values(ascending=True)
print(age_count)
print(age_count.value_counts().sort_values(ascending=True))



# plt.style.use('ggplot')
# plt.bar(me_sal, color='b')
# plt.title('Age of Mechanical Engineers National Science Foundation 2017')
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.show()
