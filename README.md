# Análisis de Ventas y Pruebas de Hipótesis para Supermercado 'Santa Ana' y Otros

Este proyecto contiene el código fuente y los datos necesarios para analizar las ventas de varios supermercados, calcular intervalos de confianza empíricos para las ventas del supermercado 'Santa Ana', realizar pruebas de hipótesis para comparar las ventas de diferentes sucursales y realizar una inferencia bayesiana sobre el porcentaje de morosidad en los clientes a crédito.

## Contenido

- `calculo_intervalos.py`: Script principal para calcular los intervalos de confianza de las ventas mensuales del supermercado 'Santa Ana'.
- `anova.py`: Script para realizar pruebas ANOVA y determinar si existen diferencias significativas en las ventas de cinco supermercados.
- `prueba_hipotesis.py`: Script para realizar pruebas de normalidad, homogeneidad de varianza y pruebas t entre las ventas de 'La Floresta' y 'Palermo'.
- `inferencia_bayesiana.py`: Script para realizar la inferencia bayesiana del porcentaje de morosidad en los clientes a crédito.
- `Datos_examen_final_18Co2024_Grupo6.xlsx`: Archivo de datos con las ventas de los cinco supermercados, utilizado en todos los análisis.
- `resultados_intervalos_confianza_Santa_Ana.xlsx`: Resultados de los intervalos de confianza calculados para 'Santa Ana'.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar los scripts.
- `README.md`: Este archivo con instrucciones.

## Estructura del Proyecto

1. **Análisis de Intervalos de Confianza (Punto 1):**

   - Se calculan intervalos de confianza empíricos para las ventas diarias del supermercado 'Santa Ana' con niveles de confianza del 95% y 99%.
   - **Script utilizado:** `calculo_intervalos.py`.

2. **Pruebas ANOVA (Punto 2):**

   - Se realizan pruebas ANOVA para comparar las ventas promedio de cinco supermercados: 'Santa Ana', 'La Floresta', 'Los Cedros', 'Palermo' y 'Córdoba'. La hipótesis nula es que las medias de ventas de todos los supermercados son iguales.
   - **Script utilizado:** `anova.py`.

3. **Pruebas de Hipótesis (Punto 3):**

   - Se ejecutan pruebas de normalidad (Shapiro-Wilk), homogeneidad de varianza (Levene) y pruebas t entre las ventas de 'La Floresta' (mayor promedio de ventas) y 'Palermo' (menor promedio de ventas) para evaluar si la diferencia es significativa.
   - **Script utilizado:** `prueba_hipotesis.py`.

4. **Inferencia Bayesiana del Porcentaje de Morosidad (Punto 4):**

   - Se realiza una inferencia bayesiana para determinar la distribución a posteriori del porcentaje de morosidad en los clientes a crédito, calculando su media y varianza.
   - **Script utilizado:** `inferencia_bayesiana.py`.

## Instrucciones de Ejecución

### Clonar el repositorio:

```bash
git clone https://github.com/pabmena/intervalos-de-confianza-santa-ana.git
cd intervalos-de-confianza-santa-ana

### Instalar las dependencias: Utiliza el archivo requirements.txt para instalar las dependencias necesarias
pip install -r requirements.txt

#### Ejecutar los scripts:

Punto 1: Intervalos de Confianza 
#Ejecuta el siguiente comando para calcular los intervalos de confianza de las ventas mensuales del supermercado 'Santa Ana':
python calculo_intervalos.py # Este script generará el archivo resultados_intervalos_confianza_Santa_Ana.xlsx con los resultados.

Punto 2: Pruebas ANOVA 
#Ejecuta el siguiente comando para realizar las pruebas ANOVA:
python anova.py #Los resultados se mostrarán en la consola.

Punto 3: Pruebas de Hipótesis
#Ejecuta el siguiente comando para realizar las pruebas de hipótesis entre 'La Floresta' y 'Palermo':
python prueba_hipotesis.py # Los resultados se mostrarán en la consola.

Punto 4: Inferencia Bayesiana del Porcentaje de Morosidad
#Ejecuta el siguiente comando para realizar la inferencia bayesiana y generar el gráfico de las distribuciones a priori y posteriori:
python inferencia_bayesiana.py # Este script mostrará en la consola los parámetros de la distribución posteriori y generará el archivo distribucion_morosidad.png con el gráfico.

# Requisitos
Python 3.x instalado en tu sistema 
# Las librerías de Python especificadas en requirements.txt.

Datos # El archivo Datos_examen_final_18Co2024_Grupo6.xlsx contiene los datos de ventas diarias de cinco supermercados: 'Santa Ana', 'La Floresta', 'Los Cedros', 'Palermo' y 'Córdoba'. Estos datos se usan en todos los análisis descritos.

Resultados
# Punto 1: Los resultados de los intervalos de confianza para 'Santa Ana' se almacenan en el archivo resultados_intervalos_confianza_Santa_Ana.xlsx.
## Punto 2 y Punto 3: Los resultados de las pruebas ANOVA y de hipótesis se imprimen directamente en la consola.
#### Punto 4: El gráfico de las distribuciones a priori y posteriori del porcentaje de morosidad se guarda en distribucion_morosidad.png.

Consideraciones
# Datos Sensibles: Asegúrate de que el archivo Datos_examen_final_18Co2024_Grupo6.xlsx no contenga información sensible antes de compartir el proyecto.
## Reproducibilidad: Los scripts están diseñados para ser ejecutados secuencialmente y reproducir los resultados presentados en el informe.
### Compatibilidad: Verifica que las versiones de las librerías instaladas sean compatibles con las especificadas en requirements.txt.