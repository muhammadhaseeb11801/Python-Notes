import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.figure(figsize=(12,6))

plt.scatter(
    df["Advertisement"],
    df["Sales"],
    s=df["Customers"]*4,
    c=df["Customers"],
    cmap="viridis",
    label="Data Points"
)

plt.title("Advertisement vs Sales")
plt.xlabel("Advertisement Cost")
plt.ylabel("Sales")

plt.legend()
plt.colorbar(label="Customers")

plt.tight_layout()
plt.savefig("scatter_chart.png", dpi=300)

plt.show()