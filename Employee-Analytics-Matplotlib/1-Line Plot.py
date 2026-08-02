# =====================================================
# EMPLOYEE SALES LINE CHART PROGRAM
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
# 3. Create Figure
# ---------------------------

plt.figure(figsize=(8,5))

### Explanation
# **figure()** creates a new chart.
# **figsize=(8,5)** sets the chart size.
# Width = 8 inches
# Height = 5 inches

# ---------------------------
# 4. Create Line Chart
# ---------------------------

plt.plot(
    df["Employee"],
    df["Sales"],
    marker="o",
    linewidth=2,
    color="blue"
)

### Explanation
# **plot()** creates a Line Chart.
#
# **df["Employee"]** provides X-axis values.
# **df["Sales"]** provides Y-axis values.
#
# **marker="o"** displays a circle at each data point.
# **linewidth=2** makes the line thicker.
# **color="blue"** sets the line color.

# ---------------------------
# 5. Add Chart Title
# ---------------------------

plt.title("Employee Sales Line Chart")

### Explanation
# **title()** adds a title to the chart.
# It describes what the chart represents.

# ---------------------------
# 6. Add X-axis Label
# ---------------------------

plt.xlabel("Employees")

### Explanation
# **xlabel()** adds a label to the X-axis.
# It shows that the horizontal axis contains employee names.

# ---------------------------
# 7. Add Y-axis Label
# ---------------------------

plt.ylabel("Sales")

### Explanation
# **ylabel()** adds a label to the Y-axis.
# It shows that the vertical axis represents sales values.

# ---------------------------
# 8. Display Grid
# ---------------------------

plt.grid(True)

### Explanation
# **grid(True)** displays horizontal and vertical grid lines.
# Grid lines make the chart easier to read and compare values.

# ---------------------------
# 9. Rotate X-axis Labels
# ---------------------------

plt.xticks(rotation=45)

### Explanation
# **xticks(rotation=45)** rotates the employee names
# by 45 degrees.
# This prevents labels from overlapping and
# improves readability.

# ---------------------------
# 10. Adjust Layout
# ---------------------------

plt.tight_layout()

### Explanation
# **tight_layout()** automatically adjusts spacing.
# It prevents chart titles and labels from overlapping.

# ---------------------------
# 11. Display Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed Line Chart
# on the screen.

# =====================================================
# LINE CHART INTERPRETATION
# =====================================================

### Explanation
# A Line Chart is used to display trends or changes
# across ordered data.
#
# In this chart:
#
# ✔ Each point represents one employee.
# ✔ The line connects all employee sales values.
# ✔ Higher points indicate higher sales.
# ✔ Lower points indicate lower sales.
#
# It helps compare sales performance
# between employees quickly.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the employee sales dataset.
# ✔ Create a chart figure.
# ✔ Draw a Line Chart.
# ✔ Set the marker style.
# ✔ Set the line width.
# ✔ Set the line color.
# ✔ Add a chart title.
# ✔ Add X-axis label.
# ✔ Add Y-axis label.
# ✔ Display grid lines.
# ✔ Rotate X-axis labels.
# ✔ Adjust chart spacing.
# ✔ Display the completed chart.
#
# This program is used to visualize and compare
# employee sales using a Line Chart with
# Pandas and Matplotlib.