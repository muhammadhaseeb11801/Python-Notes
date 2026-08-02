# =====================================================
# SALES VS PROFIT LINE CHART PROGRAM
# =====================================================

# ---------------------------
# 1. Import Required Libraries
# ---------------------------

import pandas as pd                  # Import Pandas library for data handling.
import matplotlib.pyplot as plt      # Import Matplotlib library for creating charts.

### Explanation
# **Pandas** is used to load, organize, and analyze the CSV dataset.
# **Matplotlib** is used to create charts and graphs.
# **plt** is the short name (alias) of matplotlib.pyplot.

# ---------------------------
# 2. Load the Dataset
# ---------------------------

df = pd.read_csv("sales_data.csv")   # Read the CSV file.

### Explanation
# **read_csv()** loads the sales data from the CSV file.
# The data is stored inside a Pandas DataFrame called **df**.
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
# 4. Draw Sales Line
# ---------------------------

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o",
    linewidth=3,
    label="Sales"
)

### Explanation
# **plot()** creates the first line chart.
# **df["Month"]** provides the X-axis values.
# **df["Sales"]** provides the Y-axis values.
# **marker="o"** displays circle markers.
# **linewidth=3** makes the line thicker.
# **label="Sales"** creates the legend entry.

# ---------------------------
# 5. Draw Profit Line
# ---------------------------

plt.plot(
    df["Month"],
    df["Profit"],
    marker="s",
    linestyle="--",
    linewidth=3,
    label="Profit"
)

### Explanation
# **plot()** creates the second line chart.
# **df["Month"]** is used as the X-axis.
# **df["Profit"]** provides the Profit values.
# **marker="s"** displays square markers.
# **linestyle="--"** creates a dashed line.
# **linewidth=3** increases the line thickness.
# **label="Profit"** adds the Profit legend.

# ---------------------------
# 6. Add Chart Title
# ---------------------------

plt.title("Sales vs Profit")

### Explanation
# **title()** displays the chart title.
# It describes the comparison between Sales and Profit.

# ---------------------------
# 7. Add X-axis Label
# ---------------------------

plt.xlabel("Month")

### Explanation
# **xlabel()** labels the horizontal axis.
# The X-axis represents months.

# ---------------------------
# 8. Add Y-axis Label
# ---------------------------

plt.ylabel("Amount")

### Explanation
# **ylabel()** labels the vertical axis.
# The Y-axis represents Sales and Profit amounts.

# ---------------------------
# 9. Display Legend
# ---------------------------

plt.legend()

### Explanation
# **legend()** displays the legend.
# It helps identify which line represents Sales
# and which line represents Profit.

# ---------------------------
# 10. Display Grid
# ---------------------------

plt.grid(True)

### Explanation
# **grid(True)** displays horizontal and vertical grid lines.
# Grid lines make the chart easier to read.

# ---------------------------
# 11. Adjust Layout
# ---------------------------

plt.tight_layout()

### Explanation
# **tight_layout()** automatically adjusts spacing.
# It prevents labels and titles from overlapping.

# ---------------------------
# 12. Save Chart
# ---------------------------

plt.savefig("plot_chart.png", dpi=300)

### Explanation
# **savefig()** saves the chart as a PNG image.
# **dpi=300** saves the image in high resolution.

# ---------------------------
# 13. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed chart on the screen.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the sales dataset.
# ✔ Create a chart figure.
# ✔ Draw the Sales line.
# ✔ Draw the Profit line.
# ✔ Add different markers for both lines.
# ✔ Add a dashed style for the Profit line.
# ✔ Add the chart title.
# ✔ Add X-axis label.
# ✔ Add Y-axis label.
# ✔ Display the legend.
# ✔ Display grid lines.
# ✔ Adjust the chart layout.
# ✔ Save the chart as a PNG image.
# ✔ Display the chart.
#
# This program compares Monthly Sales and Monthly Profit
# using a Multiple Line Chart, making it easy to analyze
# business performance over time.