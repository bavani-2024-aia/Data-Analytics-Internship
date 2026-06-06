import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "HR", "Sales"],
    "Salary": [50000, 45000, 55000, 47000, 60000]
}

df = pd.DataFrame(data)

result = df.groupby("Department")["Salary"].mean()

print("Average Salary by Department:")
print(result)