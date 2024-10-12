# Análisis de Ventas y Pruebas de Hipótesis para Supermercado 'Santa Ana' y Otros

Este proyecto contiene el código fuente y los datos necesarios para analizar las ventas de varios supermercados, calcular intervalos de confianza empíricos para las ventas del supermercado 'Santa Ana' y realizar pruebas de hipótesis para comparar las ventas de diferentes sucursales.

## Contenido

- `calculo_intervalos.py`: Script principal para calcular los intervalos de confianza de las ventas mensuales del supermercado 'Santa Ana'.
- `anova.py`: Script para realizar pruebas ANOVA y determinar si existen diferencias significativas en las ventas de cinco supermercados.
- `prueba_hipotesis.py`: Script para realizar pruebas de normalidad, homogeneidad de varianza y pruebas t entre las ventas de 'La Floresta' y 'Palermo'.
- `Datos_examen_final_18Co2024_Grupo6.xlsx`: Archivo de datos con las ventas de los cinco supermercados, utilizado en todos los análisis.
- `resultados_intervalos_confianza_Santa_Ana.xlsx`: Resultados de los intervalos de confianza calculados para 'Santa Ana'.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar los scripts.
- `README.md`: Este archivo con instrucciones.

## Estructura del Proyecto

1. **Análisis de Intervalos de Confianza (Punto 1):**
   - Se calculan intervalos de confianza empíricos para las ventas diarias del supermercado 'Santa Ana' con niveles de confianza del 95% y 99%.
   - Script utilizado: `calculo_intervalos.py`.

2. **Pruebas ANOVA (Punto 2):**
   - Se realizan pruebas ANOVA para comparar las ventas promedio de cinco supermercados: 'Santa Ana', 'La Floresta', 'Los Cedros', 'Palermo', y 'Córdoba'. La hipótesis nula es que las medias de ventas de todos los supermercados son iguales.
   - Script utilizado: `anova.py`.

3. **Pruebas de Hipótesis (Punto 3):**
   - Se ejecutan pruebas de normalidad (Shapiro-Wilk), homogeneidad de varianza (Levene), y pruebas t entre las ventas de 'La Floresta' (mayor promedio de ventas) y 'Palermo' (menor promedio de ventas) para evaluar si la diferencia es significativa.
   - Script utilizado: `prueba_hipotesis.py`.

## Instrucciones de Ejecución

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/pabmena/intervalos-de-confianza-santa-ana.git
   cd intervalos-de-confianza-santa-ana

