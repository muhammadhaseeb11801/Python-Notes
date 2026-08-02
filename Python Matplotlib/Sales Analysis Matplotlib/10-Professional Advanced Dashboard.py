import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

fig, ax = plt.subplots(
    2,
    2,
    figsize=(16,10)
)

fig.patch.set_facecolor("#f5f5f5")

fig.suptitle(
    "Professional Business Dashboard",
    fontsize=20,
    fontweight="bold"
)

# Sales
ax[0,0].plot(
    df["Month"],
    df["Sales"],
    color="blue",
    marker="o",
    linewidth=3,
    label="Sales"
)
ax[0,0].set_title("Sales Trend")
ax[0,0].legend()
ax[0,0].grid(True)

# Profit
ax[0,1].plot(
    df["Month"],
    df["Profit"],
    color="green",
    marker="s",
    linestyle="--",
    linewidth=3,
    label="Profit"
)
ax[0,1].set_title("Profit Trend")
ax[0,1].legend()
ax[0,1].grid(True)

# Scatter
scatter = ax[1,0].scatter(
    df["Advertisement"],
    df["Sales"],
    s=df["Customers"]*5,
    c=df["Customers"],
    cmap="plasma",
    label="Ad vs Sales"
)
ax[1,0].set_title("Advertisement vs Sales")
ax[1,0].legend()
ax[1,0].grid(True)

# Customers
ax[1,1].bar(
    df["Month"],
    df["Customers"],
    label="Customers"
)
ax[1,1].set_title("Customer Growth")
ax[1,1].legend()
ax[1,1].grid(True)

plt.tight_layout()

plt.savefig(
    "professional_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()