import pandas as pd

api_data = {
    "City": ["Chennai", "Coimbatore", "Madurai"],
    "Temperature": [34, 31, 33]
}

df = pd.DataFrame(api_data)

print("Data Extracted from API:")
print(df)