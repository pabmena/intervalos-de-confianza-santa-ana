import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import f_oneway

# Especifica la ruta a tu archivo Excel
excel_file = 'Datos_examen_final_18Co2024_Grupo6.xlsx'

# Lee los datos de cada hoja en el archivo Excel
santa_ana = pd.read_excel(excel_file, sheet_name='Santa Ana')
la_floresta = pd.read_excel(excel_file, sheet_name='La Floresta')
los_cedros = pd.read_excel(excel_file, sheet_name='Los Cedros')
palermo = pd.read_excel(excel_file, sheet_name='Palermo')
cordoba = pd.read_excel(excel_file, sheet_name='Córdoba')

# Extrae la columna de ventas de cada tienda
ventas_santa_ana = santa_ana['Ventas']
ventas_la_floresta = la_floresta['Ventas']
ventas_los_cedros = los_cedros['Ventas']
ventas_palermo = palermo['Ventas']
ventas_cordoba = cordoba['Ventas']

# Realiza el ANOVA
f_statistic, p_value = f_oneway(ventas_santa_ana, ventas_la_floresta, ventas_los_cedros, ventas_palermo, ventas_cordoba)

print(f'Estadístico F: {f_statistic}')
print(f'Valor p: {p_value}')

# Calcular los promedios de ventas
promedio_santa_ana = ventas_santa_ana.mean()
promedio_la_floresta = ventas_la_floresta.mean()
promedio_los_cedros = ventas_los_cedros.mean()
promedio_palermo = ventas_palermo.mean()
promedio_cordoba = ventas_cordoba.mean()

# Mostrar los promedios
print(f"Promedio Santa Ana: {promedio_santa_ana:.2f}")
print(f"Promedio La Floresta: {promedio_la_floresta:.2f}")
print(f"Promedio Los Cedros: {promedio_los_cedros:.2f}")
print(f"Promedio Palermo: {promedio_palermo:.2f}")
print(f"Promedio Córdoba: {promedio_cordoba:.2f}")
