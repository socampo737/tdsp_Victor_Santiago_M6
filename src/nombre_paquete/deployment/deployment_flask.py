import numpy as np
import pandas as pd
from flask import Flask, request
import joblib
import os

import sys

#print('This is error output', file=sys.stderr)
#print('This is standard output', file=sys.stdout)

def escalado(x, maximo):
	return x / maximo



app = Flask(__name__)

modelo_final = joblib.load('modelo_final.pkl')


@app.route("/prueba")
def prueba():
	return("Funcionando ... Ver. 1.0")


@app.route("/prediccion")
def prediccion():
	# LEER LOS PARAMETROS
	#http://127.0.0.1:5000/prediccion?er=EMP&po=NO&vt=S&cp=8029&ec=A&vf=N&vb=N&fb=202310&ed=NaN&cf=3&im=263.68&dt=1000.82&nl=12	
	
	#er = ESCENARIO_RECOBRO
	#po = PORTADO
	#vt = VPT
	#cp = CODIGO_POSTAL
	#ec = ESTADO_CLIENTE
	#vf = VAP_SCF
	#vb = VAP_OB
	#fb = FECHA_BPI
	#ed = EDAD
	#cf = CANTIDAD_FACTURAS
	#im = IMPORTE_FACTURA
	#dt = DEUDA_TOTAL
	#nl = NUM_LINEAS_ACTIVAS
	
	ESCENARIO_RECOBRO = request.args.get("er")
	PORTADO = request.args.get("po")
	VPT = request.args.get("vt")
	CODIGO_POSTAL = request.args.get("cp")
	ESTADO_CLIENTE = request.args.get("ec")
	VAP_SCF	= request.args.get("vf")
	VAP_OB = request.args.get("vb")
	FECHA_BPI = request.args.get("fb")
	EDAD = request.args.get("ed")
	CANTIDAD_FACTURAS = request.args.get("cf")
	IMPORTE_FACTURA	= request.args.get("im")
	DEUDA_TOTAL = request.args.get("dt")
	NUM_LINEAS_ACTIVAS = request.args.get("nl")
	
	#ESCENARIO_RECOBRO = "EMP"
	#PORTADO = "NO"
	#VPT = "S"
	#CODIGO_POSTAL = 8029
	#ESTADO_CLIENTE = "A"
	#VAP_SCF	= "N"
	#VAP_OB = "N"
	#FECHA_BPI = "202310"
	#EDAD = "NaN"
	#CANTIDAD_FACTURAS = 3
	#IMPORTE_FACTURA	= 263.68
	#DEUDA_TOTAL = 1000.82 
	#NUM_LINEAS_ACTIVAS = 12 
	
	#http://127.0.0.1:5000/prediccion?er=EMP&po=NO&vt=S&cp=8029&ec=A&vf=N&vb=N&fb=202310&ed=NaN&cf=3&im=263.68&dt=1000.82&nl=12	
	#http://127.0.0.1:5000/prediccion?er=EMP&po=NO&vt=S&cp=8029&ec=A&vf=N&vb=N&fb=202310&ed=NaN&cf=3&im=263.68&dt=1000.82&nl=12
	
	# TRATAMIENTO DE VACIOS
	if CODIGO_POSTAL == "NaN":
		CODIGO_POSTAL = 28
	else:
		CODIGO_POSTAL = int(CODIGO_POSTAL)
		
	if IMPORTE_FACTURA == "NaN":
		IMPORTE_FACTURA = 71.99
	else:
		IMPORTE_FACTURA = float(IMPORTE_FACTURA)
		
	if DEUDA_TOTAL == "NaN":
		DEUDA_TOTAL = 71.99
	else:
		DEUDA_TOTAL = float(DEUDA_TOTAL)
			
	if CANTIDAD_FACTURAS == "NaN":
		CANTIDAD_FACTURAS = 2
	else:
		CANTIDAD_FACTURAS = int(CANTIDAD_FACTURAS)
	
	if NUM_LINEAS_ACTIVAS == "NaN":
		NUM_LINEAS_ACTIVAS = 1
	else:
		NUM_LINEAS_ACTIVAS = int(NUM_LINEAS_ACTIVAS)
	
	if EDAD == "NaN":
		EDAD = 65
	else:
		EDAD = int(EDAD)
	
	
	# TRANSFORMACIONES
	if ESCENARIO_RECOBRO == "PER" or ESCENARIO_RECOBRO == "FU":
		ESCENARIO_RECOBRO = 1
	else:
		ESCENARIO_RECOBRO = 0 
		
	if PORTADO == "NO" or PORTADO == "N" or PORTADO == "BAJAS_I" or PORTADO == "BAJAS_II" or PORTADO == "N/A":
		PORTADO = 0
	else:
		PORTADO = 1
		
	if VPT == "SI":
		VPT = 1
	else:
		VPT = 0
	
	if ESTADO_CLIENTE == "A":
		ESTADO_CLIENTE = 1
	else:
		ESTADO_CLIENTE = 0
		
	if VAP_SCF == "SI":
		VAP_SCF = 1
	else:
		VAP_SCF = 0
		
	if VAP_OB == "SI":
		VAP_OB = 1
	else:
		VAP_OB = 0
		
	if VAP_OB == "SI":
		VAP_OB = 1
	else:
		VAP_OB = 0
		
	if FECHA_BPI == "NaN":
		BAJA = 0
	else:
		BAJA = 1 
		
	E_0_30 = E_31_50 = E_51_65 = E_MAYOR_65 = 0
	
	if EDAD < 30:
		E_0_30 = 1
		
	if 31 <= EDAD <= 50:  	
		E_31_50 = 1
		
	if 51 <= EDAD <= 65:
		E_51_65 = 1
	
	if EDAD > 65: 
		E_MAYOR_65 = 1
	
	if CANTIDAD_FACTURAS < 1: 
		CANTIDAD_FACTURAS = 1
	elif CANTIDAD_FACTURAS > 3.5:
		CANTIDAD_FACTURAS = 3.5
		
	if IMPORTE_FACTURA < 0:
		IMPORTE_FACTURA = 0
	elif IMPORTE_FACTURA > 314.24:
		IMPORTE_FACTURA = 314.24
	
	if DEUDA_TOTAL < 0:
		DEUDA_TOTAL = 0
	elif DEUDA_TOTAL > 628.83:
		DEUDA_TOTAL = 	628.83
	
	if NUM_LINEAS_ACTIVAS < 0:
		NUM_LINEAS_ACTIVAS = 0
	elif NUM_LINEAS_ACTIVAS >2.5:
		NUM_LINEAS_ACTIVAS = 2.5
	
	
	# ESCALADO DE VARIABLES
	CANTIDAD_FACTURAS = escalado(CANTIDAD_FACTURAS, 3.5)
	IMPORTE_FACTURA = escalado(IMPORTE_FACTURA, 314.24)
	DEUDA_TOTAL = escalado(DEUDA_TOTAL, 628.83)
	CODIGO_POSTAL = escalado(CODIGO_POSTAL, 52)
	NUM_LINEAS_ACTIVAS = escalado(NUM_LINEAS_ACTIVAS, 2.5)
	

	# CREACION DEL DATASET DE TEST
	X = np.array([CANTIDAD_FACTURAS, IMPORTE_FACTURA, ESCENARIO_RECOBRO,
	       DEUDA_TOTAL, PORTADO, VPT, CODIGO_POSTAL, NUM_LINEAS_ACTIVAS,
	       ESTADO_CLIENTE, VAP_SCF, VAP_OB, BAJA, E_0_30, E_31_50, E_51_65, E_MAYOR_65])
	
	X = X.reshape(1, -1)

	df_X = pd.DataFrame(data=X,
			  columns = ['CANTIDAD_FACTURAS', 'IMPORTE_FACTURA', 'ESCENARIO_RECOBRO',
				     'DEUDA_TOTAL', 'PORTADO', 'VPT', 'CODIGO_POSTAL', 'NUM_LINEAS_ACTIVAS',
				     'ESTADO_CLIENTE', 'VAP_SCF', 'VAP_OB', 'BAJA', '0_30', '31_50', '51_65','MAYOR_65'])
	

	y_pred = modelo_final.predict(df_X)[0]

	return(str(y_pred))
	
	# X = [3., 263.68, 0., 628.83, 0., 0., 8.029, 2.5, 1., 0., 0., 1., 0., 0., 1., 0.]
	# print("X : ", ' '.join(list(map(lambda x: str(x), X))))
	# return("SI")



if __name__ == "__main__":
	app.run(debug=True)
	#app.run(host='0.0.0.0', port=5000, debug=True)

