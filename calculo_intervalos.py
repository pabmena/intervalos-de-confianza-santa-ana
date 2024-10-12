import pandas as pd
import numpy as np
from scipy import stats

# Leer los datos desde la hoja 'Santa Ana' del archivo Excel
data = pd.read_excel('Datos_examen_final_18Co2024_Grupo6.xlsx', sheet_name='Santa Ana')

# Convertir la columna 'Fecha' al tipo datetime
data['Fecha'] = pd.to_datetime(data['Fecha'], dayfirst=True)

# Agregar una columna con el mes
data['Mes'] = data['Fecha'].dt.month

# Mapeo de números de mes a nombres en español
meses_dict = {
    1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio',
    7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
}

data['Mes'] = data['Mes'].map(meses_dict)

# Ordenar los meses correctamente
meses_ordenados = [
    'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
    'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
]

# Lista para almacenar los resultados
resultados = []

# Niveles de confianza
confianzas = [0.95, 0.99]

# Iterar sobre cada mes
for mes in meses_ordenados:
    datos_mes = data[data['Mes'] == mes]['Ventas']
    n = len(datos_mes)
    if n == 0:
        continue  # Saltar si no hay datos para el mes
    media = datos_mes.mean()
    desviacion = datos_mes.std(ddof=1)
    SE = desviacion / np.sqrt(n)
    df = n - 1

    # Calcular intervalos de confianza
    intervalos = {}
    for conf in confianzas:
        alpha = 1 - conf
        t_critico = stats.t.ppf(1 - alpha/2, df)
        ME = t_critico * SE
        LI = media - ME
        LS = media + ME
        intervalos[f'{int(conf*100)}%'] = (LI, LS)

    # Guardar resultados
    resultados.append({
        'Mes': mes.capitalize(),
        'n': n,
        'Media': media,
        'Desviacion': desviacion,
        'IC_95%_Inferior': intervalos['95%'][0],
        'IC_95%_Superior': intervalos['95%'][1],
        'IC_99%_Inferior': intervalos['99%'][0],
        'IC_99%_Superior': intervalos['99%'][1],
    })

# Convertir resultados a DataFrame
df_resultados = pd.DataFrame(resultados)

# Mostrar los resultados
print(df_resultados)

# Opcional: Exportar los resultados a un archivo Excel o CSV
df_resultados.to_excel('resultados_intervalos_confianza_Santa_Ana.xlsx', index=False)

