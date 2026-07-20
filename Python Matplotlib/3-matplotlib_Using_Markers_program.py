## Import Required Library
import matplotlib.pyplot as plt

## Create Data

days = [1, 2, 3, 4, 5, 6, 7]
temperature = [32, 34, 33, 35, 36, 34, 31]

### Explanation

# **days** contains the day numbers.

# **temperature** contains the temperature values
# recorded for each day.

# Each day is matched with its corresponding temperature.

# Example:
# Day 1 = 32
# Day 2 = 34
# Day 3 = 33
# Day 4 = 35
# Day 5 = 36
# Day 6 = 34
# Day 7 = 31


## Plot Data

plt.plot(days, temperature, marker='o')

### Explanation

# **plt.plot()** is used to create a line graph.

# **days** are displayed on the X-axis.

# **temperature** values are displayed on the Y-axis.

# **marker='o'** adds circular markers at each data point.

# The line connects all temperature values
# to show the trend over 7 days.


## Add Graph Title

plt.title("Temperature")

### Explanation

# **plt.title()** adds a title to the graph.

# The title of this graph is "Temperature".

# It helps identify what the graph represents.


## Add X-Axis Label

plt.xlabel("Days")

### Explanation

# **plt.xlabel()** adds a label to the X-axis.

# The label "Days" indicates that the X-axis
# contains day numbers.


## Add Y-Axis Label

plt.ylabel("Temperature")

### Explanation

# **plt.ylabel()** adds a label to the Y-axis.

# The label "Temperature" indicates that the Y-axis
# contains temperature values.


## Display Graph

plt.show()

### Explanation

# **plt.show()** displays the graph window.

# It renders the graph and makes it visible
# to the user.


## Summary

# This program performs the following steps:

# - Import the Matplotlib library.

# - Create day and temperature data.

# - Plot a line graph with circular markers.

# - Add a graph title.

# - Add labels for the X-axis and Y-axis.

# - Display the graph on the screen.

# - Show the temperature trend over 7 days.

