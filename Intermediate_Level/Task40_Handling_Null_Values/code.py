import pandas as pd

data = {
    "Name": ["Ravi", "Priya", "Arun"],
    "Marks": [85, None, 78]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter Handling Null Values:")
print(df)