import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.figure(figsize=(12,7))

plt.barh(
    df["Month"],
    df["Profit"],
    label="Profit"
)

plt.title("Monthly Profit Horizontal Bar Chart")
plt.xlabel("Profit")
plt.ylabel("Month")

plt.legend()
plt.grid(axis="x")

plt.tight_layout()
plt.savefig("barh_chart.png", dpi=300)

plt.show()