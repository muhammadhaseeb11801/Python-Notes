## Import Required Library

import matplotlib.pyplot as plt

## Create Data

days = [1,2,3,4,5,6,7]
temperature = [40,37,36,30,39,35,33]

### Explanation

# **days** contains the day numbers.

# **temperature** contains the temperature values
# recorded for each day.

# Each day is matched with its corresponding temperature.

# Example:
# Day 1 = 40
# Day 2 = 37
# Day 3 = 36
# Day 4 = 30
# Day 5 = 39
# Day 6 = 35
# Day 7 = 33


## Plot Data

plt.plot(days, temperature, marker='s')

### Explanation

# **plt.plot()** is used to create a line graph.

# **days** are displayed on the X-axis.

# **temperature** values are displayed on the Y-axis.

# **marker='s'** adds square-shaped markers
# at each data point.

# The line connects all temperature values
# to show the temperature trend over 7 days.


## Display Graph

plt.show()

### Explanation

# **plt.show()** displays the graph window.

# It renders the graph and makes it visible
# to the user.

# Without this command, the graph may not appear.


## Summary

# This program performs the following steps:

# - Import the Matplotlib library.

# - Create day and temperature data.

# - Plot a line graph with square (s) markers.

# - Display the graph on the screen.

# - Show the temperature trend over 7 days.
