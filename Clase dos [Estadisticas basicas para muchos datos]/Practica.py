import pandas as pd 
import numpy as np

BChart = pd.read_csv("BCH-USD.csv")

print(BChart)
print("\n")
print(BChart.info())
print("\n")
print(BChart.describe())
print("\n")
print(BChart.head())

BChart.replace(666,"Cagaste")
print("\n")
print(BChart.info())
print("\n")

for d in BChart["Open"]:
    if d == "Cagaste":
        print("Ya cagaste")
for d in BChart["High"]:
    if d == "Cagaste":
        print("Ya cagaste")
for d in BChart["Low"]:
    if d == "Cagaste":
        print("Ya cagaste")

print("\n")
print(BChart.describe(include=[np.number]))
print("\n")
print(list(BChart))
BChart = BChart.set_index('Date')
close_price = BChart["Close"]
print(close_price)
print(BChart)
print("\n")
print(BChart["Close"].astype(float))
print("\n")
print(BChart.head())