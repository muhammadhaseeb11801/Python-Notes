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


## Create Bar Chart

plt.bar(
    students,
    marks,
    width=0.5,
    color="green"
)

### Explanation

# **plt.bar()** is used to create a vertical bar chart.

# **students** are displayed on the X-axis.

# **marks** are displayed on the Y-axis.

# **width=0.5** sets the width of each bar.

# **color="green"** changes the color of all bars to green.

# Each bar represents the marks of one student.


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

# The label "Students" indicates that the X-axis
# contains student names.


## Add Y-Axis Label

plt.ylabel("Marks")

### Explanation

# **plt.ylabel()** adds a label to the Y-axis.

# The label "Marks" indicates that the Y-axis
# contains students' marks.


## Add Grid Lines

plt.grid(axis="y")

### Explanation

# **plt.grid()** adds grid lines to the graph.

# **axis="y"** displays grid lines only for
# the Y-axis.

# Horizontal grid lines make the chart
# easier to read and compare values.


## Save Graph as Image

plt.savefig("bar_chart.png")

### Explanation

# **plt.savefig()** saves the graph as an image file.

# The graph will be saved with the name
# **bar_chart.png**.

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

# - Create a green vertical bar chart.

# - Set the bar width to 0.5.

# - Add a graph title.

# - Add labels for the X-axis and Y-axis.

# - Display Y-axis grid lines.

# - Save the graph as bar_chart.png.

# - Display the graph on the screen.
