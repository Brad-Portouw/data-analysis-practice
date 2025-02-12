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
#importing seaborn for nice boxplots
import seaborn as sns

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
plt.xlabel('Age')
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

# Perhaps an age histogram that compares gender would also be interesting:

# Separating both men and women responses:
me_men = me_sal.loc[me_sal['Gender'] == 'M']
me_women = me_sal.loc[me_sal['Gender'] == 'F']

# A unique challenge here, there are some ages that have no women in that bin, therefore stacking the bins with two plots has the bins offset from one another.

print(me_women)
# Simple solution, just make the range of the bins available, and make the steps be by 1 for intergers.
plt.hist(me_men['Age'],
         bins=range(0,100,1),
         color='xkcd:grey blue',
         rwidth=0.9,
         stacked=True,
         align='left')
plt.hist(me_women['Age'],
         bins=range(0,100,1),
         color='xkcd:light orange',
         rwidth=0.9,
         stacked=True,
         align='left')
plt.title('Age of Mechanical Engineers by Gender', fontsize=20)
plt.legend(labels=['Men', 'Women'], fontsize= 15)
plt.xlabel('Age', fontsize=15)
plt.ylabel('Number of engineers', fontsize=15)
plt.xlim(20,80)
plt.xticks(list(range(20,85,5)))
plt.show()

# hard to tell if there is a correlation between age and gender, another plot may be required, but the information is interesting regardless.

# Comparing salary versus gender instead:
salary_ticks= list(range(0,500,100))
plt.hist(me_men['Salary'],
         bins=np.linspace(0, 500000, 75),
         color='xkcd:grey blue',
         stacked=True,
         align='left')
plt.hist(me_women['Salary'],
         bins=np.linspace(0,500000,75),
         color='xkcd:light orange',
         stacked=True,
         align='left')
plt.title('Salary of Mechanical Engineers', fontsize=20)
plt.xlabel('Salary')
plt.xticks(list(range(0,500000,100000)), [f"${x}k" for x in salary_ticks])
plt.show()

#Again hard to tell the difference at a glance with the population differences.

# A side by side boxplot will give information regarding quartiles and the median, possibly giving insights.
# seaborn makes a asethicically nice box plot, which can convey infomation easliy.
# plt.style.use('bmh')
sns.boxplot(data=me_sal, x='Salary', y= 'Gender',
            palette=[sns.xkcd_rgb['grey blue'], sns.xkcd_rgb['light orange']])
plt.title('Engineer Salary Quartiles', fontsize=20)
plt.xlabel('Salary', fontsize=15)
plt.xticks(list(range(0,500000,100000)), [f"${x}k" for x in salary_ticks], fontsize=15)
plt.xlim(0,500000)
plt.legend(['Male', 'Female'], fontsize=15)

plt.show()
# while not perfect, its a start. Would like to make the fontsize larger for the y axis.

# Boxplot for age of mechanical engineers with gender in mind:
sns.boxplot(data=me_sal, x='Age', y='Gender',
            palette=[sns.xkcd_rgb['grey blue'], sns.xkcd_rgb['light orange']])
plt.title('Engineer Age Quartiles', fontsize=20)
plt.xlabel('Age', fontsize=15)
plt.legend(['Male','Female'],fontsize=15)
plt.show()

# looking at both boxplots, they would imply that female engineers as a median have slighly lower salaries than their male counterparts.
# It also appears that a larger porportion of women engineers are younger.
