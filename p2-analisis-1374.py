import pandas as pd
import numpy as np 
print("Analisis de datos de vehiculos Cristopher Lopez Nc = 1374 ")

vehiculos = {
    "Modelo": ["Sedan X", "SUV Compact", "Hatchback Z", "Pickup Heavy", "Electric Eco", "Coupe Sport"],
    "Tipo_Motor": ["Gasolina", "Hibrido", "Gasolina", "Diesel", "Electrico", "Gasolina"],
    "Autonomia_Km": [600, 800, 550, 700, 450, 500],
    "Precio_USD": [22000, 35000, 18000, 45000, 32000, 41000]}
df=pd.DataFrame(vehiculos)
print(df)
print("----+--+- Agrupar por una sola columna +----+-+")
agrupado = df.groupby("Modelo")
print(agrupado)
print("----promedio por vehiculo-----")
# Average salary by department
print(agrupado["Autonomia_Km"].mean())

# Maximum age in each department
print(agrupado["Precio_USD"].max())