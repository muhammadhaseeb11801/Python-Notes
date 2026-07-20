## Import Required Library

import matplotlib.pyplot as plt

## Create Data

x = [1,2,3,4,5]
y = [40,20,35,45,32]

### Explanation

# **x** contains the values for the X-axis.

# **y** contains the values for the Y-axis.

# Each X value is matched with a corresponding Y value.

# Example:
# (1,40)
# (2,20)
# (3,35)
# (4,45)
# (5,32)


## Plot Data

plt.plot(x, y, linestyle=':')

### Explanation

# **plt.plot()** is used to create a line graph.

# **x** values are displayed on the X-axis.

# **y** values are displayed on the Y-axis.

# **linestyle=':'** creates a dotted line.

# A dotted line is made up of small dots
# instead of a continuous line.

# The dotted line connects all data points
# while showing a dot pattern.


## Add Graph Title

plt.title("Dotted Line")

### Explanation

# **plt.title()** adds a title to the graph.

# The title of this graph is "Dotted Line".

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

# - Create X-axis and Y-axis data.

# - Plot a line graph using a dotted line.

# - Add a graph title.

# - Display the graph on the screen.

# - Show the relationship between X and Y values.