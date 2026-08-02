# =====================================================
# MONTHLY SALES PIE CHART PROGRAM
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

plt.figure(figsize=(10,10))

### Explanation
# **figure()** creates a new chart window.
# **figsize=(10,10)** sets the chart size.
# Width = 10 inches
# Height = 10 inches.
# A square figure is ideal for displaying a Pie Chart.

# ---------------------------
# 4. Create Pie Chart
# ---------------------------

plt.pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%"
)

### Explanation
# **pie()** creates a Pie Chart.
#
# **df["Sales"]**
# provides the values used to calculate the size
# of each slice in the pie chart.
#
# **labels=df["Month"]**
# displays the month name on each slice.
#
# **autopct="%1.1f%%"**
# displays the percentage contribution
# of each slice with one decimal place.
#
# Example:
# January → 15.6%
# February → 18.2%

# ---------------------------
# 5. Add Chart Title
# ---------------------------

plt.title("Sales Contribution by Month")

### Explanation
# **title()** adds a title to the chart.
# It describes that the chart shows
# the percentage contribution of sales
# for each month.

# ---------------------------
# 6. Display Legend
# ---------------------------

plt.legend(
    title="Months",
    bbox_to_anchor=(1,1)
)

### Explanation
# **legend()** displays the legend.
#
# **title="Months"**
# sets the legend title.
#
# **bbox_to_anchor=(1,1)**
# places the legend outside the chart
# on the right-hand side.
# This keeps the Pie Chart clean and easy to read.

# ---------------------------
# 7. Adjust Layout
# ---------------------------

plt.tight_layout()

### Explanation
# **tight_layout()** automatically adjusts spacing.
# It prevents labels, title, and legend
# from overlapping.

# ---------------------------
# 8. Save Chart
# ---------------------------

plt.savefig("pie_chart.png", dpi=300)

### Explanation
# **savefig()** saves the Pie Chart as a PNG image.
#
# **pie_chart.png**
# is the file name of the saved image.
#
# **dpi=300**
# saves the image in high quality,
# suitable for reports and presentations.

# ---------------------------
# 9. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed Pie Chart
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
# ✔ Create a Pie Chart.
# ✔ Display monthly sales contribution.
# ✔ Show month names as labels.
# ✔ Display percentage values for each slice.
# ✔ Add a chart title.
# ✔ Display the legend outside the chart.
# ✔ Automatically adjust chart spacing.
# ✔ Save the chart as a high-quality PNG image.
# ✔ Display the chart.
#
# This program visualizes the percentage contribution
# of monthly sales using a Pie Chart.
# Each slice represents one month, making it easy
# to compare the share of total sales contributed
# by each month.