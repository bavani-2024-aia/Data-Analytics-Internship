import pandas as pd

sales = [100, 120, 140, 160, 180]

average_growth = (sales[-1] - sales[0]) / (len(sales) - 1)

forecast = sales[-1] + average_growth

print("Previous Sales:", sales)
print("Forecasted Next Month Sales:", forecast)