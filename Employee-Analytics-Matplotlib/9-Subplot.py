# =====================================================
# EMPLOYEE SALES ANALYSIS DASHBOARD PROGRAM
# =====================================================

# ---------------------------
# 1. Import Required Libraries
# ---------------------------

import pandas as pd                  # Import Pandas library for data handling.
import matplotlib.pyplot as plt      # Import Matplotlib library for creating charts.

### Explanation
# **Pandas** is used to load and manage the CSV dataset.
# **Matplotlib** is used to create charts and dashboards.
# **plt** is the alias (short name) of matplotlib.pyplot.

# ---------------------------
# 2. Load the Dataset
# ---------------------------

df = pd.read_csv("employee_sales.csv")

### Explanation
# **read_csv()** loads the CSV file.
# The dataset is stored in a DataFrame named **df**.

# ---------------------------
# 3. Count Departments
# ---------------------------

dept = df["Department"].value_counts()

### Explanation
# **value_counts()** counts how many employees
# belong to each department.
# The result is used in the Pie Chart.

# ---------------------------
# 4. Calculate Correlation
# ---------------------------

corr = df[["Sales", "Experience", "Age"]].corr()

### Explanation
# **corr()** calculates the correlation
# between numerical columns.
#
# Here it compares:
# Sales
# Experience
# Age

# ---------------------------
# 5. Create Dashboard Figure
# ---------------------------

fig, ax = plt.subplots(3,3,figsize=(18,15))

### Explanation
# **subplots()** creates multiple charts
# in one figure.
#
# **3,3** creates a dashboard containing
# 9 charts.
#
# **figsize=(18,15)** sets the dashboard size.

# =====================================================
# CHART 1 - LINE CHART
# =====================================================

ax[0,0].plot(
    df["Employee"],
    df["Sales"],
    marker='o',
    linewidth=2,
    color="blue"
)

### Explanation
# Creates a Line Chart.
#
# Employee → X-axis
# Sales → Y-axis
#
# marker='o' displays circles.
# linewidth=2 makes the line thicker.
# color="blue" sets the line color.

ax[0,0].set_title("Line Chart")
ax[0,0].set_xlabel("Employee")
ax[0,0].set_ylabel("Sales")
ax[0,0].grid(True)
ax[0,0].tick_params(axis="x", rotation=45)

### Explanation
# Adds chart title.
# Adds X-axis label.
# Adds Y-axis label.
# Displays grid lines.
# Rotates employee names by 45°.

# =====================================================
# CHART 2 - SCATTER PLOT
# =====================================================

ax[0,1].scatter(
    df["Experience"],
    df["Sales"],
    s=100,
    color="red"
)

### Explanation
# Creates a Scatter Plot.
#
# Experience → X-axis
# Sales → Y-axis
#
# s=100 sets marker size.
# color="red" changes marker color.

ax[0,1].set_title("Scatter Plot")
ax[0,1].set_xlabel("Experience")
ax[0,1].set_ylabel("Sales")
ax[0,1].grid(True)

# =====================================================
# CHART 3 - BAR CHART
# =====================================================

bars = ax[0,2].bar(
    df["Employee"],
    df["Sales"]
)

### Explanation
# Creates a Vertical Bar Chart.
#
# Each bar represents
# an employee's sales.

for bar in bars:

    ax[0,2].text(

        bar.get_x()+bar.get_width()/2,

        bar.get_height()+500,

        int(bar.get_height()),

        ha="center",

        fontsize=8

    )

### Explanation
# Displays sales values
# above every bar.
#
# get_x() gets the X position.
# get_width() gets bar width.
# get_height() gets bar height.

ax[0,2].set_title("Bar Chart")
ax[0,2].set_xlabel("Employee")
ax[0,2].set_ylabel("Sales")
ax[0,2].grid(axis="y")
ax[0,2].tick_params(axis="x", rotation=45)

# =====================================================
# CHART 4 - HORIZONTAL BAR CHART
# =====================================================

ax[1,0].barh(
    df["Employee"],
    df["Sales"]
)

### Explanation
# Creates a Horizontal Bar Chart.
#
# Employees appear vertically.
# Sales values appear horizontally.

ax[1,0].set_title("Horizontal Bar Chart")
ax[1,0].set_xlabel("Sales")
ax[1,0].set_ylabel("Employee")
ax[1,0].grid(axis="x")

# =====================================================
# CHART 5 - HISTOGRAM
# =====================================================

ax[1,1].hist(

    df["Sales"],

    bins=5,

    edgecolor="black",

    alpha=0.7

)

### Explanation
# Creates a Histogram.
#
# bins=5 divides data
# into five intervals.
#
# edgecolor="black"
# adds black borders.
#
# alpha=0.7 adds transparency.

ax[1,1].set_title("Histogram")
ax[1,1].set_xlabel("Sales")
ax[1,1].set_ylabel("Frequency")
ax[1,1].grid(True)

# =====================================================
# CHART 6 - PIE CHART
# =====================================================

explode = [

    0.1 if i==0 else 0

    for i in range(len(dept))

]

### Explanation
# Explodes (separates)
# the first pie slice.

ax[1,2].pie(

    dept,

    labels=dept.index,

    autopct="%1.1f%%",

    startangle=90,

    shadow=True,

    explode=explode

)

### Explanation
# Creates a Pie Chart.
#
# labels show department names.
# autopct shows percentages.
# startangle rotates the chart.
# shadow adds shadow effect.
# explode separates one slice.

ax[1,2].set_title("Department Distribution")
ax[1,2].axis("equal")

### Explanation
# axis("equal")
# makes the Pie Chart circular.

# =====================================================
# CHART 7 - BOX PLOT
# =====================================================

ax[2,0].boxplot(

    df["Sales"],

    patch_artist=True

)

### Explanation
# Creates a Box Plot.
#
# Displays:
# Minimum
# Maximum
# Median
# Quartiles
# Outliers

ax[2,0].set_title("Box Plot")
ax[2,0].set_ylabel("Sales")
ax[2,0].grid(True)

# =====================================================
# CHART 8 - HEATMAP
# =====================================================

heat = ax[2,1].imshow(

    corr,

    cmap="coolwarm"

)

### Explanation
# Creates a Correlation Heatmap.
#
# cmap="coolwarm"
# applies blue-red colors.

ax[2,1].set_xticks(range(len(corr.columns)))
ax[2,1].set_xticklabels(corr.columns)

ax[2,1].set_yticks(range(len(corr.columns)))
ax[2,1].set_yticklabels(corr.columns)

### Explanation
# Displays column names
# on both axes.

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):

        ax[2,1].text(

            j,

            i,

            round(corr.iloc[i,j],2),

            ha="center",

            va="center",

            color="black"

        )

### Explanation
# Displays correlation values
# inside each Heatmap cell.

ax[2,1].set_title("Heatmap")

fig.colorbar(

    heat,

    ax=ax[2,1]

)

### Explanation
# Displays the Heatmap color scale.

# =====================================================
# CHART 9 - EXPERIENCE TREND
# =====================================================

ax[2,2].plot(

    df["Experience"],

    df["Sales"],

    marker="o",

    linestyle="--"

)

### Explanation
# Creates a Line Chart showing
# Experience vs Sales.
#
# linestyle="--"
# creates a dashed line.

ax[2,2].set_title("Experience vs Sales")
ax[2,2].set_xlabel("Experience")
ax[2,2].set_ylabel("Sales")
ax[2,2].grid(True)

# =====================================================
# DASHBOARD TITLE
# =====================================================

plt.suptitle(

    "Employee Sales Analysis Dashboard",

    fontsize=22,

    fontweight="bold"

)

### Explanation
# **suptitle()** adds
# one main title
# for the complete dashboard.

# =====================================================
# ADJUST LAYOUT
# =====================================================

plt.tight_layout()

### Explanation
# **tight_layout()**
# automatically adjusts spacing
# between all charts.

# =====================================================
# DISPLAY DASHBOARD
# =====================================================

plt.show()

### Explanation
# **show()** displays
# the complete dashboard.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This dashboard performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the employee sales dataset.
# ✔ Count department records.
# ✔ Calculate correlation values.
# ✔ Create a 3×3 dashboard layout.
# ✔ Display a Line Chart.
# ✔ Display a Scatter Plot.
# ✔ Display a Vertical Bar Chart.
# ✔ Display a Horizontal Bar Chart.
# ✔ Display a Histogram.
# ✔ Display a Pie Chart.
# ✔ Display a Box Plot.
# ✔ Display a Correlation Heatmap.
# ✔ Display an Experience vs Sales trend chart.
# ✔ Add chart titles and axis labels.
# ✔ Display grid lines.
# ✔ Add a dashboard title.
# ✔ Adjust chart spacing.
# ✔ Display the completed dashboard.
#
# This program is used to analyze employee sales data
# using multiple visualization techniques in a single
# professional Matplotlib dashboard.