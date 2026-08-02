# =====================================================
# EMPLOYEE SALES HISTOGRAM PROGRAM
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
# 4. Create Histogram
# ---------------------------

plt.hist(
    df["Sales"],
    bins=5,
    edgecolor="black",
    alpha=0.7,
    color="green"
)

### Explanation
# **hist()** creates a Histogram.
#
# **df["Sales"]** provides the numerical data.
#
# **bins=5** divides the data into 5 equal intervals (bins).
#
# **edgecolor="black"** adds black borders
# around each histogram bar.
#
# **alpha=0.7** makes the bars slightly transparent.
# Alpha values range from 0 (fully transparent)
# to 1 (fully opaque).
#
# **color="green"** sets the color of the histogram bars.

# ---------------------------
# 5. Add Chart Title
# ---------------------------

plt.title("Sales Distribution")

### Explanation
# **title()** adds a title to the chart.
# It describes what the histogram represents.

# ---------------------------
# 6. Add X-axis Label
# ---------------------------

plt.xlabel("Sales")

### Explanation
# **xlabel()** adds a label to the X-axis.
# It shows that the horizontal axis
# represents sales values.

# ---------------------------
# 7. Add Y-axis Label
# ---------------------------

plt.ylabel("Frequency")

### Explanation
# **ylabel()** adds a label to the Y-axis.
# It shows the frequency (count)
# of values in each interval.

# ---------------------------
# 8. Display Grid
# ---------------------------

plt.grid(True)

### Explanation
# **grid(True)** displays horizontal and vertical grid lines.
# Grid lines make it easier to read
# and compare the histogram bars.

# ---------------------------
# 9. Adjust Layout
# ---------------------------

plt.tight_layout()

### Explanation
# **tight_layout()** automatically adjusts spacing.
# It prevents labels and titles from overlapping.

# ---------------------------
# 10. Display Histogram
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed Histogram
# on the screen.

# =====================================================
# HISTOGRAM INTERPRETATION
# =====================================================

### Explanation
# A Histogram is used to show the distribution
# of numerical data.
#
# In this chart:
#
# ✔ Each bar represents a range (interval) of sales values.
# ✔ The height of each bar shows how many values
#   fall within that range.
# ✔ Taller bars indicate a higher frequency.
# ✔ Shorter bars indicate a lower frequency.
#
# Histograms help identify:
#
# ✔ Data distribution
# ✔ Most common value ranges
# ✔ Data spread
# ✔ Skewness
# ✔ Possible gaps or unusual patterns

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the employee sales dataset.
# ✔ Create a chart figure.
# ✔ Draw a Histogram.
# ✔ Divide the data into 5 bins.
# ✔ Set the bar color.
# ✔ Add black borders to the bars.
# ✔ Apply transparency using alpha.
# ✔ Add a chart title.
# ✔ Add X-axis label.
# ✔ Add Y-axis label.
# ✔ Display grid lines.
# ✔ Adjust chart spacing.
# ✔ Display the completed Histogram.
#
# This program is used to visualize the
# distribution of employee sales data
# using a Histogram with Pandas and Matplotlib.