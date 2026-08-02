import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.figure(figsize=(10,10))

plt.pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%"
)

plt.title("Sales Contribution by Month")

plt.legend(
    title="Months",
    bbox_to_anchor=(1,1)
)

plt.tight_layout()
plt.savefig("pie_chart.png", dpi=300)

plt.show()