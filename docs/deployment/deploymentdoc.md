# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Modelo propension al pago casas cobranzas.
- **Plataforma de despliegue:** El modelo sera desplegado en un servidor local utilizando el framework Flask.
- **Requisitos técnicos:** 
	Version de Python: 3.10.12
	Librerias: math 1.3.0, numpy 1.22.4, pandas 1.5.3, collections, csv, matplotlib 3.7.1, seaborn 0.12.2, google.colab, plotly 5.13.1, keras_tunner 1.3.5, sklearn 2.2.0, imblearn, keras 2.12.0, tensorflow 2.12.0, Flask 2.2.5, opencv-python 4.7.0.72
	Software: Windows 11 Home Single Language (Sistema operativo de 64 bits), Wing PRO 9
	Hardware: AMD Ryzen 7 4800H with Radeon Graphics 2.90 GHz, RAM 8,00 GB
- **Requisitos de seguridad:** Al tratarse de datos previamente estudiados y eliminados por la compañia por sensibilidad de la informacion, no es necesario su encriptación
- **Diagrama de arquitectura:**
  
  ![image](https://github.com/socampo737/tdsp_Victor_Santiago_M6/assets/125618328/35f90532-286b-41cd-810c-dd89450c5195)


## Código de despliegue

- **Archivo principal:** La aplicación diseñada se encuentra en el archivo denominado deployment_flask.py
- **Rutas de acceso a los archivos:** La ruta de acceso a los archivos es tdsp_Victor_Santiago_M6/docs/deployment


## Documentación del despliegue

- **Instrucciones de instalación:** Es indispensable para el correcto funcionamiento del aplicativo realizar la instalacion de todos las librerias y paquetes mencionados en los requisitos tecnicos.
- **Instrucciones de configuración:** Configurar el endpoint suministrado por el área de analítica en la plataforma de producción, con el fin de que devuelva la clasificación del cliente como pagados o no pagador.
- **Instrucciones de uso:** Para el despliegue en el servidor se pone en producción la aplicación creada en un servidor que ejecute Python y se llama el endpoint pasando como parametro las variables para el proceso de clasificación.
- **Instrucciones de mantenimiento:** El modelo sera actualizado con una periodicidad mensual mediante el envío de un archivo PKL con el modelo.
- **Ejemplo endpoint:** "http://127.0.0.1:5000/prediccion?er=EMP&po=NO&vt=S&cp=8029&ec=A&vf=N&vb=N&fb=202310&ed=NaN&cf=3&im=263.68&dt=1000.82&nl=12"
    
    donde
    er = ESCENARIO_RECOBRO
    po = PORTADO
    vt = VPT
    cp = CODIGO_POSTAL
    ec = ESTADO_CLIENTE
    vf = VAP_SCF
    vb = VAP_OB
    fb = FECHA_BPI
    ed = EDAD    CANTIDAD_FACTURAS = request.args.get("cf")
    IMPORTE_FACTURA    = request.args.get("im")
    DEUDA_TOTAL = request.args.get("dt")
    NUM_LINEAS_ACTIVAS = request.args.get("nl")
    ed = EDAD    
    cf = CANTIDAD_FACTURAS
    im = IMPORTE_FACTURA
    dt = DEUDA_TOTAL
    nl = NUM_LINEAS_ACTIVAS
