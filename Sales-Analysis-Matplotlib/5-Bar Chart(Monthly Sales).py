# =====================================================
# MONTHLY SALES BAR CHART PROGRAM
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

plt.figure(figsize=(12,6))

### Explanation
# **figure()** creates a new chart window.
# **figsize=(12,6)** sets the size of the chart.
# Width = 12 inches
# Height = 6 inches

# ---------------------------
# 4. Create Bar Chart
# ---------------------------

plt.bar(
    df["Month"],
    df["Sales"],
    label="Sales"
)

### Explanation
# **bar()** creates a Vertical Bar Chart.
#
# **df["Month"]**
# provides the values for the X-axis.
#
# **df["Sales"]**
# provides the values for the Y-axis.
#
# Each bar represents the sales value for one month.
#
# **label="Sales"**
# creates the legend label.

# ---------------------------
# 5. Add Chart Title
# ---------------------------

plt.title("Monthly Sales Bar Chart")

### Explanation
# **title()** adds a title to the chart.
# It describes that the chart displays monthly sales.

# ---------------------------
# 6. Add X-axis Label
# ---------------------------

plt.xlabel("Month")

### Explanation
# **xlabel()** adds a label to the horizontal axis.
# The X-axis represents the months.

# ---------------------------
# 7. Add Y-axis Label
# ---------------------------

plt.ylabel("Sales")

### Explanation
# **ylabel()** adds a label to the vertical axis.
# The Y-axis represents the sales amount.

# ---------------------------
# 8. Display Legend
# ---------------------------

plt.legend()

### Explanation
# **legend()** displays the legend.
# It identifies that the bars represent Sales.

# ---------------------------
# 9. Display Grid
# ---------------------------

plt.grid(axis="y")

### Explanation
# **grid(axis="y")** displays horizontal grid lines only.
#
# **axis="y"**
# means the grid is shown along the Y-axis.
# This makes it easier to compare bar heights.

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

plt.savefig("bar_chart.png", dpi=300)

### Explanation
# **savefig()** saves the chart as a PNG image.
#
# **bar_chart.png**
# is the file name of the saved image.
#
# **dpi=300**
# saves the image in high quality suitable for reports and printing.

# ---------------------------
# 12. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed Bar Chart on the screen.
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
# ✔ Create a Vertical Bar Chart.
# ✔ Display monthly sales.
# ✔ Add a chart title.
# ✔ Add X-axis label.
# ✔ Add Y-axis label.
# ✔ Display the legend.
# ✔ Display horizontal grid lines.
# ✔ Automatically adjust chart spacing.
# ✔ Save the chart as a high-quality PNG image.
# ✔ Display the chart.
#
# This program visualizes monthly sales using a Vertical Bar Chart.
# Each bar represents the sales for a specific month, making it easy
# to compare sales performance across different months.