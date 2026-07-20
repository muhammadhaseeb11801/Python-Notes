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
# corresponding mark.

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
    s=100
)

### Explanation

# **plt.scatter()** is used to create a scatter plot.

# **study_hours** are displayed on the X-axis.

# **marks** are displayed on the Y-axis.

# Each point represents one student's
# study hours and marks.

# **s=100** sets the size of the points.

# Larger values create bigger points,
# while smaller values create smaller points.


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

# - Set the point size to 100.

# - Add a graph title.

# - Add labels for the X-axis and Y-axis.

# - Display the graph on the screen.

# - Show the relationship between study hours and marks.

