## Import Required Library

import matplotlib.pyplot as plt

## Create Data

study_hours = [2, 5, 4, 3, 6]

marks = [78, 92, 85, 70, 88]

colors = [10, 20, 30, 40, 50]

sizes = [100, 200, 300, 400, 500]

### Explanation

# **study_hours** contains the number of hours
# students studied.

# **marks** contains the marks obtained by students.

# **colors** contains values used to generate
# different colors for the points.

# **sizes** contains values that control the
# size of each scatter point.

# Each study hour value is matched with a
# corresponding mark, color value, and size value.


## Create Scatter Plot

plt.scatter(
    study_hours,
    marks,
    c=colors,
    cmap='viridis',
    s=sizes,
    marker='D'
)

### Explanation

# **plt.scatter()** is used to create a scatter plot.

# **study_hours** are displayed on the X-axis.

# **marks** are displayed on the Y-axis.

# **c=colors** assigns color values to the points.

# **cmap='viridis'** applies the Viridis color map.

# **s=sizes** assigns different sizes to each point.

# Larger values create larger points.

# **marker='D'** displays diamond-shaped markers.

# Each point represents one student's
# study hours and marks.


## Add Color Bar

plt.colorbar(label="Color Scale")

### Explanation

# **plt.colorbar()** adds a color scale beside
# the graph.

# The color bar shows how colors correspond
# to the values in the colors list.

# **label="Color Scale"** adds a title to the
# color bar.


## Add Graph Title

plt.title("Study Hours vs Marks")

### Explanation

# **plt.title()** adds a title to the graph.

# The title of this graph is
# "Study Hours vs Marks".

# It helps identify what the graph represents.


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
# Y-axis contains students' marks.


## Add Grid Lines

plt.grid(True)

### Explanation

# **plt.grid(True)** enables grid lines
# on both axes.

# Grid lines make the graph easier to read
# and compare values.


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

# - Create study hours, marks, color, and size data.

# - Create a scatter plot.

# - Apply the Viridis color map.

# - Use diamond (D) markers.

# - Assign different colors to points.

# - Assign different sizes to points.

# - Add a color scale bar.

# - Add graph title and axis labels.

# - Enable grid lines.

# - Display the graph on the screen.
