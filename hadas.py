# -*- coding: utf-8 -*-
#Tipos de hadas del juego

#objeto aldeano
class aldeano:
	"""Creando los aldeanos"""
	
	def __init__(self, vida = 10, capacidad = 8):
		self.vida = vida
		self.capacidad = capacidad #revisar
	
	def __str__(self):
		return "Datos del aldeano: \nvida: " + str(self.vida) + "\ncapacidad restante: " + str(self.capacidad)
	
	#el aldeano tambien puede luchar 
	def luchar(self,herida):
		self.vida -= herida #para prueba, esta linea es temporal
		if self.vida > 0:
			print "sigue luchando"
		else:
			print "ha muerto"
	
	#funcion para recolectar piedras, oro, comida, etc
	def recolectar(self):
		if self.capacidad > 0:
			print "recoger"
			self.capacidad -= 1
		else:
			print "El aldeano no puede cargar mas"
	
	def construir(self):
		print "construyendo"


class guerrero():
	
	def __init__(self, vida):
		self.vida = vida
	
	def luchar(self,herida):
		self.vida -= herida #para prueba, esta linea es temporal
		if self.vida > 0:
			print "sigue luchando"
		else:
			print "ha muerto"
	
# definimos los tipos de guerreros

class hada_fuego(guerrero):
	
	def __init__(self, vida, arma):
		guerrero.__init__(self, vida)
		self.arma = arma
		print "el arma que se utiliza es " + self.arma
		#DEFINIR ARMAS --- PROXIMAMENTE
	
	def poderes(self):
		pass #DEFINIR PODERES
		
class 


#probando las hadas aldeanos
jeremtail = aldeano()

def aldeanos():
	print """ingrese una opcion: 
	1. luchar
	2. recolectar
	3. construir
	4. ver datos
	5. salir"""
	funcion = input()
	if funcion == 1:
		jeremtail.luchar(2)
		print jeremtail.vida
		aldeanos()
	elif funcion == 2:
		jeremtail.recolectar()
		aldeanos()
	elif funcion == 3:
		jeremtail.construir()
		aldeanos()
	elif funcion == 4:
		print jeremtail
		aldeanos()
	else:
		pass

aldeanos()
