"""
IN this exercise there is a focus on parsing strings for certain phrases and data. For this a CSV containing tweets from
Colorado senators is used to descern information
"""

# Importing packages

import math
import collections
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import datetime
from matplotlib import style
# importing regex module to parse strings
import re
pd.options.mode.chained_assignment = None
# Importing senators.csv from the data directory.

# Error with csv import without encoding = 'latin-1'
sen_tweets = pd.read_csv('../../data/senators.csv', encoding='latin-1')
# print(sen_tweets)
# print(sen_tweets.info())
# After importing the csv of senator tweets from 2011 to 2017, the intention is to analyze tweets made by colorado senators.
# luckily there is a column for the state each senator is from.

# Boolean expression involving the columns can sort out the colorado senators:

co_tweets = sen_tweets.loc[sen_tweets.state == "CO"]

# .query method also works, using a boolean as a string.

# co_tweets = sen_tweets.query('state == "CO"')


print(co_tweets.info())

# It appears that there are a total of around 5436 tweets from Colorado senators in the csv

# finding all the hashtags used by Colorado senators using a pattern.

# the regex syntax: r"#(\d|\w+)" will find a section that starts with a #, and include all following digits and letters.

# Making a function to find hashtags in a given string:
def find_hash(text):
    return re.findall('#(\d|\w+)', text)


# co_tweets['hashtags'] = co_tweets['text'].apply(find_hash)
co_tweets['hashtags'] = co_tweets['text'].apply(find_hash)

print(co_tweets.head())

print(co_tweets)

# Some tweets have multiple hashtags, which means lists are nested within the hashtag column, caususing some errors.
# The solution seems to be to convert the nested sublists into tuples.

co_tweets['hashtags'] = co_tweets['hashtags'].apply(tuple)

print(co_tweets.head())
# Colorado senators made 1997 tweets with hashtags in them.
print(co_tweets.hashtags.value_counts())
print(co_tweets.info())

# In the past, there were many Colorado wildfires. Using co_tweets, an examination of senators' tweet activity regarding wildfires can be seen.
# Using regex, the number of hashtags that contain "fire or "wildfire"

# Searching through the hashtag column for any instances of fire or wildfire. flags=re.I will recognize capitals or lowercase.

