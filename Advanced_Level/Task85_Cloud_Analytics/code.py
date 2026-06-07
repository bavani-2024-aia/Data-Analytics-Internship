import pandas as pd

cloud_data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Revenue": [50000, 60000, 70000]
}

df = pd.DataFrame(cloud_data)

print("Cloud Analytics Data:")
print(df)

print("\nTotal Revenue:", df["Revenue"].sum())