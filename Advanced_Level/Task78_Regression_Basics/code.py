import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Advertising": [10, 20, 30, 40, 50],
    "Sales": [15, 25, 35, 45, 55]
}

df = pd.DataFrame(data)

X = df[["Advertising"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X, y)

predicted_sales = model.predict([[60]])

print("Predicted Sales for Advertising = 60:")
print(predicted_sales[0])