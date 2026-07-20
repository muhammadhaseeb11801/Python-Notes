## Import Required Library

import matplotlib.pyplot as plt

## Create Data

days = [1,2,3,4,5,6,7]
temperature = [39,38,30,34,39,30,35]

### Explanation

# **days** contains the day numbers.

# **temperature** contains the temperature values
# recorded for each day.

# Each day is matched with its corresponding temperature.

# Example:
# Day 1 = 39
# Day 2 = 38
# Day 3 = 30
# Day 4 = 34
# Day 5 = 39
# Day 6 = 30
# Day 7 = 33


## Plot Data

plt.plot(
    days,
    temperature,
    color='red',
    linestyle='--',
    linewidth=3
)

### Explanation

# **plt.plot()** is used to create a line graph.

# **days** are displayed on the X-axis.

# **temperature** values are displayed on the Y-axis.

# **color='red'** changes the line color to red.

# **linestyle='--'** creates a dashed line.

# **linewidth=3** makes the line thicker.

# The graph shows the temperature trend over 7 days
# using a thick red dashed line.


## Add Graph Title

plt.title("Customized Line")

### Explanation

# **plt.title()** adds a title to the graph.

# The title of this graph is "Customized Line".

# It helps identify what the graph represents.


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

# - Plot a customized line graph.

# - Set the line color to red.

# - Use a dashed line style (--).

# - Set the line width to 3.

# - Add a graph title.

# - Display the graph on the screen.
