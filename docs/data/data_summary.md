# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

Resumen general de los datos
Número total de observaciones: 7339
Variables: 25
Tipo de variables: categoricas, numericas y fechas
Valores faltantes: existen valores faltantes en las variables EMAIL 2195, EDAD 252, PERMANENCIA 7273, VPT 267, FECHA_BPI 4171, TIPO_DOCUMENTO 5659, CODIGO_POSTAL 33, FEU 616,

Toda la informacion relacionada se encuentra en los script de Python

## Resumen de calidad de los datos

Las acciones tomadas para los valores extremos, outliers y demas estan basadas en los resultados del boxplot, donde a traves de la desviacion estandar se realizan las imputaciones.

## Variable objetivo

La variable objetivo a estimar corresponde al "TARGET" y es una variable de tipo numerica discreta, su grafico y analisis se encuentran en el script.

## Ranking de variables

Se relaciona el ranking de variables posterior a realizar las transformaciones y eliminacion de variables no aportantes por datos faltantes o por la alta cardinalidad en las variables como se puede observar en el grafico de correlacion visualizado en el script.

N°  Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   CANTIDAD_FACTURAS | 7339 non-null | int64  
 1   IMPORTE_FACTURA   | 7335 non-null | float64
 2   ESCENARIO_RECOBRO | 7339 non-null | int64  
 3   DEUDA_TOTAL       | 7339 non-null | float64
 4   PORTADO           | 7339 non-null | int64  
 5   EDAD              | 7087 non-null | object 
 6   TARGET            | 7339 non-null | int64  
 7   VPT               | 7339 non-null | int64  
 8   CODIGO_POSTAL     | 7339 non-null | float64
 9   NUM_LINEAS_ACTIVAS| 7339 non-null | int64  
 10  ESTADO_CLIENTE    | 7339 non-null | int64  
 11  VAP_SCF           | 7339 non-null | int64  
 12  VAP_OB            | 7339 non-null | int64  
 13  BAJA              | 7339 non-null | int64  

