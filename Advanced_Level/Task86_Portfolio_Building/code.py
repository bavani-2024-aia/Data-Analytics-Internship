import pandas as pd

projects = {
    "Project": [
        "EDA",
        "Sales Analysis",
        "Customer Segmentation",
        "Forecasting",
        "Data Visualization"
    ]
}

df = pd.DataFrame(projects)

print("My Data Analytics Portfolio")
print(df)
print("\nPortfolio Created Successfully!")