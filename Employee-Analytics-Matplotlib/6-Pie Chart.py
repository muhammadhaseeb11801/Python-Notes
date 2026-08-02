# =====================================================
# DEPARTMENT-WISE EMPLOYEE DISTRIBUTION PIE CHART PROGRAM
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
# 3. Count Employees by Department
# ---------------------------

department = df["Department"].value_counts()

### Explanation
# **value_counts()** counts the number of employees
# in each department.
#
# The result is stored in **department** and is
# used to create the Pie Chart.

# ---------------------------
# 4. Create Explode List
# ---------------------------

explode = [0.1, 0, 0, 0, 0]

### Explanation
# **explode** separates one or more pie slices.
#
# **0.1** moves the first slice slightly away
# from the center.
#
# **0** keeps the remaining slices in
# their normal positions.

# ---------------------------
# 5. Create Figure
# ---------------------------

plt.figure(figsize=(7,7))

### Explanation
# **figure()** creates a new chart.
# **figsize=(7,7)** sets the chart size.
# Width = 7 inches
# Height = 7 inches.

# ---------------------------
# 6. Create Pie Chart
# ---------------------------

plt.pie(
    department,
    labels=department.index,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True,
    explode=explode
)

### Explanation
# **pie()** creates a Pie Chart.
#
# **department** provides the values for each slice.
#
# **labels=department.index**
# displays the department names.
#
# **autopct="%1.1f%%"**
# displays the percentage of each slice
# with one decimal place.
#
# **startangle=90**
# rotates the chart so that it starts
# from 90 degrees.
#
# **shadow=True**
# adds a shadow effect below the chart.
#
# **explode=explode**
# separates the first slice from the Pie Chart.

# ---------------------------
# 7. Add Chart Title
# ---------------------------

plt.title("Department Wise Employee Distribution")

### Explanation
# **title()** adds a title to the chart.
# It describes what the Pie Chart represents.

# ---------------------------
# 8. Make Pie Chart Circular
# ---------------------------

plt.axis("equal")

### Explanation
# **axis("equal")** ensures that the Pie Chart
# is displayed as a perfect circle.
#
# Without this line, the chart may appear
# stretched into an oval shape.

# ---------------------------
# 9. Display Pie Chart
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed Pie Chart
# on the screen.

# =====================================================
# PIE CHART INTERPRETATION
# =====================================================

### Explanation
# A Pie Chart is used to show how different
# categories contribute to a whole.
#
# In this chart:
#
# ✔ Each slice represents one department.
# ✔ The size of each slice represents
#   the number of employees in that department.
# ✔ Larger slices indicate more employees.
# ✔ Smaller slices indicate fewer employees.
# ✔ Percentages show each department's share
#   of the total employees.
# ✔ The exploded slice highlights
#   the first department for emphasis.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the employee sales dataset.
# ✔ Count employees in each department.
# ✔ Create an explode list.
# ✔ Create a chart figure.
# ✔ Draw a Pie Chart.
# ✔ Display department names.
# ✔ Display percentage values.
# ✔ Rotate the chart using startangle.
# ✔ Add a shadow effect.
# ✔ Highlight the first slice.
# ✔ Add a chart title.
# ✔ Display the Pie Chart as a perfect circle.
# ✔ Display the completed chart.
#
# This program is used to visualize the
# distribution of employees across different
# departments using a Pie Chart with
# Pandas and Matplotlib.