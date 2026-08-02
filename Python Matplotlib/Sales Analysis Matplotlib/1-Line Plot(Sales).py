import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.figure(figsize=(12,6))

plt.plot(
    df["Month"],
    df["Sales"],
    color="blue",
    marker="o",
    linewidth=3,
    label="Sales"
)

plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("line_chart.png", dpi=300)

plt.show()