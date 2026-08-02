# =====================================================
# SALES HISTOGRAM PROGRAM
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
# **figsize=(12,6)** sets the chart size.
# Width = 12 inches
# Height = 6 inches.

# ---------------------------
# 4. Create Histogram
# ---------------------------

plt.hist(
    df["Sales"],
    bins=6,
    edgecolor="Red",
    label="Sales Distribution"
)

### Explanation
# **hist()** creates a Histogram.
#
# **df["Sales"]**
# provides the Sales data to be analyzed.
#
# **bins=6**
# divides the Sales values into 6 equal intervals (groups).
# Each bar shows how many sales values fall within that range.
#
# **edgecolor="black"**
# adds a black border around each histogram bar,
# making the bars easier to distinguish.
#
# **label="Sales Distribution"**
# creates the legend label.

# ---------------------------
# 5. Add Chart Title
# ---------------------------

plt.title("Sales Histogram")

### Explanation
# **title()** adds a title to the chart.
# It describes that the chart displays
# the distribution of Sales values.

# ---------------------------
# 6. Add X-axis Label
# ---------------------------

plt.xlabel("Sales")

### Explanation
# **xlabel()** adds a label to the horizontal axis.
# The X-axis represents Sales values.

# ---------------------------
# 7. Add Y-axis Label
# ---------------------------

plt.ylabel("Frequency")

### Explanation
# **ylabel()** adds a label to the vertical axis.
# The Y-axis represents the frequency (count)
# of Sales values in each interval.

# ---------------------------
# 8. Display Legend
# ---------------------------

plt.legend()

### Explanation
# **legend()** displays the legend.
# It identifies that the histogram
# represents Sales Distribution.

# ---------------------------
# 9. Display Grid
# ---------------------------

plt.grid(True)

### Explanation
# **grid(True)** displays horizontal and vertical grid lines.
# Grid lines make it easier to compare
# the height of the histogram bars.

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

plt.savefig("histogram_chart.png", dpi=300)

### Explanation
# **savefig()** saves the histogram as a PNG image.
#
# **histogram_chart.png**
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
# **show()** displays the completed Histogram
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
# ✔ Create a Histogram.
# ✔ Divide Sales values into 6 intervals (bins).
# ✔ Display the frequency of Sales values.
# ✔ Add black borders to histogram bars.
# ✔ Add a chart title.
# ✔ Add X-axis label.
# ✔ Add Y-axis label.
# ✔ Display the legend.
# ✔ Display grid lines.
# ✔ Automatically adjust chart spacing.
# ✔ Save the chart as a high-quality PNG image.
# ✔ Display the chart.
#
# This program visualizes the distribution of Sales values
# using a Histogram. It helps analyze how frequently
# different Sales ranges occur in the dataset,
# making it easier to understand the overall sales distribution.