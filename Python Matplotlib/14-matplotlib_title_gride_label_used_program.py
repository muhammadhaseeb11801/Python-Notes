## Import Required Library

import matplotlib.pyplot as plt

## Create Data

values_1 = [10,20,30,40,50]
values_2 = [10,20,35,40,50]

### Explanation

# **values_1** contains the values for the X-axis.

# **values_2** contains the values for the Y-axis.

# Each value in values_1 is matched with a
# corresponding value in values_2.

# Example:
# (10,10)
# (20,20)
# (30,35)
# (40,40)
# (50,50)


## Plot Data

plt.plot(values_1, values_2, linestyle='-')

### Explanation

# **plt.plot()** is used to create a line graph.

# **values_1** are displayed on the X-axis.

# **values_2** are displayed on the Y-axis.

# **linestyle='-'** creates a solid line.

# The line connects all data points continuously.


## Add X-Axis Label

plt.xlabel(values_1)

### Explanation

# **plt.xlabel()** adds a label to the X-axis.

# Here, the entire list values_1 is used as
# the X-axis label.

# Output label:
# [10, 20, 30, 40, 50]

# Normally, a text label such as "Values 1"
# is used instead of a list.


## Add Y-Axis Label

plt.ylabel(values_2)

### Explanation

# **plt.ylabel()** adds a label to the Y-axis.

# Here, the entire list values_2 is used as
# the Y-axis label.

# Output label:
# [10, 20, 35, 40, 50]

# Normally, a text label such as "Values 2"
# is used instead of a list.


## Add Graph Title

plt.title("Graph", loc='left')

### Explanation

# **plt.title()** adds a title to the graph.

# "Graph" is the title text.

# **loc='left'** places the title on the
# left side of the graph.


## Add Grid

plt.grid(axis='y')

### Explanation

# **plt.grid()** adds grid lines to the graph.

# **axis='y'** displays grid lines only for
# the Y-axis.

# Horizontal grid lines help make values
# easier to read.


## Display Graph

plt.show()

### Explanation

# **plt.show()** displays the graph window.

# It renders the graph and makes it visible
# to the user.


## Summary

# This program performs the following steps:

# - Import the Matplotlib library.

# - Create X-axis and Y-axis data.

# - Plot a line graph using a solid line.

# - Add X-axis and Y-axis labels.

# - Add a title aligned to the left.

# - Display Y-axis grid lines.

# - Show the graph on the screen.
