---
Title: pyplot_tutorial
Author: Brad Portouw - from matplotlib website: https://matplotlib.org/stable/users/explain/quick_start.html#quick-start
Date: 1/18/25
---

# An intro to the pyplot interface. 

 ```python
# importing packages
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
```

## Matplotlib 
Matplotlib graphs data on figures, which will contain axes, an area where points can be specified in terms of coordinates.
The simplest way of creating a figure with axes is: pyplot.subplots -> Axes.plot (ax.plot) -> plt.show()

```python
x = list(range(0, 10)) 
y = list(range(-10, 0))
plt.plot(x,y)
```

## Components of a plot in matplotlib

### Figure
The figure keeps track of all child axes, a group of special artists(titles, figure legends, colorbars, etc), and nested subfigures

Typically a new figure can be created with the following functions:

    fig = plt.figure()                  # an empty figure with no Axes
    fig, ax = plt.subplots()            # a figure with a single Axes
    fig, axs = plt.subplots(2, 2)       # a figure with a 2x2 grid of Axes
    Finally a figure with one axes on the left, and two on the right:
    fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                                   ['left', 'right_bottom']])

subplots() and subplot_mosaic() are convenient functions because they create axis objects inside the figure, but axes can be added manually later on. 

### Axes 
An Axes is an Artist attached to a figure that contains a region for plotting data, an dusually includes two (or three) Axis objects (Axis and Axes are different) that provide ticks and tick labels to provide scales for the data in the Axes. Each Axes also has a title (set_title()) an x-label (set_xlabel()), and a y-label set via set_ylabel()

### Axis
These objects set the scale and limits of the plot using limits, ticks and ticklabels. The location of the ticks is determined by a Locator object and the ticklabel strings are formatted by a Formatter. The combo of Locator and Formatter objects gives fine control over tick locations and labels.

### Artist
Everything visible in a Figure is an Artist(Figure, Axes, and Axis objects). This includes Text, Line2D, collections, and Patch objects. When the figure is rendered, all the artist objects are drawn to the canvas. Most Artists are tied to an Axis, and these Artists cannot be shared by multiple Axes or moved from one to another. 

##  Types of inputs to plotting functions
Plotting functions expect numpy.array or numpy.ma.masked_array as input, or objects that can be passed to numpy.asarray. Classes that are similar to arrays ('array-like') such as pandas data objects and numpy.matrix may not work as intended. Common convention is to convert these to numpy.array objects prior to plotting. For example to convert a numpy.matrix

```python
b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)
```

Most Methods will also parse a string-indexable object like a dict, a structured numpy array, or a pandas.DataFrame. Matplotlib allows you to provide the data keyword argument and generate plots passing the strings corresponding to the x and y variables. 
    