import io


FIN_ARCHIVO = ["","","","","","",""]
FIN = ""
def leerdato(archivo):
	linea = archivo.readline()
	lista = []
	if linea != FIN:
		lista = linea.split(",") 
		#print(lista)
	else:
		lista =FIN_ARCHIVO
	return  lista[0] ,lista[3] ,lista[4]
########################################

def actualizacion(archivo):
	usuario, fecha, hora = leerdato(archivo)
	lista_usuarios  = []
	i = 1 
	while usuario:
		if usuario not in lista_usuarios:
			apertura(usuario)
			lista_usuarios.append(usuario) 
		escritura_archivo(usuario,fecha,hora)
		usuario, fecha, hora = leerdato(archivo)

	return lista_usuarios

"""
def diferencia_horaria(fecha_2,hora_2,fecha_1,hora_1):
	#fecha2 = datetime.timedelta(hours=23,minutes=22)
	year2 , month2 ,day2 = fecha_2.rstrip("\r").split("-")
	year1, month1, day1 = fecha_1.rstrip("\r").split("-")
	print(year2,month2,day2,hora_2)
	print(year1,month1,day1,hora_2,"\n")"""

################################################################################
def escritura_archivo(usuario,fecha,hora):
	archivo = open("usuarios/"+usuario+".csv","r+")
	archivo.seek(len(archivo.read()))
	archivo.write(usuario+","+fecha+","+hora+"\n")
	archivo.close()



########################################
def apertura(nombre):
	archivo = open("usuarios/"+nombre+".csv","w")
	archivo.close()

########################################
def generar_archivos(archivo):
	maestro = open(archivo,"r")
	usuarios = actualizacion(maestro)
	maestro.close()
	return usuarios
generar_archivos("recordList.csv")
"""
>>> fecha2= datetime.timedelta(hours=23,minutes=22)
>>> fecha = datetime.timedelta(hours=19,minutes =15)

>>> otra = fecha2 - fecha
>>> print otra
4:07:00
>>> fecha2= datetime.timedelta(hours=23,minutes=23)
>>> otra = fecha2 - fecha}
"""