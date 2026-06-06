import pandas as pd

students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Ravi", "Priya", "Arun"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [85, 90, 78]
})

merged_data = pd.merge(students, marks, on="ID")

print("Merged Dataset:")
print(merged_data)