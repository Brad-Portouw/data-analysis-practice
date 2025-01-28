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

# Importing senators.csv from the data directory.

#
sen_tweets = pd.read_csv('../../data/senators.csv', encoding='latin-1')
print(sen_tweets)
print(sen_tweets.info())
# After importing the csv of senator tweets from 2011 to 2017, the intention is to analyze tweets made by colorado senators.
# luckily there is a column for the state each senator is from.

# Boolean expression involving the columns can sort out the colorado senators:

co_tweets = sen_tweets[sen_tweets.state == "CO"]

# .query method also works, using a boolean as a string.

co_tweets = sen_tweets.query('state == "CO"')


print(co_tweets.info())

# It appears that there are a total of around 5436 tweets from Colorado senators in the csv

# finding all the hashtags used by Colorado senators using a pattern.

# the regex syntax: r"#(\d|\w+)" will find a section that starts with a #, and include all following digits and letters.

# Making a function to find hashtags in a given string:
def find_hash(text):
    return re.findall('#(\d|\w+)', text)


# co_tweets['hashtags'] = co_tweets['text'].apply(lambda x: find_hash(x))
co_tweets['hashtags'] = co_tweets['text'].apply(find_hash)

print(co_tweets.head())

print(co_tweets)