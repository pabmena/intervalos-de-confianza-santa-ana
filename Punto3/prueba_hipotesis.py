import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind, mannwhitneyu

# Especifica la ruta a tu archivo Excel
excel_file = 'Datos_examen_final_18Co2024_Grupo6.xlsx'

# Lee los datos de las hojas correspondientes
la_floresta = pd.read_excel(excel_file, sheet_name='La Floresta')
palermo = pd.read_excel(excel_file, sheet_name='Palermo')

# Extrae la columna de ventas
ventas_la_floresta = la_floresta['Ventas']
ventas_palermo = palermo['Ventas']

# Prueba de normalidad para La Floresta
stat_la_floresta, p_la_floresta = shapiro(ventas_la_floresta)
print(f"Prueba de Shapiro-Wilk para La Floresta: Estadístico={stat_la_floresta:.4f}, p-valor={p_la_floresta:.4f}")

# Prueba de normalidad para Palermo
stat_palermo, p_palermo = shapiro(ventas_palermo)
print(f"Prueba de Shapiro-Wilk para Palermo: Estadístico={stat_palermo:.4f}, p-valor={p_palermo:.4f}")

# Prueba de homogeneidad de varianzas (Levene)
stat_levene, p_levene = levene(ventas_la_floresta, ventas_palermo)
print(f"Prueba de Levene: Estadístico={stat_levene:.4f}, p-valor={p_levene:.4f}")

# Prueba t para muestras independientes
t_statistic, p_value = ttest_ind(ventas_la_floresta, ventas_palermo, equal_var=True)
print(f"Prueba t: Estadístico t={t_statistic:.4f}, p-valor={p_value:.4e}")

stat_mwu, p_mwu = mannwhitneyu(ventas_la_floresta, ventas_palermo, alternative='two-sided')
print(f"Prueba de Mann-Whitney U: Estadístico U={stat_mwu:.4f}, p-valor={p_mwu:.4e}")
