# 📊 Matplotlib in Python — A Complete, Friendly Guide

## 📖 What is Matplotlib?

Matplotlib is the most widely used Python library for creating charts and graphs. Whether you want to track sales over time, compare categories, or simply understand your data better, Matplotlib gives you the tools to turn plain numbers into clear, visual stories.

It works well with other popular libraries like NumPy and Pandas, which makes it a natural fit for any data project.

---

## 🧠 How Matplotlib Works — Step by Step

Creating a chart with Matplotlib follows a simple, repeatable process:

---

### ✅ Step 1 — Import Matplotlib

Every Matplotlib project starts with one line:

```python
import matplotlib.pyplot as plt
```

`pyplot` is the part of Matplotlib that handles plotting, and it's almost always imported as `plt` for convenience.

---

### ✅ Step 2 — Prepare Your Data

Before plotting, you need data in a simple format — usually Python lists, NumPy arrays, or Pandas columns.

**Example:**

```python
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [200, 350, 300, 500, 450, 600]
```

---

### ✅ Step 3 — Create a Figure

A "figure" is the blank canvas your chart will be drawn on.

```python
plt.figure(figsize=(7, 4.5))
```

`figsize` controls the width and height of your chart in inches.

---

### ✅ Step 4 — Choose a Chart Type

This is where you decide how your data should be displayed:

| Function | Chart Type |
|---|---|
| `plt.plot()` | Line Chart |
| `plt.bar()` | Bar Chart |
| `plt.barh()` | Horizontal Bar Chart |
| `plt.scatter()` | Scatter Plot |
| `plt.hist()` | Histogram |
| `plt.pie()` | Pie Chart |
| `plt.boxplot()` | Box Plot |
| `plt.fill_between()` | Area Chart |
| `plt.subplots()` | Multiple Charts Together |

---

### ✅ Step 5 — Add Labels & Title

A chart without labels is confusing. Always tell your reader what they're looking at:

```python
plt.title('Monthly Sales Report')
plt.xlabel('Month')
plt.ylabel('Sales (Units)')
```

---

### ✅ Step 6 — Customize the Style

Make your chart clear and easy on the eyes:

```python
plt.grid(alpha=0.3)
plt.legend()
```

You can also change colors, line styles, markers, and fonts to match your needs.

---

### ✅ Step 7 — Show or Save the Chart

Finally, display the chart or save it as an image file:

```python
plt.show()                          # Display it
plt.savefig('sales_chart.png')      # Or save it as an image
```

---

## 🎨 Chart Types in Matplotlib — With Examples

Now that you know the workflow, let's go through every major chart type Matplotlib offers, with a real image and working code for each one.

---

### 1. Line Chart

A line chart connects data points with a line. It's the best choice when you want to show how something changes **over time**, like revenue growing month by month.

```python
plt.plot(months, revenue, marker='o', color='#2563eb', linewidth=2)
plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.grid(alpha=0.3)
plt.show()
```

**Use it when:** you're tracking trends, like stock prices, temperature, or monthly sales.

---

### 2. Bar Chart

A bar chart uses rectangular bars to compare values across different categories. It's great when you want to compare a few groups side by side.

```python
plt.bar(products, sales, color='#16a34a')
plt.title('Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Sales ($)')
plt.show()
```

**Use it when:** comparing categories, like sales across different products or regions.

---

### 3. Horizontal Bar Chart

Same idea as a bar chart, just turned sideways. This is handy when your category names are long and wouldn't fit well under vertical bars.

```python
plt.barh(products, sales, color='#f59e0b')
plt.title('Sales by Product Line (Horizontal)')
plt.xlabel('Sales ($)')
plt.show()
```

**Use it when:** you have long labels or many categories to list.

---

### 4. Scatter Plot

A scatter plot places dots based on two values, showing how two things relate to each other. If the dots form a pattern, there's likely a relationship between the two variables.

```python
plt.scatter(ad_spend, sales, color='#db2777', alpha=0.7)
plt.title('Advertising Spend vs Sales')
plt.xlabel('Ad Spend ($)')
plt.ylabel('Sales ($)')
plt.show()
```

**Use it when:** checking if two things are connected, like ad spend and sales, or hours studied and test scores.

---

### 5. Histogram

A histogram groups numbers into "buckets" and shows how many values fall into each bucket. It's perfect for understanding the shape and spread of your data.

```python
plt.hist(ages, bins=20, color='#7c3aed', edgecolor='white')
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.show()
```

**Use it when:** you want to see how your data is distributed, like ages, scores, or salaries.

---

### 6. Pie Chart

A pie chart shows how a whole is divided into parts. Each slice represents a percentage of the total.

```python
plt.pie(sales, labels=products, autopct='%1.1f%%', startangle=90)
plt.title('Sales Share by Product Line')
plt.show()
```

**Use it when:** showing proportions, like market share or budget breakdown. (Tip: keep the number of slices small — too many makes it hard to read.)

---

### 7. Box Plot

A box plot summarizes data using five numbers: minimum, maximum, median, and the two quartiles. It's a quick way to spot outliers and compare the spread of different groups.

```python
plt.boxplot([storeA, storeB, storeC], tick_labels=['Store A', 'Store B', 'Store C'])
plt.title('Daily Sales Spread by Store')
plt.ylabel('Sales ($)')
plt.show()
```

**Use it when:** comparing the spread and consistency of data across groups, and spotting unusual values.

---

### 8. Area Chart

An area chart is a line chart with the space underneath filled in with color. It works well for showing volume or cumulative growth over time.

```python
plt.fill_between(months, revenue, color='#38bdf8', alpha=0.5)
plt.plot(months, revenue, color='#0284c7', linewidth=2)
plt.title('Revenue Growth Over Time')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.show()
```

**Use it when:** highlighting the size of change over time, not just the direction.

---

### 9. Stacked Bar Chart

A stacked bar chart breaks each bar into smaller segments, so you can see both the total and the individual parts that make it up.

```python
plt.bar(months, offline_sales, label='In-Store', color='#16a34a')
plt.bar(months, online_sales, bottom=offline_sales, label='Online', color='#f59e0b')
plt.title('Revenue: Online vs In-Store')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.legend()
plt.show()
```

**Use it when:** comparing totals while also showing what each total is made of.

---

### 10. Subplots (Multiple Charts Together)

Sometimes one chart is not enough. Subplots let you place several charts side by side in a single figure, so you can compare them at a glance.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
axes[0].plot(months, revenue, marker='o', color='#2563eb')
axes[0].set_title('Revenue Trend')
axes[1].bar(products, sales, color='#16a34a')
axes[1].set_title('Sales by Product')
plt.show()
```

**Use it when:** you want to tell a bigger story using more than one chart at once.

---

## 📋 Quick Cheat Sheet

| Chart Type | Function | Best For |
|---|---|---|
| Line Chart | `plt.plot()` | Trends over time |
| Bar Chart | `plt.bar()` | Comparing categories |
| Horizontal Bar | `plt.barh()` | Long category names |
| Scatter Plot | `plt.scatter()` | Relationship between two variables |
| Histogram | `plt.hist()` | Data distribution |
| Pie Chart | `plt.pie()` | Parts of a whole |
| Box Plot | `plt.boxplot()` | Spread and outliers |
| Area Chart | `plt.fill_between()` | Cumulative growth/volume |
| Stacked Bar | `plt.bar()` (stacked) | Totals + breakdown |
| Subplots | `plt.subplots()` | Multiple charts together |

---

## 🎯 Summary

Matplotlib follows the same simple workflow every time: import the library, prepare your data, create a figure, pick a chart type, add labels, style it, and finally show or save your work. Once this rhythm feels natural, switching between chart types is just a matter of choosing the right function for the story your data is telling.

Start with line and bar charts since they cover most everyday needs, then explore the rest as your projects grow. Happy plotting! 📊
