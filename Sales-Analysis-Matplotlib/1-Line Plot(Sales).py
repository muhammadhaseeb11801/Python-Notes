# =====================================================
# MONTHLY SALES LINE CHART PROGRAM
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

df = pd.read_csv("sales_data.csv")   # Read the CSV file.

### Explanation
# **read_csv()** loads the CSV file.
# The data is stored in a DataFrame called **df**.
# A DataFrame stores data in rows and columns.

# ---------------------------
# 3. Create Figure
# ---------------------------

plt.figure(figsize=(12,6))

### Explanation
# **figure()** creates a new chart.
# **figsize=(12,6)** sets the chart size.
# Width = 12 inches
# Height = 6 inches

# ---------------------------
# 4. Create Line Plot
# ---------------------------

plt.plot(
    df["Month"],
    df["Sales"],
    color="blue",
    marker="o",
    linewidth=3,
    label="Sales"
)

### Explanation
# **plot()** creates a Line Chart.
# **df["Month"]** provides X-axis values.
# **df["Sales"]** provides Y-axis values.
# **color="blue"** sets the line color.
# **marker="o"** displays a circle at each data point.
# **linewidth=3** makes the line thicker.
# **label="Sales"** adds a legend label.

# ---------------------------
# 5. Add Chart Title
# ---------------------------

plt.title("Monthly Sales Trend", fontsize=16)

### Explanation
# **title()** adds a title to the chart.
# **fontsize=16** increases the title size.

# ---------------------------
# 6. Add X-axis Label
# ---------------------------

plt.xlabel("Month")

### Explanation
# **xlabel()** adds a label to the X-axis.
# It shows that the horizontal axis contains months.

# ---------------------------
# 7. Add Y-axis Label
# ---------------------------

plt.ylabel("Sales")

### Explanation
# **ylabel()** adds a label to the Y-axis.
# It shows that the vertical axis represents sales.

# ---------------------------
# 8. Display Legend
# ---------------------------

plt.legend()

### Explanation
# **legend()** displays the chart legend.
# It identifies the plotted line as "Sales".

# ---------------------------
# 9. Display Grid
# ---------------------------

plt.grid(True)

### Explanation
# **grid(True)** displays horizontal and vertical grid lines.
# Grid lines make the chart easier to read.

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

plt.savefig("line_chart.png", dpi=300)

### Explanation
# **savefig()** saves the chart as an image.
# **dpi=300** saves the image in high quality.

# ---------------------------
# 12. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed Line Chart on the screen.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the sales dataset from a CSV file.
# ✔ Create a chart figure.
# ✔ Draw a Line Chart.
# ✔ Set the line color and marker.
# ✔ Set the line width.
# ✔ Add a chart title.
# ✔ Add X-axis label.
# ✔ Add Y-axis label.
# ✔ Display the legend.
# ✔ Display grid lines.
# ✔ Adjust chart spacing.
# ✔ Save the chart as a PNG image.
# ✔ Display the chart.
#
# This program is used to visualize monthly sales trends
# using a Line Chart with Pandas and Matplotlib.