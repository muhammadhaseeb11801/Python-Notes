## Import Required Library

import matplotlib.pyplot as plt

## Create Data

study_hours = [2, 5, 4, 3, 6]

marks = [78, 92, 85, 70, 88]

### Explanation

# **study_hours** contains the number of hours
# students studied.

# **marks** contains the marks obtained by students.

# Each study hour value is matched with a
# corresponding marks value.

# Example:
# 2 Hours = 78 Marks
# 5 Hours = 92 Marks
# 4 Hours = 85 Marks
# 3 Hours = 70 Marks
# 6 Hours = 88 Marks


## Create Scatter Plot

plt.scatter(
    study_hours,
    marks,
    s=100,
    marker="D",
    color="red"
)

### Explanation

# **plt.scatter()** is used to create a scatter plot.

# **study_hours** are displayed on the X-axis.

# **marks** are displayed on the Y-axis.

# **s=100** sets the size of the points.

# **marker="D"** displays diamond-shaped markers.

# **color="red"** changes the color of all points to red.

# Each point represents one student's
# study hours and marks.


## Add Graph Title

plt.title("Study Hours vs Marks", loc="left")

### Explanation

# **plt.title()** adds a title to the graph.

# The title of this graph is
# "Study Hours vs Marks".

# **loc="left"** places the title on the
# left side of the graph.


## Add X-Axis Label

plt.xlabel("Study Hours")

### Explanation

# **plt.xlabel()** adds a label to the X-axis.

# The label "Study Hours" indicates that
# the X-axis contains study time values.


## Add Y-Axis Label

plt.ylabel("Marks")

### Explanation

# **plt.ylabel()** adds a label to the Y-axis.

# The label "Marks" indicates that the
# Y-axis contains marks values.


## Add Grid Lines

plt.grid(True)

### Explanation

# **plt.grid(True)** enables grid lines
# on both axes.

# Grid lines make the graph easier to read
# and compare values.


## Save Graph as Image

plt.savefig("scatter_plot.png")

### Explanation

# **plt.savefig()** saves the graph as an image file.

# The graph will be saved with the name
# **scatter_plot.png**.

# The image is stored in the current
# working folder.

# This allows the graph to be used later
# without recreating it.


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

# - Create study hours and marks data.

# - Create a scatter plot.

# - Set the marker size to 100.

# - Use diamond (D) markers.

# - Change marker color to red.

# - Add a title aligned to the left.

# - Add X-axis and Y-axis labels.

# - Enable grid lines.

# - Save the graph as scatter_plot.png.

# - Display the graph on the screen.
