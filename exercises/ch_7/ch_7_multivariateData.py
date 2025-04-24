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
from scipy.stats.stats import pearsonr
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
plt.legend(labels=['Men', 'Women'], fontsize=15)
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

#a scatterplot showing the age(x-axis) vs Salary may show trends between the two, where we would expect older engineers to be paid more.
# Having 1 plot containing both the data for men and women superimposed on one another is difficult to read, so two subplots seems to be a better option.

fig, ax = plt.subplots(1, 2, sharey=True)
ax[0].scatter(me_men['Age'], me_men['Salary'],
            c='xkcd:grey blue',
            s=5,
            alpha= 1)
ax[1].scatter(me_women['Age'], me_women['Salary'],
            c='xkcd:light orange',
            s=5,
            alpha= 1)
ax[0].set_title('Men', fontsize=12)
ax[0].set_ylim(0,500000)
ax[0].set_yticks(list(range(0,500000,100000)), [f"${x}k" for x in salary_ticks])
ax[0].set_xlim(20,80)
ax[1].set_xlim(20,80)
ax[1].set_title('Women', fontsize=15)
fig.suptitle('Age versus Salary Mechanical Engineers', fontsize=20)
plt.show()

#This plot will have different readability depening upon the size of the window it is opened in.
# A large number of datapoints makes it difficult to read if the points are too large due to overlap.
# In a small preview window, the marker points are small
# However, in a large window the marker points may need to be larger (s goes up) as they don't scale with the window itself.

# A pearson coefficent here could show a correlation between age and salary.
cor_eng, p = pearsonr(me_sal['Age'], me_sal['Salary'])
cor_eng
print(f'The Pearsons correlation between age and salary for mechanical engineers is %.3f' %cor_eng)

# Checking for each gender now:
cor_men, p_men = pearsonr(me_men['Age'], me_men['Salary'])
print(f'The Pearsons correlation for age vs salary for men is %.3f' %cor_men )
cor_women, p_women = pearsonr(me_women['Age'], me_women['Salary'])
print(f'Likewise the Pearsons correlation for women is %.3f' %cor_women)

# It would appear that the pearson correlation between age and salary has a slight positive value, and doesn't have a signifigant difference between men and women.
# Looking at the scatterplot above, it appears that young engineers have entry level salaries that are grouped together, but as time goes on the salaries gain variance.

# a cumulative distribuiton comparing salary may discern what salary the majority of engineers should expect in their careers.
x_men = np.sort(me_men['Salary'])
x_fem = np.sort(me_women['Salary'])

y_men = np.arange(len(me_men))/ float(len(me_men))
y_fem = np.arange(len(me_women))/ float(len(me_women))

plt.plot(x_men,y_men, c='xkcd:grey blue')
plt.plot(x_fem,y_fem, c='xkcd:light orange')
# After a preliminary look at  the graph, the plot is affected by a couple of outliers with a few people making around 1 million dollars. In this case they will be removed from this plot
plt.title('Cumulative Distribution of Engineering Salaries by Gender' )
plt.xlabel('Engineering Salary')
plt.ylabel('Cumulative Fraction')
plt.xlim(0,500000)
plt.xticks(list(range(0,500000,100000)), [f"${x}k" for x in salary_ticks])
plt.yticks(np.arange(0,1.1,0.1))
plt.legend(['Men', 'Women'])
plt.show()

# Looking at this plot, it appears that about 99% of engineers make less than 250k, so it may be beneficial to zoom in to notice differences more easily.
sal_ticks2 = list(range(0,350,50))
plt.plot(x_men,y_men, c='xkcd:grey blue')
plt.plot(x_fem,y_fem, c='xkcd:light orange')
# After a preliminary look at  the graph, the plot is affected by a couple of outliers with a few people making around 1 million dollars. In this case they will be removed from this plot
plt.title('Cumulative Distribution of Engineering Salaries by Gender' )
plt.xlabel('Engineering Salary')
plt.ylabel('Cumulative Fraction')
plt.xlim(0,300000)
plt.xticks(list(range(0,350000,50000)), [f"${x}k" for x in sal_ticks2])
plt.yticks(np.arange(0,1.1,0.1))
plt.legend(['Men', 'Women'])
plt.show()

# This plot is rather unfortunate, which suggests that women are statistically less likely to make the same wage as their male counterparts
# The quantiles were shown in the boxplot earlier, but calculating them could be useful

# me_women.Salary.describe()
# me_men.Salary.describe()
quantile_f = me_women.Salary.quantile([0, 0.25, 0.5, 0.75, 1.0])
quantile_m = me_men.Salary.quantile([0, 0.25, 0.5, 0.75, 1.0])
print(f'The median salary for women is $%.0f' %quantile_f.iloc[2])
print(f'The median salary for men is $%.0f' %quantile_m.iloc[2])
print(f'The difference in the medians is: $%.0f' %(quantile_m.iloc[2]-quantile_f.iloc[2]))
print(f'Maximum salary for women is $%.0f' %quantile_f.iloc[4])
print(f'Maximum salary for men is $%.0f' %quantile_m.iloc[4])
print(f'The difference in the maximum is $%.0f' %(quantile_m.iloc[-1]-quantile_f.iloc[-1]))

'''
There are a large number of potential factors in play for overall pay of employees, but the largest one might be the 
company and occupation of each engineer. If a company and type  of engineering could be found, it would be helpful. Also
it seems that the pay for many engineers plateaus at around 100k. It could be helpful to know which engineers have 
management positions. The school each engineer graduated at may play a small role in salary, as new hires out of 
prestigous schools may be offered more to start. Also where the engineer lives would play a role in pay considering cost 
of living, and potential benefits. 
'''