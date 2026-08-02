import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.figure(figsize=(12,6))

plt.hist(
    df["Sales"],
    bins=6,
    edgecolor="black",
    label="Sales Distribution"
)

plt.title("Sales Histogram")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("histogram_chart.png", dpi=300)

plt.show()