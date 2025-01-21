# Author: Brad Portouw
# Date: 1/19/25

# Learning matplotlib from scratch from: https://www.youtube.com/watch?v=OZOOLe2imFo

import numpy as np
# importing matplotlib, specifically the .pyplot module will have most necessary functionality. Using the plt alias
import matplotlib.pyplot as plt
from matplotlib import style

# #Making random data points. Random function gives valeus between 0 and 1, .random(50) gives 50 values
# x_data = np.random.random(50) * 100
# y_data = np.random.random(50) * 100
# # Plotting on a scatter plot. c = color marker= point types, s = point size
 plt.scatter(x_data, y_data, c="red", marker="*", s=150)
# # in order to show the plot after creating it use plt.show
# plt.show()

# # For a line chart:
# years = [2006 + x for x in range(16)]
# weights = [80 ,83, 84, 85, 86, 82, 81, 79, 83, 80, 82, 82, 83, 81, 80, 79]
#
# plt.plot(years, weights, c="g", lw=3, linestyle="--")
# # or  a positional parameter like matlab has the same result:
# plt.plot(years, weights,'r--', lw=3)
# plt.show()

# # Bar Plots:
#
# # Programming languages used for programming languages in a bar plot
# x = ["C++", "C#", "Python", "Java", "Go"]
# y = [20, 50, 140, 1, 45]
#
# plt.bar(x,y, color='r', align="edge", width=0.5, edgecolor="green", lw= 6)
# plt.show()

# Histograms

# Random ages in a normal distribution .normal(mean, std, n)
# ages = np.random.normal(20, 1.5, 1000)
#
# # Plot a histogram of the ages
# # bins will specify the number of bins(resolution), or can specify the bins themselves
# plt.hist(ages,
#          bins=[ages.min(), 18, 21, ages.max()])
# plt.show()
# # Alternatively a cumlative histogram is possible by pasing the optional arg cumulative = True
# plt.hist(ages,
#          bins=20,
#          cumulative=True)
# plt.show()

# Pie charts
#
# # Favorite programming languages
# langs = ["Python", "C++", "Java", "C#", "Go"]
# votes = [50, 24, 14, 6, 17]
# explodes = [0.3, 0, 0, 0, 0]
#
# plt.pie(votes, labels=langs, explode=explodes,
#         autopct="%.2f%%", pctdistance=0.8, startangle=90)      # Floating point number up to 2 decimal points for the percentage of each slice
# plt.show()

# Boxplots

# # random normal distribution of heights in cm
# heights = np.random.normal(172, 8, 300)
# # Shown in a boxplot
# plt.boxplot(heights)
# plt.show()
#
# # can manually make each quadrant of a box plot
# first = np.linspace(0, 10,25)
# second = np.linspace(10, 200, 25)
# third = np.linspace(200, 210, 25)
# fourth = np.linspace(210, 230, 25)
#
# # Can concatenate the numpy arrays together
# data = np.concatenate([first, second, third, fourth])
#
# plt.boxplot(data)
# plt.show()


# Plot Customization:

# Sample data:
# years = [2014 + x for x in range(8)]
# income = [55, 56, 62, 61, 72, 72, 73, 75]
# income_ticks = list(range(50, 81, 2))
# plt.plot(years, income)
# plt.title("Income of John (in USD)", fontsize=30)
# plt.xlabel("Year")
# plt.ylabel("Yearly Income in USD")
# # Want to add k to denote that income is in the thousands. Utilize a formatted string with a comprehension
# plt.yticks(income_ticks, [f"${x}k" for x in income_ticks])
#
# plt.show()

# # Multiple lines of data on the same plot
# stock_a = [100, 102, 99, 101, 101, 100, 102]
# stock_b = [90, 95, 102, 104, 105, 103, 109]
# stock_c = [110, 115, 100, 105, 100, 98, 95]
#
# # Plot all 3 stocks using 3 different functions, and label within using label="name"
# plt.plot(stock_a, label="Company 1")
# plt.plot(stock_b, label="Company 2")
# plt.plot(stock_c, label="Company 3")
#
# # Legend isn't on by default, needs to be called. loc is optional argument for legend location
# plt.legend(loc="upper right")
#
# plt.show()
#
# # WIth a pie chart:
# votes = [10, 2, 5, 16, 22]
# people = ["A", "B", "C", "D", "E"]
# # Style will change the colors and style of data points on a plot. Look online at matplotlib to find different styles to use
# # Note: needs to be called before making the plot object
# style.use("dark_background")
#
# plt.pie(votes, labels=None)
# # Legend labels can be called within the legend function
# plt.legend(labels=people)
#
#
# plt.show()


# # Multiple plots:
#
# x1, y1 = np.random.random(100), np.random.random(100)
# x2, y2 = np.arange(100), np.random.random(100)
#
# plt.figure(1)
# plt.scatter(x1, y1)
#
# # Denoting figure 2 to show that two figures are sharing the same window
# plt.figure(2)
# plt.plot(x2, y2)
#
# # This will print two figures in separate windows
# plt.show()

x = np.arange(100)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Sine Wave")

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title("Cosine Wave")

axs[1, 0].plot(x, np.random.random(100))
axs[1, 0].set_title("Random Function")

axs[1, 1].plot(x, np.log(x))
axs[1, 1].set_title("Log Function")
# Can label each individual plot
axs[1, 1].set_xlabel("Test")

# If a title is needed for the group of plots use a super title
fig.suptitle("Four Plots")

plt.show()

# Can save plots with the .savefig("filename.png", dpi=resolution) function
plt.savefig("fourplots.png", dpi=300,
            transparent =False, bbox_inches="tight")