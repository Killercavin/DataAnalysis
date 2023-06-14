# DataAnalysis

## 1. Introduction

This is a repository for data analysis. It contains some data analysis projects and some data analysis & visualization tools.
This repository focuses on the use of python for data analysis and visualization tools.
I will use python packages like numpy, pandas, matplotlib, seaborn, plotly, etc. to do data analysis and visualization.

## 2. Projects

### 2.1. Using Matplotlib to Visualize and Analyze Data

#### 2.1.1. Introduction and Installation of Matplotlib

Matplotlib is a python library used to create 2D graphs and plots by using python scripts. It has a module named pyplot which makes things easy for plotting by providing feature to control line styles, font properties, formatting axes etc. It is a cross-platform library for making 2D plots from data in arrays. It can be used in python scripts, shell, web application servers and other graphical user interface toolkits.

To install matplotlib, you can use pip install matplotlib when working from the terminal or conda install matplotlib when using Anaconda editor.

```pip install matplotlib```

The above command will install matplotlib in your system. You can also use the following command to check if matplotlib is installed or not.

```python -c "import matplotlib; matplotlib.test()"```
If matplotlib is installed, then the above command will not throw any error. If matplotlib is not installed, then the above command will throw an error.

#### 2.1.2. Basic Plotting with Matplotlib

Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+. There is also a procedural "pylab" interface based on a state machine (like OpenGL), designed to closely resemble that of MATLAB, though its use is discouraged. SciPy makes use of matplotlib.

Matplotlib was originally written by John D. Hunter, has an active development community, and is distributed under a BSD-style license. Michael Droettboom was nominated as matplotlib's lead developer shortly before John Hunter's death in August 2012, and further joined by Thomas Caswell.

Matplotlib is a plotting library. Matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

In matplotlib.pyplot various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes (please note that "axes" here and in most places in the documentation refers to the axes part of a figure and not the strict mathematical term for more than one axis).

The following steps are used to plot a simple graph of y = x^2:

1. Import the matplotlib.pyplot module as plt.
2. Use the linspace function from the numpy module to create an array of points from 0 to 2, with 20 points.
3. Plot x and y using the plot function.
4. Use the show function to display the plot.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 20)
y = x ** 2

plt.plot(x, y)
plt.show()
```

#### 2.1.3. Plotting with Keyword Strings

There are some instances where you have data in a format that lets you access particular variables with strings. For example, with numpy.recarray or pandas.DataFrame.

Matplotlib allows you provide such an object with the data keyword argument. If provided, then you may generate plots with the strings corresponding to these variables.

```python
import matplotlib.pyplot as plt
import numpy as np

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
```
