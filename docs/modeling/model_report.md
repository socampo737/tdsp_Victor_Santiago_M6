# Reporte del Modelo Final

## Descripción del Problema

El problema a solucionar se basa en la mejora de la recuperación de impagos sobre clientes con una edad antigua en la deuda. El contexto en el que se encuentra dicho proyecto son los Recobros carterizados que se realizan vía contact center con estrategias de omnicanalidad (Telefonía, Chat, redes sociales, canales de autoconsumo, etc. Con la implementación del modelo de redes neuronales se logrará tener una cartera diferenciada y segmentada por los clientes con mayor propensión al pago con el fin de diseñar estrategias que permitan optimizar la gestión de los recobros.

## Descripción del Modelo

Se realizarán los siguientes ajustes en busca de obtener el mejor resultado ejecutando diferentes alternativas en cuanto a modelos predictivos.

- Se determina realizar una red neuronal secuencial que a través de la búsqueda de los mejores hiperparámetros (learning rate, capas, neuronas) nos permita evidenciar el mejor resultado posible de exactitud.
- Adicional al punto anterior se busca el numero óptimo de épocas que acompañará la optimización de la red neuronal.
- Como resultado de tener los mejores hiperparámetros, el resumen del modelo es una red neuronal secuencial con una primera capa densa de 24 neuronas para los datos de entrada, dos capas densas intermedias de 64 y 288 neuronas y por último una capa densa de salida para un total de 21017 parámetros.


## Evaluación del Modelo

El resultado de la métrica utilizada es un accuracy: 0.7122

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/094fa434-dd33-4216-a9e7-8ab0b0f71393)

El resultado de la métrica utilizada es un accuracy: 0.6108

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/ef4687e7-9f2e-4477-bdf0-baf11dc1375e)


## Conclusiones y Recomendaciones

- Como podemos observar el resultado de la exactitud en el modelo de redes neuronales con los mejores hiperparametros, es inferior en un 9% respecto al modelo Random Forest ejecutado como modelo base, lo que nos indica que en este caso se presenta el principio de parsimonia, debido a que la teoría más simple de ejecutar tiene mayor probabilidad de ser la correcta.

- De acuerdo con el desarrollo del ejercicio donde es primordial ejecutar diferentes modelos con el fin de encontrar el resultado optimo. Recomendamos buscar en los casos que aplique, los mejores hiperparámetros para customizar cada modelo en busca de conseguir los máximos resultados de las métricas a evaluar.

## Referencias

Proyecto de redes neuronales realizado en el módulo 5 del diplomado.
