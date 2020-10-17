import sys
from event import Event
from model import Model
from simulation import Simulation
import random as r
#Alumno: Luis Angel Rivera Sanchez
#Matricula: 2133042914
#               Ejercicios de la semana VII
#       Programar los algoritmos PI y PIF mostrados en el libro. Después en ambos algoritmos, agregar retardos aleatorios 
#a la propagación del mensaje de entre 1.0 y 5.0 unidades de tiempo (por ejemplo 1.0, 2.4, 4.89, 3.16, etc.).
#Deben pensar como agendar los eventos de transmisión con un tiempo aleatorio. 
#       Además cada proceso, al recibir un mensaje, debe imprimir el identificador de quién le ha enviado dicho mensaje.

#       Enviar los archivos de los programa PI y PIF con retardos aleatorios.

class Algorithm2(Model):
	def init(self):
		print("Nodo"+str(self.id)+": Inicializo algoritmo\n","\tVecinos =", self.neighbors)
		self.visited=False
		self.father=self.id
		self.count=1
	def receive(self,event):
		self.count -= 1
		print("Yo soy el Nodo %d y recibí mensaje del Nodo %d a los %f segundos." % (self.id, event.source, self.clock))
		if self.visited == False:
			print("Soy %d y recibo PRIMER mensaje de %d en tiempo t= %f" % (self.id,event.source,self.clock))
			self.visited=True
			self.father=event.source
			for t in self.neighbors:
				if t != self.father:
					newevent = Event("C",self.clock+r.uniform(1.0,5.0),t,self.id)
					self.transmit(newevent)
					self.count+=1
		if self.count == 0:
			print ("Nodo %d :Termino algoritmo con el padre = %d" % (self.id, self.father))
			newevent = Event("C",self.clock+r.uniform(1.0,5.0),self.father,self.id)
			self.transmit(newevent)


#Igualito a pi.py
if len(sys.argv) != 2:
	print ("Falta en nombre del archivo")
	raise SystemExit(1)
experiment = Simulation(sys.argv[1], 500)

for i in range(1,len(experiment.graph)+1):
	m = Algorithm2()
	experiment.setModel(m,i)
seed = Event("C",0.0,1,1)
experiment.init(seed)
experiment.run()
