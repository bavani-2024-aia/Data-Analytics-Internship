import pandas as pd

sales_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [12000, 15000, 18000, 20000]
}

df = pd.DataFrame(sales_data)

print("Sales Data:")
print(df)

print("\nTotal Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())