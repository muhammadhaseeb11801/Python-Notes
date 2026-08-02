# =====================================================
# EMPLOYEE SALES HORIZONTAL BAR CHART PROGRAM
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

plt.figure(figsize=(8,6))

### Explanation
# **figure()** creates a new chart.
# **figsize=(8,6)** sets the chart size.
# Width = 8 inches
# Height = 6 inches.

# ---------------------------
# 4. Create Horizontal Bar Chart
# ---------------------------

plt.barh(
    df["Employee"],
    df["Sales"],
    color="skyblue"
)

### Explanation
# **barh()** creates a Horizontal Bar Chart.
#
# **df["Employee"]** provides Y-axis values.
# **df["Sales"]** provides X-axis values.
#
# **color="skyblue"** sets the color of all bars.

# ---------------------------
# 5. Add Chart Title
# ---------------------------

plt.title("Employee Sales")

### Explanation
# **title()** adds a title to the chart.
# It describes what the chart represents.

# ---------------------------
# 6. Add X-axis Label
# ---------------------------

plt.xlabel("Sales")

### Explanation
# **xlabel()** adds a label to the X-axis.
# It shows that the horizontal axis
# represents employee sales.

# ---------------------------
# 7. Add Y-axis Label
# ---------------------------

plt.ylabel("Employees")

### Explanation
# **ylabel()** adds a label to the Y-axis.
# It shows that the vertical axis
# contains employee names.

# ---------------------------
# 8. Display Grid
# ---------------------------

plt.grid(axis="x")

### Explanation
# **grid(axis="x")** displays
# only vertical grid lines.
# These grid lines make it easier
# to compare the length of each bar.

# ---------------------------
# 9. Adjust Layout
# ---------------------------

plt.tight_layout()

### Explanation
# **tight_layout()** automatically adjusts spacing.
# It prevents labels and titles from overlapping.

# ---------------------------
# 10. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed
# Horizontal Bar Chart on the screen.

# =====================================================
# HORIZONTAL BAR CHART INTERPRETATION
# =====================================================

### Explanation
# A Horizontal Bar Chart is used to compare
# values between different categories.
#
# In this chart:
#
# ✔ Each horizontal bar represents one employee.
# ✔ The length of each bar represents sales.
# ✔ Longer bars indicate higher sales.
# ✔ Shorter bars indicate lower sales.
# ✔ It is especially useful when category names
#   are long because they are easier to read.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the employee sales dataset.
# ✔ Create a chart figure.
# ✔ Draw a Horizontal Bar Chart.
# ✔ Set the bar color.
# ✔ Add a chart title.
# ✔ Add X-axis label.
# ✔ Add Y-axis label.
# ✔ Display vertical grid lines.
# ✔ Adjust chart spacing.
# ✔ Display the completed chart.
#
# This program is used to compare employee
# sales using a Horizontal Bar Chart
# with Pandas and Matplotlib.