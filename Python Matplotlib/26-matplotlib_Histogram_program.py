## Import Required Library

import matplotlib.pyplot as plt

## Create Data

marks = [45, 50, 55, 60, 65, 70, 72, 75, 78, 80,
         82, 85, 88, 90, 92, 95, 67, 73, 81, 89]

### Explanation

# **marks** contains the marks of students.

# There are 20 marks values in the dataset.

# These values will be grouped into intervals
# to create a histogram.


## Create Histogram

plt.hist(
    marks,
    bins=5,
    color="skyblue",
    edgecolor="black"
)

### Explanation

# **plt.hist()** is used to create a histogram.

# A histogram shows the frequency distribution
# of numerical data.

# **marks** provides the data values.

# **bins=5** divides the data into 5 groups
# (intervals).

# Each bar shows how many values fall within
# a specific interval.

# **color="skyblue"** changes the color of
# the bars to sky blue.

# **edgecolor="black"** adds black borders
# around each bar.

# This makes the bars easier to see and compare.


## Add Chart Title

plt.title("Student Marks Histogram")

### Explanation

# **plt.title()** adds a title to the histogram.

# The title of this chart is
# "Student Marks Histogram".

# It helps identify what the chart represents.


## Add X-Axis Label

plt.xlabel("Marks")

### Explanation

# **plt.xlabel()** adds a label to the X-axis.

# The X-axis contains marks values.


## Add Y-Axis Label

plt.ylabel("Number of Students")

### Explanation

# **plt.ylabel()** adds a label to the Y-axis.

# The Y-axis shows the number of students
# in each marks interval.


## Add Grid Lines

plt.grid(True)

### Explanation

# **plt.grid(True)** enables grid lines.

# Grid lines make the histogram easier
# to read and understand.


## Display Histogram

plt.show()

### Explanation

# **plt.show()** displays the histogram window.

# It renders the chart and makes it visible
# to the user.

# Without this command, the chart may not appear.


## Summary

# This program performs the following steps:

# - Import the Matplotlib library.

# - Create student marks data.

# - Create a histogram.

# - Divide the data into 5 intervals (bins).

# - Set the bar color to sky blue.

# - Add black borders to the bars.

# - Add a chart title.

# - Add X-axis and Y-axis labels.

# - Enable grid lines.

# - Display the histogram on the screen.
