import pandas as pd

sales_data = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet"],
    "Sales": [50000, 30000, 20000]
})

customer_data = pd.DataFrame({
    "Customer": ["Ravi", "Priya", "Arun"],
    "City": ["Chennai", "Coimbatore", "Madurai"]
})

print("Sales Data:")
print(sales_data)

print("\nCustomer Data:")
print(customer_data)

print("\nData stored in a centralized warehouse.")