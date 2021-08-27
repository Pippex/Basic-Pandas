import pandas as pd 
import numpy as np

BChart = pd.read_csv("BCH-USD.csv")

print(BChart)
print("\n")
print(BChart.info())
print("\n")
print(BChart.describe())
print("\n")