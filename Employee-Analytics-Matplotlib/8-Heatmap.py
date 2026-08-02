# =====================================================
# EMPLOYEE SALES CORRELATION HEATMAP PROGRAM
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

df = pd.read_csv("employee_sales.csv")   # Read the CSV file.

### Explanation
# **read_csv()** loads the CSV file.
# The data is stored in a DataFrame called **df**.
# A DataFrame stores data in rows and columns.

# ---------------------------
# 3. Calculate Correlation
# ---------------------------

corr = df[["Sales", "Experience", "Age"]].corr()

### Explanation
# **corr()** calculates the correlation between numerical columns.
# Here, the correlation is calculated for:
# Sales
# Experience
# Age
#
# Correlation values range from -1 to +1.
#
# +1 = Perfect Positive Correlation
#  0 = No Correlation
# -1 = Perfect Negative Correlation

# ---------------------------
# 4. Create Figure
# ---------------------------

plt.figure(figsize=(6,5))

### Explanation
# **figure()** creates a new chart.
# **figsize=(6,5)** sets the chart size.
# Width = 6 inches
# Height = 5 inches

# ---------------------------
# 5. Create Heatmap
# ---------------------------

plt.imshow(
    corr,
    cmap="coolwarm"
)

### Explanation
# **imshow()** displays data as an image.
# Here it converts the correlation matrix into a Heatmap.
#
# **corr** is the correlation matrix.
# **cmap="coolwarm"** applies a color theme.
#
# Blue colors represent lower or negative correlation.
# Red colors represent higher or positive correlation.

# ---------------------------
# 6. Display Color Bar
# ---------------------------

plt.colorbar()

### Explanation
# **colorbar()** displays the color scale.
# It helps understand which color represents
# higher or lower correlation values.

# ---------------------------
# 7. Add X-axis Labels
# ---------------------------

plt.xticks(
    range(len(corr.columns)),
    corr.columns
)

### Explanation
# **xticks()** sets labels on the X-axis.
# **range(len(corr.columns))** creates positions.
# **corr.columns** displays:
# Sales
# Experience
# Age

# ---------------------------
# 8. Add Y-axis Labels
# ---------------------------

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

### Explanation
# **yticks()** sets labels on the Y-axis.
# The same column names are displayed vertically.

# ---------------------------
# 9. Add Chart Title
# ---------------------------

plt.title("Correlation Heatmap")

### Explanation
# **title()** adds a title to the chart.
# It describes the Heatmap.

# ---------------------------
# 10. Display Correlation Values
# ---------------------------

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(
            j,
            i,
            round(corr.iloc[i, j], 2),
            ha="center",
            va="center",
            color="black"
        )

### Explanation
# These nested loops visit every cell in the Heatmap.
#
# **plt.text()** writes the correlation value
# inside each Heatmap cell.
#
# **j** = X-axis position.
# **i** = Y-axis position.
# **round(...,2)** displays values with 2 decimal places.
# **ha="center"** centers text horizontally.
# **va="center"** centers text vertically.
# **color="black"** sets the text color.

# ---------------------------
# 11. Display Heatmap
# ---------------------------

plt.show()

### Explanation
# **show()** displays the completed Heatmap.

# =====================================================
# HEATMAP INTERPRETATION
# =====================================================

### Explanation
# A Heatmap is used to visualize the relationship
# between numerical variables.
#
# The colors indicate the strength of correlation.
#
# Dark Red  = Strong Positive Correlation
# Light Red = Moderate Positive Correlation
# White     = Weak or No Correlation
# Blue      = Negative Correlation
#
# Values close to +1 indicate a strong positive relationship.
# Values close to -1 indicate a strong negative relationship.
# Values close to 0 indicate little or no relationship.

# =====================================================
# SUMMARY
# =====================================================

### Explanation
# This program performs the following tasks:
#
# ✔ Import required libraries.
# ✔ Load the employee sales dataset.
# ✔ Select numerical columns.
# ✔ Calculate the correlation matrix.
# ✔ Create a Heatmap.
# ✔ Apply the "coolwarm" color theme.
# ✔ Display a color scale.
# ✔ Add X-axis labels.
# ✔ Add Y-axis labels.
# ✔ Add a chart title.
# ✔ Display correlation values inside each cell.
# ✔ Display the completed Heatmap.
#
# This program is used to visualize the correlation
# between Sales, Experience, and Age using
# a Heatmap with Pandas and Matplotlib.