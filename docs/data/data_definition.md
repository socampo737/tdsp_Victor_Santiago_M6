# Definición de los datos

## Origen de los datos

- [ ] Los datos se extraen desde un data warehouse que a través de ETL´s se actualiza la información con una periodicidad diaria, permitiendo observar los movimientos en las carteras correspondientes a pagos, deudas, deducciones, días de mora, entre otras variables importantes. La forma de obtener los datos es subir una actualización con la periodicidad anteriormente mencionada a google drive.

## Especificación de los scripts para la carga de datos

- [ ] El script utilizado para la carga de datos se denomina "data_acquisition" 

## Referencias a rutas o bases de datos origen y destino

- [ ] La ruta donde se encuentra el archivo o la base de datos es "ruta_archivo= '/content/drive/MyDrive/UNAL_Cobros_I.csv'"

### Rutas de origen de datos

- [ ] Especificar la estructura de los archivos de origen de los datos.
El dataset cuyo tamaño es de 0.98MB contiene 7339 filas y 25 variables donde inicialmente los datos se encuentran en formato .csv que posteriormente se convierte en un dataframe de pandas
- [ ] Describir los procedimientos de transformación y limpieza de los datos.
Los procedimientos de transformación y limpieza están basados en entender en primera instancia las distribuciones, el rango de valores que tienen las variables y si hay o no datos faltantes o inconsistente; allí es implementada la estadística a través de histogramas de frecuencia, diagramas de barras, diagramas circulares, boxplot, entre otros. Sin embargo, con el fin de complementar la información para realizar todos los procesos, se identifican los tipos de variables existentes en el conjunto de datos (categóricas, numéricas y de fecha) para así obtener los conteos, los mínimos, los máximos, los promedios, las desviaciones estándar, la moda y los cuartiles; medidas que dependientes del tipo de variables son aplicadas al conjunto de datos. Por último, se debe realizar la validación del porcentaje de faltantes y de datos inconsistentes para identificar si las variables deben ser eliminadas o si se debe imputar datos de acuerdo con las estadísticas mencionadas anteriormente.

