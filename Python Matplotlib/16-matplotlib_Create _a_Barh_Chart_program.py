## Import Required Library

import matplotlib.pyplot as plt

## Create Data

students = ["Ali", "Ahmed", "Sara", "Ayesha", "Usman"]

marks = [78, 92, 85, 70, 88]

### Explanation

# **students** contains the names of the students.

# **marks** contains the marks obtained by each student.

# Each student is matched with a corresponding mark.

# Example:
# Ali = 78
# Ahmed = 92
# Sara = 85
# Ayesha = 70
# Usman = 88


## Create Horizontal Bar Chart

plt.barh(students, marks, height=0.1)

### Explanation

# **plt.barh()** is used to create a horizontal bar chart.

# **students** are displayed on the Y-axis.

# **marks** are displayed on the X-axis.

# Each horizontal bar represents the marks
# of one student.

# **height=0.1** sets the thickness of each bar.

# Smaller values create thinner bars,
# while larger values create thicker bars.


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

# In this graph, the X-axis contains the marks values.

# A better label would be **"Marks"** because
# marks are displayed horizontally.


## Add Y-Axis Label

plt.ylabel("Marks")

### Explanation

# **plt.ylabel()** adds a label to the Y-axis.

# In this graph, the Y-axis contains student names.

# A better label would be **"Students"** because
# student names are displayed vertically.


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

# - Create student and marks data.

# - Create a horizontal bar chart.

# - Set the bar height to 0.1.

# - Add a graph title.

# - Add labels for the X-axis and Y-axis.

# - Display the graph on the screen.

# - Compare students' marks using horizontal bars.
