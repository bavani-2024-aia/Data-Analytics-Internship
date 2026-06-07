import pandas as pd

# Extract
data = {
    "Name": ["Ravi", "Priya", "Arun"],
    "Marks": [80, 90, 85]
}

df = pd.DataFrame(data)

# Transform
df["Marks"] = df["Marks"] + 5

# Load
print("Processed Data:")
print(df)