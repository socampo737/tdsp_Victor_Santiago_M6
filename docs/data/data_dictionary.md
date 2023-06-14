# Diccionario de datos

## Base de datos cobranza

**Base de datos donde se actualizan las gestiones de cobro a los clientes y donde se encuentran los datos sociodemograficos de los mismos.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| CUST_CODE | Identificador único para cada cliente | float64 | 1/N | UNAL_Cobros.csv |
| NUMERO_FACTURA | Numero identificador de factura emitida | object | A/Z | UNAL_Cobros.csv |
| FECHA_ENVIO | Fecha envío de la factura | object | 15/12/2022 - 01/04/2023 | UNAL_Cobros.csv |
| CANTIDAD_FACTURAS | Indica cuantas facturas lleva emitidas el cliente | int64 | 1/9 | UNAL_Cobros.csv |
| FECHA_DEVOLUCION | Fecha en la que se produce la devolución de la factura | object | 20/08/2021 - 01/04/2023 | UNAL_Cobros.csv |
| IMPORTE_FACTURA | Importe total de la factura original con impuestos incluidos | float64 | 1/N | UNAL_Cobros.csv |
| FECHA_FACTURA | Fecha de la factura a cobrar | object | 20/08/2021 - 01/04/2023 | UNAL_Cobros.csv |
| ESCENARIO_RECOBRO | Indica el segmento en el que se encuentra el cliente | object | PER/FU/EMP | UNAL_Cobros.csv |
| DEUDA_TOTAL | Deuda todal del cliente sobre sus facturas | float64 | 1/N | UNAL_Cobros.csv |
| PORTADO | Indica si el cliente ha tenido portabilidad | object | SI/NO | UNAL_Cobros.csv |
| EMAIL | Dominio de correo electronico del cliente | object | infinito | UNAL_Cobros.csv |
| EDAD | Cantidad de años del cliente expresado en rangos | object | 0/MAYOR 65 | UNAL_Cobros.csv |
| FECHA CARGA | Fecha de carga a la base de datos de gestión | object | 15/12/2022 - 01/04/2023 | UNAL_Cobros.csv |
| IMPORTE PRODUCTO | Importe pagado por el cliente en caso de aplicar | float64 | 1/N | UNAL_Cobros.csv |
| TARGET | Descripción de pago o impago | object | SI/NO | UNAL_Cobros.csv |
| PERMANENCIA | Meses de permanencia por contrato de cliente | object | compromiso 12/24 | UNAL_Cobros.csv |
| VPT | Indica si tiene algun concepto de terminal venta a plazos | object | SI/NO | UNAL_Cobros.csv |
| FECHA_BPI | Fecha indicada para baja de cliente | float64 | 202301/202305 | UNAL_Cobros.csv |
| TIPO_DOCUMENTO | Tipo de documento del cliente | object | CIF/NIF | UNAL_Cobros.csv |
| CODIGO_POSTAL | Código postal donde reside el cliente | float64 | 1001/52006 | UNAL_Cobros.csv |
| NUM_LINEAS_ACTIVAS | Cantidad de lineas activas adquiridas por el cliente | int64 | 0/91 | UNAL_Cobros.csv |
| ESTADO_CLIENTE | Indica si el cluente esta activo o inactivo | object | A/B | UNAL_Cobros.csv |
| VAP_SCF | Indica si tiene algun concepto de venta a plazos cubierta por otra entidad | object | N/S | UNAL_Cobros.csv |
| VAP_OB | Indica si tiene algun concepto de venta a plazos cubierta por Orange Bank | object | N/S | UNAL_Cobros.csv |
| FEU | Indica si existe cobertura por el fondo europeo | object | N/S | UNAL_Cobros.csv |



- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.