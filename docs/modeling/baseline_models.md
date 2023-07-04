# Reporte del Modelo Baseline

## Descripción del modelo

Posterior a realizar la búsqueda exhaustiva de un modelo base en el estado del arte con ayuda de páginas como Hugging Face o interacciones con chat GPT, que cumpla con el objetivo de mejorar las tasas de cobro, no fue posible tener resultados de coincidencias con estas características; por ello decidimos utilizar un modelo base correspondiente a un Random Forest, que actualmente es utilizado por el equipo de trabajo en distintas verticales de negocio (ventas, retenciones, etc) para clasificar clientes, arrojando resultados de exactitud lo suficientemente buenos para cumplir con el objetivo.

## Variables de entrada

Como variables de entrada se utilizan 16 variables transformadas para el modelo, resaltando la conversión de variables categóricas a numéricas.

CANTIDAD_FACTURAS - float64

IMPORTE_FACTURA - float64

ESCENARIO_RECOBRO - int64

DEUDA_TOTAL - float64

PORTADO - int64

VPT - int64

CODIGO_POSTAL - float64

NUM_LINEAS_ACTIVAS - float64

ESTADO_CLIENTE - int64

VAP_SCF - int64

VAP_OB - int64

BAJA - int64

0_30 - float64

31_50 - float64

51_65 - float64

MAYOR_65 - float64

## Variable objetivo

Como variable objetivo se utiliza el "TARGET" que traduce si se realizó o no el pago de la deuda.

## Evaluación del modelo

### Métricas de evaluación

Las métricas de evaluación utilizadas son el accuracy o exactitud.

### Resultados de evaluación

accuracy: 0.799

![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/a06a1ad3-5fe1-4fdc-bb17-9fcd4acf2aff)


## Conclusiones

La conclusión para este modelo base es que a pesar de tener un valor sobresaliente de exactitud, es necesario realizar una búsqueda optima de hiperparámetros que nos permita ejecutar con diferentes alternativas el modelo Random Forest. Así con el valor del modelo base (0.799) vs el modelo con los mejores hiperparámetros realizar la comparación directa en la exactitud con el modelo principal.

## Referencias

Algoritmos y modelos utilizados actualmente en la compañía (Random Forest).
Proyecto de redes neuronales realizado en el módulo 5 del diplomado.
