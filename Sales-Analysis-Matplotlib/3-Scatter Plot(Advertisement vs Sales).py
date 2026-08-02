# =====================================================
# ADVERTISEMENT VS SALES SCATTER PLOT PROGRAM
# =====================================================

# ---------------------------
# 1. Import Required Libraries
# ---------------------------

import pandas as pd                  # Import Pandas library for data handling.
import matplotlib.pyplot as plt      # Import Matplotlib library for creating charts.

### Explanation
# **Pandas** is used to load and manage the CSV dataset.
# **Matplotlib** is used to create graphs and charts.
# **plt** is the short name (alias) of matplotlib.pyplot.

# ---------------------------
# 2. Load the Dataset
# ---------------------------

df = pd.read_csv("sales_data.csv")   # Read the CSV file.

### Explanation
# **read_csv()** loads the CSV dataset.
# The data is stored inside a DataFrame named **df**.
# A DataFrame stores data in rows and columns.

# ---------------------------
# 3. Create Figure
# ---------------------------

plt.figure(figsize=(12,6))

### Explanation
# **figure()** creates a new chart window.
# **figsize=(12,6)** sets the chart size.
# Width = 12 inches
# Height = 6 inches

# ---------------------------
# 4. Draw Scatter Plot
# ---------------------------

plt.scatter(
    df["Advertisement"],
    df["Sales"],
    s=df["Customers"]*4,
    c=df["Customers"],
    cmap="viridis",
    label="Data Points"
)

### Explanation
# **scatter()** creates a Scatter Plot.
#
# **df["Advertisement"]**
# provides the X-axis values.
#
# **df["Sales"]**
# provides the Y-axis values.
#
# **s=df["Customers"]*4**
# controls the size of each point.
# More customers = Larger point.
#
# **c=df["Customers"]**
# changes the color of each point
# according to the number of customers.
#
# **cmap="viridis"**
# applies the Viridis color map.
# Different customer values appear in different colors.
#
# **label="Data Points"**
# adds the legend label.

# ---------------------------
# 5. Add Chart Title
# ---------------------------

plt.title("Advertisement vs Sales")

### Explanation
# **title()** displays the chart title.
# It describes the relationship between
# Advertisement Cost and Sales.

# ---------------------------
# 6. Add X-axis Label
# ---------------------------

plt.xlabel("Advertisement Cost")

### Explanation
# **xlabel()** labels the horizontal axis.
# The X-axis represents Advertisement Cost.

# ---------------------------
# 7. Add Y-axis Label
# ---------------------------

plt.ylabel("Sales")

### Explanation
# **ylabel()** labels the vertical axis.
# The Y-axis represents Sales.

# ---------------------------
# 8. Display Legend
# ---------------------------

plt.legend()

### Explanation
# **legend()** displays the legend.
# It identifies the plotted data points.

# ---------------------------
# 9. Display Color Bar
# ---------------------------

plt.colorbar(label="Customers")

### Explanation
# **colorbar()** displays a color scale.
# It shows how colors represent
# different customer values.
# Higher customer values have different colors
# than lower customer values.

# ---------------------------
# 10. Adjust Layout
# ---------------------------

plt.tight_layout()

### Explanation
# **tight_layout()** automatically adjusts spacing.
# It prevents labels and titles from overlapping.

# ---------------------------
# 11. Save Chart
# ---------------------------

plt.savefig("scatter_chart.png", dpi=300)

### Explanation
# **savefig()** saves the Scatter Plot
# as a PNG image.
# **dpi=300** saves the image
# in high resolution.

# ---------------------------
# 12. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed Scatter Plot
# on the screen.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the sales dataset.
# ✔ Create a chart figure.
# ✔ Create a Scatter Plot.
# ✔ Use Advertisement Cost as the X-axis.
# ✔ Use Sales as the Y-axis.
# ✔ Set point size based on Customers.
# ✔ Set point color based on Customers.
# ✔ Apply the Viridis color map.
# ✔ Add chart title.
# ✔ Add X-axis label.
# ✔ Add Y-axis label.
# ✔ Display the legend.
# ✔ Display the color bar.
# ✔ Adjust chart spacing.
# ✔ Save the chart as a PNG image.
# ✔ Display the chart.
#
# This program visualizes the relationship between
# Advertisement Cost and Sales using a Scatter Plot.
# The size and color of each point represent
# the number of Customers, making it easier
# to analyze business performance.