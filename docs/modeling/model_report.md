# Reporte del Modelo Final

## Descripción del Problema

El problema a solucionar se basa en la optimización y mejora de la recuperación de impagos y clientes con una edad antigua en la deuda que está constituida entre los 0 a 120 días, de acuerdo a su fase (Cobro amistoso – Recobro no amistoso – Fase 3 – Retención). El contexto en el que se encuentra dicho proyecto son los Recobros carterizados que se realizan vía contact center con estrategias de omnicanalidad (Telefonía, Chat, redes sociales, canales de autoconsumo, etc. Con la implementacion del modelo de redes neuronales se lograra tener una cartera diferenciada y segmentada por los clientes con mayor propensión al pago con el fin de diseñar estrategias que permitan optimizar la gestión de los recobros

## Descripción del Modelo

Como resultado de tener los mejores hiperparametros, utilizamos una red neuronal secuencial con una primera capa densa de 9 neuronas para los datos de entrada, dos capas densas intermedias de 352 y 224 neuronas, y por ultimo una capa densa de salida.

## Evaluación del Modelo

El resultado de la metrica utilizada es un accuracy: 0.6935

## Conclusiones y Recomendaciones

Posterior a implementar el base line con optimizadores y cambios en el numero de capas aleatorio, el modelo evoluciona con la utilizacion de KerasTuner que nos ayuda a evaluar los modelos con hiperparametros diferente como los son el learning rate, las neuronas, las epocas, entre otros. Asi logramos tener despues de una cantidad de iteraciones significativas, el mejor modelo con el cual se lograra tener la mayor exactitud cercana al 70% y perdida cercana al 54%.

## Referencias

Proyecto de redes neuronales realizado en el modulo 5 del diplomado.
