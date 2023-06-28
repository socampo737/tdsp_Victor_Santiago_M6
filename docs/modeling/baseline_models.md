# Reporte del Modelo Baseline

## Descripción del modelo

Posterior a realizar la busqueda exaustiva de un modelo base en el estado del arte con ayuda de paginas como Hugging Face o interacciones con chat GPT, que cumpla con el objetivo de mejorar las tasas de cobro; decidimos utilizar un modelo base correspondiente a un Random Forest, que actualmente es utilizado en distintas verticales de negocio para clasificar clientes, arrojando resultados de exactitud lo suficientemente buenos para cumplir con el objetivo.

## Variables de entrada

Como variables de entrada se utilizan 16 variables tranformadas para el modelo, resaltando la conversion de variables categoricas a numericas.

## Variable objetivo

Como variable objetivo se utiliza el "TARGET" que traduce si se realizó o no el pago de la deuda.

## Evaluación del modelo

### Métricas de evaluación

Las metricas de evaluación utilizadas son el accuracy o exactitud.

### Resultados de evaluación

accuracy: 0.6835

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/a47fc71a-73cb-44bb-b015-db2d61685514)

## Conclusiones

La conclusion para este modelo base es que a pesar de tener un valor aceptable de exactutud, es necesario realizar una busqueda optima de hiperparametros que nos permita ejecutar con diferentes alternativas los modelos de redes neuronales y que al final a traves de la busqueda de los mejores hiperparametros, realizar la comparación entre las metricas del modelo base vs las metricas del modelo principal con los ajustes mencionados.

## Referencias

Proyecto de redes neuronales realizado en el modulo 5 del diplomado.
