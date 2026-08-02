import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

fig, ax = plt.subplots(
    2,
    2,
    figsize=(14,10)
)

ax[0,0].plot(df["Month"], df["Sales"],
             marker="o",
             label="Sales")
ax[0,0].set_title("Sales Trend")
ax[0,0].legend()
ax[0,0].grid(True)

ax[0,1].plot(df["Month"], df["Profit"],
             marker="s",
             label="Profit")
ax[0,1].set_title("Profit Trend")
ax[0,1].legend()
ax[0,1].grid(True)

ax[1,0].plot(df["Month"], df["Customers"],
             marker="^",
             label="Customers")
ax[1,0].set_title("Customer Trend")
ax[1,0].legend()
ax[1,0].grid(True)

ax[1,1].plot(df["Month"], df["Advertisement"],
             marker="D",
             label="Advertisement")
ax[1,1].set_title("Advertisement Trend")
ax[1,1].legend()
ax[1,1].grid(True)

plt.tight_layout()

plt.savefig(
    "subplot_chart.png",
    dpi=300
)

plt.show()