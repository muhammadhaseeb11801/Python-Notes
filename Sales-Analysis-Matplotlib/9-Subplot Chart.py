# =====================================================
# MULTIPLE SUBPLOTS LINE CHART PROGRAM
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
# 3. Create Subplots
# ---------------------------

fig, ax = plt.subplots(
    2,
    2,
    figsize=(14,10)
)

### Explanation
# **subplots()** creates multiple charts in a single figure.
#
# **2,2**
# creates a grid containing 2 rows and 2 columns.
# Total charts = 4.
#
# **fig**
# represents the complete figure.
#
# **ax**
# is an array containing four plotting areas.
#
# **figsize=(14,10)**
# sets the figure size.
# Width = 14 inches
# Height = 10 inches.

# =====================================================
# FIRST SUBPLOT
# SALES TREND
# =====================================================

ax[0,0].plot(
    df["Month"],
    df["Sales"],
    marker="o",
    label="Sales"
)

### Explanation
# **ax[0,0]**
# refers to the first subplot
# (Row 1, Column 1).
#
# **plot()**
# creates a Line Chart.
#
# **Month**
# is displayed on the X-axis.
#
# **Sales**
# is displayed on the Y-axis.
#
# **marker="o"**
# displays circle markers.
#
# **label="Sales"**
# creates the legend label.

ax[0,0].set_title("Sales Trend")

### Explanation
# **set_title()**
# adds the title to the first subplot.

ax[0,0].legend()

### Explanation
# **legend()**
# displays the legend for the first subplot.

ax[0,0].grid(True)

### Explanation
# **grid(True)**
# displays grid lines for easier reading.

# =====================================================
# SECOND SUBPLOT
# PROFIT TREND
# =====================================================

ax[0,1].plot(
    df["Month"],
    df["Profit"],
    marker="s",
    label="Profit"
)

### Explanation
# **ax[0,1]**
# refers to the second subplot
# (Row 1, Column 2).
#
# **Profit**
# is plotted against Month.
#
# **marker="s"**
# displays square markers.

ax[0,1].set_title("Profit Trend")

### Explanation
# Adds the title for the second subplot.

ax[0,1].legend()

### Explanation
# Displays the legend.

ax[0,1].grid(True)

### Explanation
# Displays grid lines.

# =====================================================
# THIRD SUBPLOT
# CUSTOMER TREND
# =====================================================

ax[1,0].plot(
    df["Month"],
    df["Customers"],
    marker="^",
    label="Customers"
)

### Explanation
# **ax[1,0]**
# refers to the third subplot
# (Row 2, Column 1).
#
# **Customers**
# are plotted against Month.
#
# **marker="^"**
# displays triangle markers.

ax[1,0].set_title("Customer Trend")

### Explanation
# Adds the title for the third subplot.

ax[1,0].legend()

### Explanation
# Displays the legend.

ax[1,0].grid(True)

### Explanation
# Displays grid lines.

# =====================================================
# FOURTH SUBPLOT
# ADVERTISEMENT TREND
# =====================================================

ax[1,1].plot(
    df["Month"],
    df["Advertisement"],
    marker="D",
    label="Advertisement"
)

### Explanation
# **ax[1,1]**
# refers to the fourth subplot
# (Row 2, Column 2).
#
# **Advertisement**
# is plotted against Month.
#
# **marker="D"**
# displays diamond-shaped markers.

ax[1,1].set_title("Advertisement Trend")

### Explanation
# Adds the title for the fourth subplot.

ax[1,1].legend()

### Explanation
# Displays the legend.

ax[1,1].grid(True)

### Explanation
# Displays grid lines.

# ---------------------------
# 4. Adjust Layout
# ---------------------------

plt.tight_layout()

### Explanation
# **tight_layout()**
# automatically adjusts spacing
# between all four subplots.
# It prevents titles and labels
# from overlapping.

# ---------------------------
# 5. Save Chart
# ---------------------------

plt.savefig(
    "subplot_chart.png",
    dpi=300
)

### Explanation
# **savefig()**
# saves all four subplots
# as a single PNG image.
#
# **subplot_chart.png**
# is the output file name.
#
# **dpi=300**
# saves the image in high quality
# suitable for reports and presentations.

# ---------------------------
# 6. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()**
# displays the completed figure
# containing all four subplots.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the sales dataset.
# ✔ Create one figure with four subplots.
# ✔ Plot Sales Trend.
# ✔ Plot Profit Trend.
# ✔ Plot Customer Trend.
# ✔ Plot Advertisement Trend.
# ✔ Add different markers for each line.
# ✔ Add titles for each subplot.
# ✔ Display legends.
# ✔ Display grid lines.
# ✔ Automatically adjust spacing.
# ✔ Save the complete figure as a PNG image.
# ✔ Display all four charts together.
#
# This program uses **Matplotlib Subplots**
# to display four different Line Charts
# in one figure. It allows users to compare
# Sales, Profit, Customers, and Advertisement
# trends simultaneously, making data analysis
# easier and more effective.