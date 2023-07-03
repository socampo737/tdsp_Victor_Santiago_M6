# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

- Número total de observaciones: 7339

- Q variables: 25

- Tipo de variables: categóricas, numéricas y fechas

- Valores faltantes:

EMAIL                 2195

EDAD                   252

PERMANENCIA           7273

VPT                    267

FECHA_BPI             4171

TIPO_DOCUMENTO        5659

CODIGO_POSTAL           33

FEU                   6169

Es necesario evaluar el porcentaje de nulos sobre el total general de cada variable con el fin de ejecutar imputación de datos o eliminación de la variable sobre los datos. Sin embargo es relevante mencionar que sin importar la técnica aplicada (imputación o eliminación), se utilizaran las 7339 observaciones. 

Toda la información relacionada se encuentra en los scripts de Python.

## Resumen de calidad de los datos

A pesar de encontrar en el 32% de las variables valores nulos o faltantes que oscilan entre el 1% y el 98%, se utilizaran las 7339 observaciones, debido al preprocesamiento de los datos. Con este resultado podemos inferir que la calidad de los datos es media. 

Una de las acciones tomadas para los valores extremos u outliers están basadas en los resultados de los boxplot, donde a través de las estadísticas de las variables como la varianza, mediana, media y la desviación estándar, se normalizan los valores y se realizan las imputaciones correspondientes.

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/b38747af-5572-4a17-bd1b-e463d7688f89)


![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/f1186d90-a2cb-4b05-ada9-ac62145f7fed)


![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/5784a5d8-bbbd-4098-8531-d59aae5d658e)


## Variable objetivo

La variable objetivo a estimar corresponde al "TARGET" y es una variable de tipo numérica discreta que corresponde a 1 que identifica si la acción es pago y 0 si la acción es no pago. El gráfico y análisis se evidencian en el script de Python.

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/7895aeb7-dd19-4eae-945f-83148115beda)

## Variables individuales

Se relacionan los resultados relevantes respecto a las estadísticas de las variables, la visualización de las mismas y las transformaciones realizadas para la correcta ejecución de los modelos.

- Variable estado de cliente representada en un diagrama circular

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/2e5d0e32-44fb-427b-9d31-5d1fe0f4f89a)

- Variable cantidad de facturas representada en un histograma de frecuencias ejecutado con seaborn

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/5a140480-a5a7-4b72-ba76-728149b74368)

Es relevante mencionar que en los puntos anteriores se evidencias otros gráficos como el boxplot, los diagramas de barras horizontales y las estadísticas de las variables.

Adicional a ello se relacionan algunas transformaciones

- En la variable FECHA_BPI los valores diferentes a NaN indican que hay fecha de baja, los valores NaN indica que no. Por lo tanto crearemos una nueva variable numérica llamada BAJA:

Si FECHA_BPI = NaN => BAJA=0
Sino => BAJA=1

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/e298f318-3b9b-4c44-a8e7-68ec88569deb)

- Al observar la variable ESTADO_CLIENTE se evidencian dos clases, por lo tanto usaremos el valor 1 para la clase A y el 0 para la clase B.

- Respecto a la variable edad, es necesario transformarla a valores numéricos, por lo tanto se realiza la creación de variables dummies.

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/241532f8-a121-4a6b-ba62-dc9b861058d4)

Por ultimo se relaciona las variables transformadas y analizadas

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/591bf08a-83d2-4cf7-a4f4-4cfc2e06815c)


## Ranking de variables

Se relaciona el ranking de variables posterior a realizar las transformaciones y eliminación de variables no aportantes por datos faltantes o por la alta cardinalidad en las variables. Adicional a ello a través de los resultados en los splits levels arrojados por el modelo Random Forest que se refieren a la profundidad del árbol de decisión, es decir, cuántos niveles o capas de divisiones se realizan antes de llegar a las hojas del árbol, se determina la importancia de las variables mediante el cálculo de la ganancia promedio de importancia de todas las variables en todos los árboles del bosque. Esta medida se basa en el criterio de ganancia de información, que mide cuánta reducción en la impureza se obtiene al dividir los datos utilizando una variable en particular.

 1   TARGET
 
 2   DEUDA_TOTAL
 
 3   ESCENARIO_RECOBRO
 
 4   IMPORTE_FACTURA
 
 5   CANTIDAD_FACTURAS
 
 6   CODIGO_POSTAL
 
 7   BAJA
 
 8   EDAD
 
 9   PORTADO
 
 10  NUM_LINEAS_ACTIVAS
 
 11  VPT
 
 12  ESTADO_CLIENTE
 
 13  VAP_OB
 
 14  VAP_SCF 

## Relación entre variables explicativas y variable objetivo

Como se observa en el gráfico de correlación, las variables explicativas no poseen una correlación positiva o negativa fuerte respecto a la variable objetivo (TARGET), esto nos indica que el valor máximo de correlación positiva es 0,08 entre las variables VAP_OB vs TARGET y el valor máximo de correlación negativa es -0,28 entre las variables CANTIDAD_FACTURAS vs TARGET.

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/97223a0d-611c-4c50-b696-9b73d7b1c7b8)

