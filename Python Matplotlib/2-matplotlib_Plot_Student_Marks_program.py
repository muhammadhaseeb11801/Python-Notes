## Import Required Library

import matplotlib.pyplot as plt

## Create Data

subjects = ["Math", "Physics", "Chemistry", "English", "Computer"]
marks = [85, 78, 92, 70, 88]

### Explanation

# **subjects** contains the names of the subjects.

# **marks** contains the marks obtained in each subject.

# Each subject is matched with its corresponding mark.

# Example:
# Math = 85
# Physics = 78
# Chemistry = 92
# English = 70
# Computer = 88


## Plot Data

plt.plot(subjects, marks)

### Explanation

# **plt.plot()** is used to create a line graph.

# **subjects** are displayed on the X-axis.

# **marks** are displayed on the Y-axis.

# The points are connected with lines to show
# the marks for each subject.


## Add Graph Title

plt.title("Student Marks")

### Explanation

# **plt.title()** adds a title to the graph.

# The title of this graph is "Student Marks".

# It helps users understand what the graph represents.


## Add X-Axis Label

plt.xlabel("Subjects")

### Explanation

# **plt.xlabel()** adds a label to the X-axis.

# The label "Subjects" indicates that the X-axis
# contains subject names.


## Add Y-Axis Label

plt.ylabel("Marks")

### Explanation

# **plt.ylabel()** adds a label to the Y-axis.

# The label "Marks" indicates that the Y-axis
# contains students' marks.


## Display Graph

plt.show()

### Explanation

# **plt.show()** displays the graph window.

# It renders the graph and makes it visible
# to the user.


## Summary

# This program performs the following steps:

# - Import the Matplotlib library.

# - Create subject and marks data.

# - Plot a line graph using the data.

# - Add a graph title.

# - Add labels for the X-axis and Y-axis.

# - Display the graph on the screen.

