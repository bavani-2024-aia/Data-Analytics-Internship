import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 130, 170, 220]

plt.plot(months, sales, marker="o")
plt.title("Sales Growth Over Time")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()