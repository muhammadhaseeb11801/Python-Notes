# =====================================================
# EMPLOYEE SALES BAR CHART PROGRAM
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

df = pd.read_csv("employee_sales.csv")

### Explanation
# **read_csv()** loads the CSV file.
# The dataset is stored in a DataFrame called **df**.
# A DataFrame stores data in rows and columns.

# ---------------------------
# 3. Create Color List
# ---------------------------

colors = [
    "red", "green", "blue", "orange", "purple",
    "brown", "pink", "gray", "cyan", "gold"
]

### Explanation
# A list of colors is created.
# Each bar will use one color from this list.
# Different colors make the chart more attractive
# and help distinguish each employee.

# ---------------------------
# 4. Create Figure
# ---------------------------

plt.figure(figsize=(10,5))

### Explanation
# **figure()** creates a new chart.
# **figsize=(10,5)** sets the chart size.
# Width = 10 inches
# Height = 5 inches.

# ---------------------------
# 5. Create Bar Chart
# ---------------------------

bars = plt.bar(
    df["Employee"],
    df["Sales"],
    color=colors
)

### Explanation
# **bar()** creates a Vertical Bar Chart.
#
# **df["Employee"]** provides X-axis values.
# **df["Sales"]** provides Y-axis values.
# **color=colors** assigns different colors
# to each bar.

# ---------------------------
# 6. Display Sales Values
# ---------------------------

for bar in bars:

    plt.text(

        bar.get_x() + bar.get_width()/2,

        bar.get_height() + 500,

        int(bar.get_height()),

        ha="center"

    )

### Explanation
# The **for loop** visits each bar one by one.
#
# **plt.text()** displays the sales value
# above every bar.
#
# **bar.get_x()** gets the X position.
# **bar.get_width()** gets the width of the bar.
# **bar.get_height()** gets the height (sales value).
# **ha="center"** centers the text horizontally.

# ---------------------------
# 7. Add Chart Title
# ---------------------------

plt.title("Employee Sales")

### Explanation
# **title()** adds a title to the chart.
# It describes what the chart represents.

# ---------------------------
# 8. Add X-axis Label
# ---------------------------

plt.xlabel("Employees")

### Explanation
# **xlabel()** adds a label to the X-axis.
# It shows that the horizontal axis
# contains employee names.

# ---------------------------
# 9. Add Y-axis Label
# ---------------------------

plt.ylabel("Sales")

### Explanation
# **ylabel()** adds a label to the Y-axis.
# It shows that the vertical axis
# represents employee sales.

# ---------------------------
# 10. Display Grid
# ---------------------------

plt.grid(axis="y")

### Explanation
# **grid(axis="y")** displays
# only horizontal grid lines.
# Horizontal grid lines make it easier
# to compare bar heights.

# ---------------------------
# 11. Rotate X-axis Labels
# ---------------------------

plt.xticks(rotation=45)

### Explanation
# **xticks(rotation=45)** rotates
# employee names by 45 degrees.
# This prevents labels from overlapping.

# ---------------------------
# 12. Adjust Layout
# ---------------------------

plt.tight_layout()

### Explanation
# **tight_layout()** automatically adjusts spacing.
# It prevents labels and titles from overlapping.

# ---------------------------
# 13. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed
# Bar Chart on the screen.

# =====================================================
# BAR CHART INTERPRETATION
# =====================================================

### Explanation
# A Bar Chart is used to compare values
# between different categories.
#
# In this chart:
#
# ✔ Each bar represents one employee.
# ✔ The height of each bar represents sales.
# ✔ Taller bars indicate higher sales.
# ✔ Shorter bars indicate lower sales.
# ✔ Different colors make each employee
#   easy to identify.
# ✔ Sales values are displayed above each bar.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the employee sales dataset.
# ✔ Create a list of bar colors.
# ✔ Create a chart figure.
# ✔ Draw a Vertical Bar Chart.
# ✔ Assign different colors to each bar.
# ✔ Display sales values above every bar.
# ✔ Add a chart title.
# ✔ Add X-axis label.
# ✔ Add Y-axis label.
# ✔ Display horizontal grid lines.
# ✔ Rotate X-axis labels.
# ✔ Adjust chart spacing.
# ✔ Display the completed chart.
#
# This program is used to compare employee
# sales using a colorful Vertical Bar Chart
# with Pandas and Matplotlib.