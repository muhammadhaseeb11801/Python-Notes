# =====================================================
# PROFESSIONAL BUSINESS DASHBOARD PROGRAM
# =====================================================

# ---------------------------
# 1. Import Required Libraries
# ---------------------------

import pandas as pd                  # Import Pandas library for data handling.
import matplotlib.pyplot as plt      # Import Matplotlib library for creating charts.

### Explanation
# **Pandas** is used to load, organize, and analyze the CSV dataset.
# **Matplotlib** is used to create charts, graphs, and dashboards.
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
# 3. Create Dashboard Figure
# ---------------------------

fig, ax = plt.subplots(
    2,
    2,
    figsize=(16,10)
)

### Explanation
# **subplots()** creates multiple charts inside one figure.
#
# **2,2**
# creates 2 rows and 2 columns.
# Total charts = 4.
#
# **fig**
# represents the complete dashboard.
#
# **ax**
# stores the four plotting areas.
#
# **figsize=(16,10)**
# sets the dashboard size.
# Width = 16 inches
# Height = 10 inches.

# ---------------------------
# 4. Set Dashboard Background
# ---------------------------

fig.patch.set_facecolor("#f5f5f5")

### Explanation
# **set_facecolor()**
# changes the background color
# of the complete dashboard.
#
# **#f5f5f5**
# is a light gray color that gives
# the dashboard a professional appearance.

# ---------------------------
# 5. Add Dashboard Title
# ---------------------------

fig.suptitle(
    "Professional Business Dashboard",
    fontsize=20,
    fontweight="bold"
)

### Explanation
# **suptitle()**
# adds one main title
# for the entire dashboard.
#
# **fontsize=20**
# increases the title size.
#
# **fontweight="bold"**
# makes the title bold.

# =====================================================
# FIRST CHART
# SALES TREND
# =====================================================

ax[0,0].plot(
    df["Month"],
    df["Sales"],
    color="blue",
    marker="o",
    linewidth=3,
    label="Sales"
)

### Explanation
# **plot()**
# creates a Line Chart.
#
# **Month**
# is displayed on the X-axis.
#
# **Sales**
# is displayed on the Y-axis.
#
# **color="blue"**
# makes the line blue.
#
# **marker="o"**
# displays circular markers.
#
# **linewidth=3**
# increases line thickness.
#
# **label="Sales"**
# creates the legend label.

ax[0,0].set_title("Sales Trend")

### Explanation
# Adds the title for the Sales chart.

ax[0,0].legend()

### Explanation
# Displays the legend.

ax[0,0].grid(True)

### Explanation
# Displays grid lines.

# =====================================================
# SECOND CHART
# PROFIT TREND
# =====================================================

ax[0,1].plot(
    df["Month"],
    df["Profit"],
    color="green",
    marker="s",
    linestyle="--",
    linewidth=3,
    label="Profit"
)

### Explanation
# Creates the Profit Line Chart.
#
# **color="green"**
# displays a green line.
#
# **marker="s"**
# displays square markers.
#
# **linestyle="--"**
# displays a dashed line.
#
# **linewidth=3**
# makes the line thicker.

ax[0,1].set_title("Profit Trend")

### Explanation
# Adds the Profit chart title.

ax[0,1].legend()

### Explanation
# Displays the legend.

ax[0,1].grid(True)

### Explanation
# Displays grid lines.

# =====================================================
# THIRD CHART
# SCATTER PLOT
# =====================================================

scatter = ax[1,0].scatter(
    df["Advertisement"],
    df["Sales"],
    s=df["Customers"]*5,
    c=df["Customers"],
    cmap="plasma",
    label="Ad vs Sales"
)

### Explanation
# **scatter()**
# creates a Scatter Plot.
#
# **Advertisement**
# is displayed on the X-axis.
#
# **Sales**
# is displayed on the Y-axis.
#
# **s=df["Customers"]*5**
# controls the size of each point.
# More customers = Larger point.
#
# **c=df["Customers"]**
# changes the point color
# according to customer values.
#
# **cmap="plasma"**
# applies the Plasma color map.
#
# **label="Ad vs Sales"**
# creates the legend label.

ax[1,0].set_title("Advertisement vs Sales")

### Explanation
# Adds the Scatter Plot title.

ax[1,0].legend()

### Explanation
# Displays the legend.

ax[1,0].grid(True)

### Explanation
# Displays grid lines.

# =====================================================
# FOURTH CHART
# CUSTOMER GROWTH
# =====================================================

ax[1,1].bar(
    df["Month"],
    df["Customers"],
    label="Customers"
)

### Explanation
# **bar()**
# creates a Vertical Bar Chart.
#
# **Month**
# is displayed on the X-axis.
#
# **Customers**
# is displayed on the Y-axis.
#
# Each bar represents the total customers
# for a specific month.
#
# **label="Customers"**
# creates the legend label.

ax[1,1].set_title("Customer Growth")

### Explanation
# Adds the Customer Growth chart title.

ax[1,1].legend()

### Explanation
# Displays the legend.

ax[1,1].grid(True)

### Explanation
# Displays grid lines.

# ---------------------------
# 6. Adjust Dashboard Layout
# ---------------------------

plt.tight_layout()

### Explanation
# **tight_layout()**
# automatically adjusts spacing
# between all charts.
# It prevents titles, labels,
# and legends from overlapping.

# ---------------------------
# 7. Save Dashboard
# ---------------------------

plt.savefig(
    "professional_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

### Explanation
# **savefig()**
# saves the complete dashboard
# as a PNG image.
#
# **professional_dashboard.png**
# is the output file name.
#
# **dpi=300**
# saves the image in high quality.
#
# **bbox_inches="tight"**
# removes unnecessary white space
# around the dashboard.

# ---------------------------
# 8. Display Dashboard
# ---------------------------

plt.show()

### Explanation
# **show()**
# displays the complete Professional
# Business Dashboard on the screen.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the sales dataset.
# ✔ Create a professional dashboard.
# ✔ Create four different charts.
# ✔ Display Sales Trend using a Line Chart.
# ✔ Display Profit Trend using a Dashed Line Chart.
# ✔ Display Advertisement vs Sales using a Scatter Plot.
# ✔ Display Customer Growth using a Bar Chart.
# ✔ Add a professional dashboard title.
# ✔ Add titles for each chart.
# ✔ Display legends.
# ✔ Display grid lines.
# ✔ Apply a professional background color.
# ✔ Automatically adjust chart spacing.
# ✔ Save the complete dashboard as a high-quality PNG image.
# ✔ Display the dashboard.
#
# This program creates a Professional Business Dashboard
# using Matplotlib Subplots. It combines four different
# visualizations (Sales Trend, Profit Trend, Advertisement
# vs Sales, and Customer Growth) into a single dashboard,
# making business data easier to analyze, compare,
# and present professionally.