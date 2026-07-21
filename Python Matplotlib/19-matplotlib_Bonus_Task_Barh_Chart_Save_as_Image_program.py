## Import Required Library

import matplotlib.pyplot as plt

## Create Data

students = ["Ali", "Ahmed", "Sara", "Ayesha", "Usman"]

marks = [78, 99, 80, 88, 98]

### Explanation

# **students** contains the names of the students.

# **marks** contains the marks obtained by each student.

# Each student is matched with a corresponding mark.

# Example:
# Ali = 78
# Ahmed = 99
# Sara = 80
# Ayesha = 88
# Usman = 98


## Create Horizontal Bar Chart

plt.barh(
    students,
    marks,
    height=0.5,
    color="green"
)

### Explanation

# **plt.barh()** is used to create a horizontal bar chart.

# **students** are displayed on the Y-axis.

# **marks** are displayed on the X-axis.

# **height=0.5** sets the thickness of each bar.

# **color="green"** changes the color of all bars to green.

# Each horizontal bar represents the marks
# of one student.


## Add Graph Title

plt.title("Student Marks")

### Explanation

# **plt.title()** adds a title to the graph.

# The title of this graph is "Student Marks".

# It helps identify what the graph represents.


## Add X-Axis Label

plt.xlabel("Students")

### Explanation

# **plt.xlabel()** adds a label to the X-axis.

# In this graph, marks are displayed on the X-axis.

# A better label would be **"Marks"**.


## Add Y-Axis Label

plt.ylabel("Marks")

### Explanation

# **plt.ylabel()** adds a label to the Y-axis.

# In this graph, student names are displayed
# on the Y-axis.

# A better label would be **"Students"**.


## Add Grid Lines

plt.grid(axis="x")

### Explanation

# **plt.grid()** adds grid lines to the graph.

# **axis="x"** displays grid lines only for
# the X-axis.

# Vertical grid lines make the chart easier
# to read and compare values.


## Save Graph as Image

plt.savefig("barh_chart.png")

### Explanation

# **plt.savefig()** saves the graph as an image file.

# The graph will be saved with the name
# **barh_chart.png**.

# The image is stored in the current working folder.

# This allows the graph to be used later
# without recreating it.


## Display Graph

plt.show()

### Explanation

# **plt.show()** displays the graph window.

# It renders the graph and makes it visible
# to the user.


## Summary

# This program performs the following steps:

# - Import the Matplotlib library.

# - Create student and marks data.

# - Create a green horizontal bar chart.

# - Set the bar height to 0.5.

# - Add a graph title.

# - Add labels for the X-axis and Y-axis.

# - Display X-axis grid lines.

# - Save the graph as barh_chart.png.

# - Display the graph on the screen.
