## Import Required Library

import matplotlib.pyplot as plt

## Create Data

x = [1000, 60, 10, 1]

mylabels = ["Students", "Rooms", "Labs", "Office"]

myexplode = [0.3, 0, 0, 0]

mycolors = ["blue", "green", "orange", "red"]

### Explanation

# **x** contains the values for each category.

# **mylabels** contains the category names.

# **myexplode** controls how far a slice
# moves away from the center.

# **mycolors** assigns different colors
# to each slice.

# The first slice (Students) will be separated
# slightly from the pie chart.


## Create Figure

plt.figure(figsize=(7,7))

### Explanation

# **plt.figure()** creates a new figure window.

# **figsize=(7,7)** sets the width and height
# of the chart to 7 inches.

# This creates a square-shaped figure.


## Create Pie Chart

plt.pie(
    x,
    labels=mylabels,
    colors=mycolors,
    explode=myexplode,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

### Explanation

# **plt.pie()** is used to create a pie chart.

# **labels=mylabels** displays category names.

# **colors=mycolors** assigns colors to slices.

# **explode=myexplode** separates selected slices.

# **autopct="%1.1f%%"** displays percentages
# with one decimal place.

# **startangle=90** starts the first slice
# from 90 degrees.

# **shadow=True** adds a shadow effect.

# Each slice represents a percentage of
# the total resources.


## Add Chart Title

plt.title("College Resources")

### Explanation

# **plt.title()** adds a title to the chart.

# The title of this chart is
# "College Resources".

# It helps identify what the chart represents.


## Add Legend

plt.legend()

### Explanation

# **plt.legend()** adds a legend box.

# The legend displays the category names
# and their corresponding colors.

# It makes the chart easier to understand.


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

# - Assign colors to slices.

# - Explode the Students slice.

# - Display percentage values.

# - Start the chart at 90 degrees.

# - Add a shadow effect.

# - Add a title and legend.

# - Display the pie chart on the screen.
