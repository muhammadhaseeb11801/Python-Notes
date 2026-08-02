import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.figure(figsize=(12,6))

plt.plot(df["Month"], df["Sales"],
         marker="o",
         linewidth=3,
         label="Sales")

plt.plot(df["Month"], df["Profit"],
         marker="s",
         linestyle="--",
         linewidth=3,
         label="Profit")

plt.title("Sales vs Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("plot_chart.png", dpi=300)

plt.show()