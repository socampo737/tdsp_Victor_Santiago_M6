# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

- Número total de observaciones: 7339

- Q variables: 25

- Tipo de variables: categoricas, numericas y fechas

- Valores faltantes:

EMAIL                 2195

EDAD                   252

PERMANENCIA           7273

VPT                    267

FECHA_BPI             4171

TIPO_DOCUMENTO        5659

CODIGO_POSTAL           33

FEU                   6169

Es necesario evaluar el porcentaje de nulos sobre el total general de cada variable con el fin de ejecutar imputación de datos o eliminación de la variable sobre los datos. Sin embargo es relevante mencionar que sin importar la técnica aplicada (imputación o eliominación), se utilizaran las 7339 observaciones. 

Toda la informacion relacionada se encuentra en los script de Python

## Resumen de calidad de los datos

A pesar de encontrar en el 32% de las variables valores nulos o faltantes que oscilan entre el 1% y el 98%, se utilizaran las 7339 observaciones, debido al preprocesamiento de los datos. Con este resultado podemos inferir que la calidad de los datos es media. 

Una de las acciones tomadas para los valores extremos u outliers estan basadas en los resultados de los boxplot, donde a traves de las estadisticas de la variables como la varianza y la desviacion estandar, se normalizan los valores y se realizan las imputaciones correspondientes.

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/b38747af-5572-4a17-bd1b-e463d7688f89)

## Variable objetivo

La variable objetivo a estimar corresponde al "TARGET" y es una variable de tipo numerica discreta que corresponde a 1 que identifica si la accion es pago y 0 si la accion es no pago. El grafico y analisis se evidencian en el script de Python.

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/7895aeb7-dd19-4eae-945f-83148115beda)


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

## Relación entre variables explicativas y variable objetivo

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/97223a0d-611c-4c50-b696-9b73d7b1c7b8)

