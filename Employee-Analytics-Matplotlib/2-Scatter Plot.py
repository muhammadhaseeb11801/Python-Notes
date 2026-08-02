# =====================================================
# EMPLOYEE EXPERIENCE VS SALES SCATTER PLOT PROGRAM
# =====================================================

# ---------------------------
# 1. Import Required Libraries
# ---------------------------

import pandas as pd                  # Import Pandas library for data handling.
import matplotlib.pyplot as plt      # Import Matplotlib library for creating charts.

### Explanation
# **Pandas** is used to load and manage the CSV dataset.
# **Matplotlib** is used to create charts and graphs.
# **plt** is the short name (alias) of matplotlib.pyplot.

# ---------------------------
# 2. Load the Dataset
# ---------------------------

df = pd.read_csv("employee_sales.csv")

### Explanation
# **read_csv()** loads the CSV file.
# The dataset is stored in a DataFrame called **df**.
# A DataFrame stores data in rows and columns.

# ---------------------------
# 3. Create Figure
# ---------------------------

plt.figure(figsize=(8,5))

### Explanation
# **figure()** creates a new chart.
# **figsize=(8,5)** sets the chart size.
# Width = 8 inches
# Height = 5 inches.

# ---------------------------
# 4. Create Scatter Plot
# ---------------------------

plt.scatter(
    df["Experience"],
    df["Sales"],
    s=100,
    color="blue"
)

### Explanation
# **scatter()** creates a Scatter Plot.
#
# **df["Experience"]** provides X-axis values.
# **df["Sales"]** provides Y-axis values.
#
# **s=100** sets the marker size.
# Larger values create larger dots.
#
# **color="blue"** sets the marker color.

# ---------------------------
# 5. Add Chart Title
# ---------------------------

plt.title("Experience vs Sales")

### Explanation
# **title()** adds a title to the chart.
# It describes the relationship being shown.

# ---------------------------
# 6. Add X-axis Label
# ---------------------------

plt.xlabel("Experience (Years)")

### Explanation
# **xlabel()** adds a label to the X-axis.
# It indicates that the horizontal axis
# represents employee experience in years.

# ---------------------------
# 7. Add Y-axis Label
# ---------------------------

plt.ylabel("Sales")

### Explanation
# **ylabel()** adds a label to the Y-axis.
# It indicates that the vertical axis
# represents employee sales.

# ---------------------------
# 8. Display Grid
# ---------------------------

plt.grid(True)

### Explanation
# **grid(True)** displays horizontal and vertical grid lines.
# Grid lines make it easier to compare data points.

# ---------------------------
# 9. Adjust Layout
# ---------------------------

plt.tight_layout()

### Explanation
# **tight_layout()** automatically adjusts spacing.
# It prevents chart labels and title from overlapping.

# ---------------------------
# 10. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed Scatter Plot
# on the screen.

# =====================================================
# SCATTER PLOT INTERPRETATION
# =====================================================

### Explanation
# A Scatter Plot is used to show the relationship
# between two numerical variables.
#
# In this chart:
#
# ✔ Each dot represents one employee.
# ✔ The X-axis shows employee experience.
# ✔ The Y-axis shows employee sales.
# ✔ Dots higher on the chart indicate higher sales.
# ✔ Dots farther to the right indicate more experience.
#
# If the dots move upward from left to right,
# it suggests a positive relationship.
#
# If the dots move downward,
# it suggests a negative relationship.
#
# If the dots appear randomly scattered,
# there is little or no relationship.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the employee sales dataset.
# ✔ Create a chart figure.
# ✔ Draw a Scatter Plot.
# ✔ Set the marker size.
# ✔ Set the marker color.
# ✔ Add a chart title.
# ✔ Add X-axis label.
# ✔ Add Y-axis label.
# ✔ Display grid lines.
# ✔ Adjust chart spacing.
# ✔ Display the completed chart.
#
# This program is used to visualize the relationship
# between employee experience and sales
# using a Scatter Plot with Pandas and Matplotlib.