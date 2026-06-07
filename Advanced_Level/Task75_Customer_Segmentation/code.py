import pandas as pd

data = {
    "Customer": ["Ravi", "Priya", "Arun", "Meena"],
    "Purchases": [5, 15, 3, 20]
}

df = pd.DataFrame(data)

df["Segment"] = df["Purchases"].apply(
    lambda x: "Premium" if x >= 10 else "Regular"
)

print(df)