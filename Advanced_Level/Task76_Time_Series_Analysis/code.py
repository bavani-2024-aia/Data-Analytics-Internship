import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 120, 140, 130, 160]
}

df = pd.DataFrame(data)

print("Time Series Data:")
print(df)

average_sales = df["Sales"].mean()
print("\nAverage Sales:", average_sales)