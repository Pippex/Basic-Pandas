import pandas as pd
import numpy as np


datos = {'Nombres': ['AnaSofi', 'Enrique', 'Felipe', 'Marisol'],
         'Medallas': [3, 7, 4, np.nan],
         'Calificaciones': [9.9999, 'NaN', 9, 10]}

dataFrame = pd.DataFrame(datos)

print(dataFrame)
print('\n'*2)
print(dataFrame.describe())
print('\n'*2)
dataFrame = dataFrame.replace('NaN', np.nan)
print(dataFrame.describe())
print('\n'*2)
print(dataFrame.info())
print('\n'*2)
print(dataFrame.dropna(how='any'))
print('\n'*2)
print(dataFrame[dataFrame['Calificaciones'] != np.nan])
print('\n'*2)
print(dataFrame['Calificaciones'].mean())
dataFrame.fillna(0, inplace=True)
print('\n'*2)
print(dataFrame)
print('\n'*2)
print(dataFrame.describe())
print('\n'*2)
print(dataFrame.info())

dataFrame['Calificaciones'] = dataFrame.astype(int)

print(dataFrame)