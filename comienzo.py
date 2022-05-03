"""
lectura de archivo de una maquina de registro, 
primera linea:
	User		WorkId	CardNo	Date		Time		IN/OUT	EventCode
	'Gabriel	1		'NULL	2021-05-20	00:10:49	IN		30038

-este es un programa para visualizar los horarios de los empleados 
"""

from generar_archivos import generar_archivos
import datetime 
from datetime import timedelta

FIN_ARCHIVO = ""
class usuario:
	def __init__(self,nombre):
		self.nombre = nombre 
		self.dias_presente = {}
		self.cantidad_horas = []
		self.puesto_trabajo = []
		self.precioXhora = 210

	def agregar_puesto(self,puesto):
		if len(self.puesto_trabajo) <= 2:
			self.puesto_trabajo.append(puesto)
		else:
			print("no se puede agregar mas puestos de trabajo(max=2)")

	
	def mostrar_dias_presente(self):
		dato_ant=""
		cant= 0

		with open("usuarios/"+self.nombre+".csv","r") as f:
			for i in f: 
				dato = i.rstrip("\n").split(",")  
				print(dato)
				if dato_ant != "":
					diferencia_horaria(dato[1],dato[2],dato_ant[1],dato_ant[2])
				dato_ant = dato

################################################
#def distancia_horaria(dato1,dato2):
	
################################################
def diferencia_horaria(fecha_2,hora_2,fecha_1,hora_1):
	#fecha2 = datetime.timedelta(hours=23,minutes=22)
	year2 , month2 ,day2 = fecha_2.rstrip("\r").split("-")
	year1, month1, day1 = fecha_1.rstrip("\r").split("-") 

	hora , minutos, segundos = hora_1.rstrip("\n").split(":")
	comp1= datetime.datetime(year=int(year1),month=int(month1),day=int(day1),hour=int(hora),minute=int(minutos),second=int(segundos))
	hora , minutos, segundos = hora_2.rstrip("\n").split(":")
	comp2= datetime.datetime(year=int(year2),month=int(month2),day=int(day2),hour=int(hora),minute=int(minutos),second=int(segundos))
	n=0
	unDia = timedelta(hours=13)
	if unDia > comp2-comp1 :
		print("primera marca:",comp1,"\nsegunda marca:",comp2)
		print(comp2-comp1)
		n=1
	else:
		print("supera 13hs")
################################################
def leerdato(archivo):
	linea = archivo.readline()
	lista = []
	if linea != FIN_ARCHIVO:
		lista = linea.split(",") 
		#print(lista)
	else:
		lista =["","",""]
	return  lista
################################################
def mostra_lista(lista):
	e =1
	for i in lista:
		print(e,"-",i)
		e +=1
################################################
def main(): 

	lista_usuarios = generar_lista("recordList.csv")
	mostra_lista(lista_usuarios)
	num_usuario = int(input("ingrese un num de usuario"))
	x = usuario(lista_usuarios[num_usuario-1]) 
	x.mostrar_dias_presente()

################################################################################################
################################################################################################
################################################################################################

main()
otro = input("fin del programa")

