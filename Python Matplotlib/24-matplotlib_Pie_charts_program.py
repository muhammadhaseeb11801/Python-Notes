## Import Required Library

import matplotlib.pyplot as plt

## Create Data

x = (600, 60, 10, 1)

mylabels = ("Students", "Rooms", "Labs", "Office")

myexplode = (0.5, 0, 0, 0)

### Explanation

# **x** contains the values for each category.

# **mylabels** contains the names of the categories.

# **myexplode** controls how far a slice moves
# away from the center of the pie chart.

# The first slice (Students) will be separated
# from the pie chart because its explode value is 0.5.


## Create Pie Chart

plt.pie(
    x,
    labels=mylabels,
    explode=myexplode,
    shadow=True
)

### Explanation

# **plt.pie()** is used to create a pie chart.

# **x** provides the values for each slice.

# **labels=mylabels** displays category names
# on the chart.

# **explode=myexplode** separates selected slices
# from the center.

# **shadow=True** adds a shadow effect
# to the pie chart.

# Each slice represents a portion of the
# total college resources.


## Add Chart Title

plt.title("College Resources")

### Explanation

# **plt.title()** adds a title to the chart.

# The title of this chart is
# "College Resources".

# It helps identify what the chart represents.


## Add Legend

plt.legend(title="Categories")

### Explanation

# **plt.legend()** adds a legend box.

# **title="Categories"** adds a title
# to the legend.

# The legend helps identify each slice
# of the pie chart.


## Display Pie Chart

plt.show()

### Explanation

# **plt.show()** displays the pie chart window.

# It renders the chart and makes it visible
# to the user.

# Without this command, the chart may not appear.


## Summary

# This program performs the following steps:

# - Import the Matplotlib library.

# - Create data for the pie chart.

# - Create category labels.

# - Explode the first slice (Students).

# - Add a shadow effect.

# - Create a pie chart.

# - Add a chart title.

# - Add a legend with a title.

# - Display the pie chart on the screen.
