# =====================================================
# CUSTOMER GROWTH LINE CHART PROGRAM
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
# **read_csv()** loads the CSV dataset.
# The data is stored inside a Pandas DataFrame named **df**.
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
# 4. Draw Customer Growth Line
# ---------------------------

plt.plot(
    df["Month"],
    df["Customers"],
    marker="D",
    linewidth=3,
    label="Customers"
)

### Explanation
# **plot()** creates a Line Chart.
#
# **df["Month"]**
# provides the values for the X-axis.
#
# **df["Customers"]**
# provides the values for the Y-axis.
#
# **marker="D"**
# displays Diamond-shaped markers at each data point.
#
# **linewidth=3**
# makes the line thicker and easier to see.
#
# **label="Customers"**
# creates the legend label.

# ---------------------------
# 5. Add Chart Title
# ---------------------------

plt.title("Customer Growth")

### Explanation
# **title()** adds a title to the chart.
# It describes that the chart shows customer growth over time.

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

plt.ylabel("Customers")

### Explanation
# **ylabel()** adds a label to the vertical axis.
# The Y-axis represents the number of customers.

# ---------------------------
# 8. Display Grid
# ---------------------------

plt.grid(
    True,
    linestyle="--",
    linewidth=1
)

### Explanation
# **grid(True)** enables grid lines.
#
# **linestyle="--"**
# displays dashed grid lines.
#
# **linewidth=1**
# sets the thickness of the grid lines.
#
# Grid lines make the chart easier to read and compare values.

# ---------------------------
# 9. Display Legend
# ---------------------------

plt.legend()

### Explanation
# **legend()** displays the legend.
# It identifies the plotted line as "Customers".

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

plt.savefig("grid_chart.png", dpi=300)

### Explanation
# **savefig()** saves the chart as a PNG image.
#
# **grid_chart.png**
# is the file name of the saved image.
#
# **dpi=300**
# saves the image in high quality suitable for reports and printing.

# ---------------------------
# 12. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed chart on the screen.
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
# ✔ Plot customer growth using a Line Chart.
# ✔ Display diamond markers on each data point.
# ✔ Increase line thickness for better visibility.
# ✔ Add a chart title.
# ✔ Add X-axis label.
# ✔ Add Y-axis label.
# ✔ Display dashed grid lines.
# ✔ Display the legend.
# ✔ Automatically adjust chart spacing.
# ✔ Save the chart as a high-quality PNG image.
# ✔ Display the chart on the screen.
#
# This program visualizes customer growth over different months
# using a Line Chart. The grid lines, legend, and markers make
# the chart easier to read and analyze.