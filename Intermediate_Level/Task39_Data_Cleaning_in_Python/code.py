import pandas as pd

data = {
    "Name": ["Ravi", "Priya", "Ravi"],
    "Marks": [85, 90, 85]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)