## Import Required Library

import matplotlib.pyplot as plt

## Create Data

students = ["Ali", "Ahmed", "Sara", "Ayesha", "Usman"]

marks = [78, 92, 85, 70, 88]

study_hours = [2, 5, 4, 3, 6]

### Explanation

# **students** contains the names of students.

# **marks** contains the marks obtained by students.

# **study_hours** contains the number of hours
# each student studied.

# The data will be used to create two graphs.


## Create Figure

plt.figure(figsize=(12,5))

### Explanation

# **plt.figure()** creates a new figure window.

# **figsize=(12,5)** sets the figure width
# to 12 inches and height to 5 inches.

# This provides enough space for multiple graphs.


## Create First Subplot

plt.subplot(1,2,1)

### Explanation

# **plt.subplot(1,2,1)** creates the first graph area.

# 1 = Total rows.

# 2 = Total columns.

# 1 = Position of the first graph.

# This subplot will contain the bar chart.


## Create Bar Chart

plt.bar(
    students,
    marks,
    width=0.5,
    color="skyblue"
)

### Explanation

# **plt.bar()** is used to create a vertical bar chart.

# **students** are displayed on the X-axis.

# **marks** are displayed on the Y-axis.

# **width=0.5** sets the width of each bar.

# **color="skyblue"** changes the bar color
# to sky blue.

# Each bar represents one student's marks.


## Add Bar Chart Title

plt.title("Student Marks")

### Explanation

# **plt.title()** adds the title
# "Student Marks" to the bar chart.


## Add X-Axis Label

plt.xlabel("Students")

### Explanation

# **plt.xlabel()** adds the label
# "Students" to the X-axis.


## Add Y-Axis Label

plt.ylabel("Marks")

### Explanation

# **plt.ylabel()** adds the label
# "Marks" to the Y-axis.


## Add Grid Lines

plt.grid(axis="y")

### Explanation

# **plt.grid(axis="y")** displays
# horizontal grid lines only.

# This makes the marks easier to compare.


## Create Second Subplot

plt.subplot(1,2,2)

### Explanation

# **plt.subplot(1,2,2)** creates the second graph area.

# This subplot will contain the scatter plot.


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

# **s=100** sets the marker size.

# **marker="D"** creates diamond-shaped markers.

# **color="red"** changes marker color to red.


## Add Scatter Plot Title

plt.title("Study Hours vs Marks")

### Explanation

# **plt.title()** adds the title
# "Study Hours vs Marks" to the scatter plot.


## Add X-Axis Label

plt.xlabel("Study Hours")

### Explanation

# **plt.xlabel()** adds the label
# "Study Hours" to the X-axis.


## Add Y-Axis Label

plt.ylabel("Marks")

### Explanation

# **plt.ylabel()** adds the label
# "Marks" to the Y-axis.


## Add Grid Lines

plt.grid(True)

### Explanation

# **plt.grid(True)** enables grid lines
# on both axes.

# This makes data points easier to read.


## Adjust Layout

plt.tight_layout()

### Explanation

# **plt.tight_layout()** automatically adjusts
# spacing between graphs.

# It prevents labels and titles from overlapping.


## Save Dashboard

plt.savefig("student_dashboard.png")

### Explanation

# **plt.savefig()** saves the complete dashboard
# as an image file.

# The file name is **student_dashboard.png**.

# The image is stored in the current working folder.


## Display Dashboard

plt.show()

### Explanation

# **plt.show()** displays the dashboard window.

# It renders both graphs on the screen.

# Without this command, the graphs may not appear.


## Summary

# This program performs the following steps:

# - Import the Matplotlib library.

# - Create student, marks, and study hours data.

# - Create a figure with two graph areas.

# - Display a bar chart of student marks.

# - Display a scatter plot of study hours vs marks.

# - Add titles, labels, and grid lines.

# - Adjust graph spacing automatically.

# - Save the dashboard as student_dashboard.png.

# - Display the dashboard on the screen.
