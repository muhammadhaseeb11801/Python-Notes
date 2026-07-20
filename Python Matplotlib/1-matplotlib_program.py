## Import Required Library

import matplotlib.pyplot as plt

### Explanation

# **Matplotlib** is a Python library used for creating charts,
# graphs, and data visualizations.

# We use **plt** as the short name (alias) for pyplot.


## Create Data

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

### Explanation

# **x** contains the values for the X-axis.

# **y** contains the values for the Y-axis.

# Each X value is paired with a corresponding Y value.


## Plot Data

plt.plot(x, y, 'o', ms=20, mec='pink', mfc='red')

### Explanation

# **plt.plot()** is used to plot data on a graph.

# **x** and **y** are the data values being plotted.

# **'o'** creates circular markers.

# **ms=20** sets the marker size to 20.

# **mec='pink'** sets the marker edge color to pink.

# **mfc='red'** sets the marker fill color to red.


## Display Graph

plt.show()

### Explanation

# **plt.show()** displays the graph window.

# It renders the graph and makes it visible to the user.


## Summary

# This program imports Matplotlib.

# It creates X-axis and Y-axis data.

# It plots the data using red circular markers
# with pink borders.

# Finally, it displays the graph on the screen.

