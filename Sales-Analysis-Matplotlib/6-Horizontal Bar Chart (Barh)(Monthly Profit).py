# =====================================================
# MONTHLY PROFIT HORIZONTAL BAR CHART PROGRAM
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
# **read_csv()** loads the sales dataset from the CSV file.
# The data is stored inside a Pandas DataFrame called **df**.
# A DataFrame stores information in rows and columns.

# ---------------------------
# 3. Create Figure
# ---------------------------

plt.figure(figsize=(12,7))

### Explanation
# **figure()** creates a new chart window.
# **figsize=(12,7)** sets the chart size.
# Width = 12 inches
# Height = 7 inches.
# A larger figure provides more space for the horizontal bars.

# ---------------------------
# 4. Create Horizontal Bar Chart
# ---------------------------

plt.barh(
    df["Month"],
    df["Profit"],
    label="Profit"
)

### Explanation
# **barh()** creates a Horizontal Bar Chart.
#
# **df["Month"]**
# provides the values for the Y-axis.
# Each month is displayed as a separate horizontal bar.
#
# **df["Profit"]**
# provides the values for the X-axis.
# The length of each bar represents the profit.
#
# **label="Profit"**
# creates the legend label.

# ---------------------------
# 5. Add Chart Title
# ---------------------------

plt.title("Monthly Profit Horizontal Bar Chart")

### Explanation
# **title()** adds a title to the chart.
# It describes that the chart displays monthly profit
# using a Horizontal Bar Chart.

# ---------------------------
# 6. Add X-axis Label
# ---------------------------

plt.xlabel("Profit")

### Explanation
# **xlabel()** adds a label to the horizontal axis.
# The X-axis represents the profit amount.

# ---------------------------
# 7. Add Y-axis Label
# ---------------------------

plt.ylabel("Month")

### Explanation
# **ylabel()** adds a label to the vertical axis.
# The Y-axis represents the months.

# ---------------------------
# 8. Display Legend
# ---------------------------

plt.legend()

### Explanation
# **legend()** displays the legend.
# It identifies that the horizontal bars represent Profit.

# ---------------------------
# 9. Display Grid
# ---------------------------

plt.grid(axis="x")

### Explanation
# **grid(axis="x")** displays vertical grid lines only.
#
# **axis="x"**
# means the grid is shown along the X-axis.
# This makes it easier to compare the length of the horizontal bars
# and understand profit values.

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

plt.savefig("barh_chart.png", dpi=300)

### Explanation
# **savefig()** saves the chart as a PNG image.
#
# **barh_chart.png**
# is the file name of the saved image.
#
# **dpi=300**
# saves the image in high quality suitable
# for reports and printing.

# ---------------------------
# 12. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed Horizontal Bar Chart
# on the screen.
# The program execution ends after displaying the chart.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the sales dataset.
# ✔ Create a chart figure.
# ✔ Create a Horizontal Bar Chart.
# ✔ Display monthly profit.
# ✔ Add a chart title.
# ✔ Add X-axis label.
# ✔ Add Y-axis label.
# ✔ Display the legend.
# ✔ Display vertical grid lines.
# ✔ Automatically adjust chart spacing.
# ✔ Save the chart as a high-quality PNG image.
# ✔ Display the chart.
#
# This program visualizes monthly profit using a
# Horizontal Bar Chart. Each horizontal bar represents
# the profit of a specific month, making it easy to
# compare profit values across different months.