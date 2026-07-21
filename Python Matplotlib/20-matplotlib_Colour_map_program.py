## Import Required Library

import matplotlib.pyplot as plt

## Create Data

study_hours = [2, 5, 4, 3, 6]

marks = [78, 92, 85, 70, 88]

colors = [10, 20, 30, 40, 50]

### Explanation

# **study_hours** contains the number of hours
# students studied.

# **marks** contains the marks obtained by students.

# **colors** contains values used to generate
# different colors for the scatter points.

# Each study hour value is matched with a
# corresponding mark and color value.


## Create Scatter Plot

plt.scatter(
    study_hours,
    marks,
    c=colors,
    cmap='viridis',
    s=80,
    marker='D'
)

### Explanation

# **plt.scatter()** is used to create a scatter plot.

# **study_hours** are displayed on the X-axis.

# **marks** are displayed on the Y-axis.

# **c=colors** assigns color values to points.

# **cmap='viridis'** applies the Viridis color map.

# The color changes automatically according
# to the values in the colors list.

# **s=80** sets the size of each point.

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


## Save Graph as Image

plt.savefig("scatter_plot.png")

### Explanation

# **plt.savefig()** saves the graph as
# an image file.

# The graph will be saved with the name
# **scatter_plot.png**.

# The image is stored in the current
# working folder.


## Display Graph

plt.show()

### Explanation

# **plt.show()** displays the graph window.

# It renders the graph and makes it visible
# to the user.


## Summary

# This program performs the following steps:

# - Import the Matplotlib library.

# - Create study hours, marks, and color data.

# - Create a scatter plot.

# - Apply the Viridis color map.

# - Use diamond (D) markers.

# - Set the marker size to 80.

# - Add a color scale bar.

# - Add graph title and axis labels.

# - Enable grid lines.

# - Save the graph as scatter_plot.png.

# - Display the graph on the screen.
