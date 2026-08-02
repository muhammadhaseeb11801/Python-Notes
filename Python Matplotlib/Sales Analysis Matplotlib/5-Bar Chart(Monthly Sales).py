import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.figure(figsize=(12,6))

plt.bar(
    df["Month"],
    df["Sales"],
    label="Sales"
)

plt.title("Monthly Sales Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()
plt.grid(axis="y")

plt.tight_layout()
plt.savefig("bar_chart.png", dpi=300)

plt.show()