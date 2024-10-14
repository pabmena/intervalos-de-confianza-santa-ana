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

### Análisis de Intervalos de Confianza (Punto 1):

Se calculan intervalos de confianza empíricos para las ventas diarias del supermercado 'Santa Ana' con niveles de confianza del 95% y 99%.

**Script utilizado:** `calculo_intervalos.py`.

### Pruebas ANOVA (Punto 2):

Se realizan pruebas ANOVA para comparar las ventas promedio de cinco supermercados: 'Santa Ana', 'La Floresta', 'Los Cedros', 'Palermo' y 'Córdoba'. La hipótesis nula es que las medias de ventas de todos los supermercados son iguales.

**Script utilizado:** `anova.py`.

### Pruebas de Hipótesis (Punto 3):

Se ejecutan pruebas de normalidad (Shapiro-Wilk), homogeneidad de varianza (Levene) y pruebas t entre las ventas de 'La Floresta' (mayor promedio de ventas) y 'Palermo' (menor promedio de ventas) para evaluar si la diferencia es significativa.

**Script utilizado:** `prueba_hipotesis.py`.

### Inferencia Bayesiana del Porcentaje de Morosidad (Punto 4):

Se realiza una inferencia bayesiana para determinar la distribución a posteriori del porcentaje de morosidad en los clientes a crédito, calculando su media y varianza.

**Script utilizado:** `inferencia_bayesiana.py`.

## Instrucciones de Ejecución

### Clonar el repositorio:

```bash
git clone https://github.com/pabmena/intervalos-de-confianza-santa-ana.git
cd intervalos-de-confianza-santa-ana

## Dependencias

Este proyecto requiere las siguientes dependencias:

- Python 3.x
- Pandas
- NumPy
- SciPy
- Matplotlib

Las dependencias se pueden instalar fácilmente utilizando el archivo `requirements.txt`. Para instalarlas, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt

### Sección de Ejecución de Scripts

```markdown
## Ejecución de Scripts

Sigue los siguientes pasos para ejecutar los scripts y obtener los resultados de cada punto:

### 1. Ejecutar el script para calcular los Intervalos de Confianza (Punto 1): Este script generará el archivo resultados_intervalos_confianza_Santa_Ana.xlsx, que contendrá los intervalos de confianza de las ventas diarias del supermercado 'Santa Ana'.

```bash
python calculo_intervalos.py

```markdown
### 2. Ejecutar el script para las pruebas ANOVA (Punto 2): Este script realizará la prueba ANOVA para determinar si hay diferencias significativas entre las ventas de los cinco supermercados. Los resultados se imprimirán en la consola.

```bash
python anova.py

```markdown
### 3. Ejecutar el script para las pruebas de hipótesis (Punto 3): Este script realiza pruebas de normalidad, homogeneidad de varianza y pruebas t entre 'La Floresta' y 'Palermo'. Los resultados se mostrarán en la consola.

```bash
python prueba_hipotesis.py

```markdown
### 4. Ejecutar el script para la inferencia bayesiana del porcentaje de morosidad (Punto 4): Este script calcula la distribución a posteriori del porcentaje de morosidad y genera un gráfico (distribucion_morosidad.png) con las distribuciones a priori y posteriori.

```bash
python inferencia_bayesiana.py

## Datos

El archivo `Datos_examen_final_18Co2024_Grupo6.xlsx` contiene los datos de ventas diarias de cinco supermercados: 'Santa Ana', 'La Floresta', 'Los Cedros', 'Palermo' y 'Córdoba'. Estos datos se usan en todos los análisis descritos.

## Resultados

- **Punto 1:** Los resultados de los intervalos de confianza para 'Santa Ana' se almacenan en el archivo `resultados_intervalos_confianza_Santa_Ana.xlsx`.
- **Punto 2 y Punto 3:** Los resultados de las pruebas ANOVA y de hipótesis se imprimen directamente en la consola.
- **Punto 4:** El gráfico de las distribuciones a priori y posteriori del porcentaje de morosidad se guarda en `distribucion_morosidad.png`.

## Consideraciones

- **Datos Sensibles:** Asegúrate de que el archivo `Datos_examen_final_18Co2024_Grupo6.xlsx` no contenga información sensible antes de compartir el proyecto.
- **Reproducibilidad:** Los scripts están diseñados para ser ejecutados secuencialmente y reproducir los resultados presentados en el informe.
- **Compatibilidad:** Verifica que las versiones de las librerías instaladas sean compatibles con las especificadas en `requirements.txt`.
