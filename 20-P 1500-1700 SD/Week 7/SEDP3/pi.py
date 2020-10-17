import sys
from event import Event
from model import Model
from simulation import Simulation
import random as r

#Alumno: Luis Angel Rivera Sanchez
#Matricula: 2133042914
#		Ejercicios de la semana VII
#	Programar los algoritmos PI y PIF mostrados en el libro. Después en ambos algoritmos, agregar retardos aleatorios 
#a la propagación del mensaje de entre 1.0 y 5.0 unidades de tiempo (por ejemplo 1.0, 2.4, 4.89, 3.16, etc.).
#Deben pensar como agendar los eventos de transmisión con un tiempo aleatorio. 
#	Además cada proceso, al recibir un mensaje, debe imprimir el identificador de quién le ha enviado dicho mensaje.

#	Enviar los archivos de los programa PI y PIF con retardos aleatorios.




class Algorithm1(Model):
	def init(self):
		self.visited=False
	def receive(self, event):
		#Event source is 
		print("Soy el Nodo %d y recibo mensaje de Nodo %d y recíbi mensaje a los: %f segundos desde el inicio. :)" % (self.id,event.source,self.clock))
		if self.visited == False:
			self.visited= True
			for t in self.neighbors:
				delay = r.uniform(1.0,5.0)	#Crea mis retardos 
				#print("Hubo un retardo de %f" % delay)
				newevent=Event("Yo soy %d y te mado saludos!" % self.id, self.clock+delay,t,self.id)
				self.transmit(newevent)

if len(sys.argv) !=2:
	print("Please supply a file name")
	raise SystemExit(1)
experiment = Simulation(sys.argv[1], 500)

for i in range(1,len(experiment.graph)+1):
	m = Algorithm1()
	experiment.setModel(m, i)

seed = Event("C",0.0,1,1)
experiment.init(seed)
experiment.run()
