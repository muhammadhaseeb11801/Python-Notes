import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.figure(figsize=(12,6))

plt.plot(
    df["Month"],
    df["Customers"],
    marker="D",
    linewidth=3,
    label="Customers"
)

plt.title("Customer Growth")
plt.xlabel("Month")
plt.ylabel("Customers")

plt.grid(
    True,
    linestyle="--",
    linewidth=1
)

plt.legend()

plt.tight_layout()
plt.savefig("grid_chart.png", dpi=300)

plt.show()