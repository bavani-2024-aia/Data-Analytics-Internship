import pandas as pd

data = {
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nSummary Statistics:")
print(df.describe())