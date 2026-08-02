# =====================================================
# EMPLOYEE SALES BOX PLOT PROGRAM
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

df = pd.read_csv("employee_sales.csv")   # Read the CSV file.

### Explanation
# **read_csv()** loads the CSV file.
# The data is stored in a DataFrame called **df**.
# A DataFrame stores data in rows and columns.

# ---------------------------
# 3. Create Figure
# ---------------------------

plt.figure(figsize=(6,5))

### Explanation
# **figure()** creates a new chart.
# **figsize=(6,5)** sets the chart size.
# Width = 6 inches
# Height = 5 inches

# ---------------------------
# 4. Create Box Plot
# ---------------------------

plt.boxplot(
    df["Sales"],
    patch_artist=True
)

### Explanation
# **boxplot()** creates a Box Plot.
# **df["Sales"]** provides the numerical data.
# **patch_artist=True** fills the box with color
# (default Matplotlib color is used unless specified).

# ---------------------------
# 5. Add Chart Title
# ---------------------------

plt.title("Employee Sales Box Plot")

### Explanation
# **title()** adds a title to the chart.
# It describes what the chart represents.

# ---------------------------
# 6. Add Y-axis Label
# ---------------------------

plt.ylabel("Sales")

### Explanation
# **ylabel()** adds a label to the Y-axis.
# It shows that the vertical axis represents sales values.

# ---------------------------
# 7. Display Grid
# ---------------------------

plt.grid(True)

### Explanation
# **grid(True)** displays horizontal and vertical grid lines.
# Grid lines make the chart easier to read and compare values.

# ---------------------------
# 8. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed Box Plot on the screen.

# =====================================================
# BOX PLOT INTERPRETATION
# =====================================================

### Explanation
# A Box Plot displays the distribution of numerical data.
#
# It shows:
#
# ✔ Minimum Value
# ✔ First Quartile (Q1)
# ✔ Median (Middle Value)
# ✔ Third Quartile (Q3)
# ✔ Maximum Value
# ✔ Outliers (if present)
#
# The line inside the box represents the Median.
# The box represents the middle 50% of the data (Interquartile Range - IQR).
# The whiskers show the spread of the remaining data.
# Any points outside the whiskers are called Outliers.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the employee sales dataset.
# ✔ Create a chart figure.
# ✔ Draw a Box Plot.
# ✔ Display the distribution of sales values.
# ✔ Show the median and quartiles.
# ✔ Identify possible outliers.
# ✔ Add a chart title.
# ✔ Add a Y-axis label.
# ✔ Display grid lines.
# ✔ Display the Box Plot.
#
# This program is used to analyze the distribution,
# spread, median, and outliers of employee sales data
# using a Box Plot with Pandas and Matplotlib.