import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [120, 150, 180, 200]
}

sns.barplot(x=data["Month"], y=data["Sales"])

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("output.png")
print("Chart saved as output.png")