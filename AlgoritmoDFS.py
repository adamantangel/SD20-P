import sys
from event import Event
from model import Model
from simulation import Simulation
import random as r
f = open("dfs.txt","a")

#Alumno: Luis Angel Rivera Sanchez
#Matricula: 2133042914

#               Ejercicios de la semana VIII
#       CONTINUAMOS SIMULANDO LA ONDA
#       

class dfs(Model):
	

	def init(self):#Es lo primero llamado
		#print("Nodo"+str(self.id)+": Inicializo algoritmo\n","\tVecinos =", self.neighbors)
		self.visited = False
		self.father = self.id
		self.sin_visitar = self.neighbors.copy() #Nodos que le falta visitar.
		self.mis_hijos = self.neighbors.copy()

	def continue_exploration(self):
		if not self.sin_visitar: #Lista esta vacia
			if(self.father != self.id):
				msg = Event("REGRESA", self.clock+1.0, self.father, self.id)
				print("N: %d"%self.id, " P: %d"%self.father," H:",self.mis_hijos, file = f)
				self.transmit(msg)
				
				#print("\nSoy Nodo %d con ->\nVecinos: " %self.id,self.neighbors,"\nPadre: %d" % self.father)
				
			else:
				#print("\nSoy Nodo Inicial %d con ->\nVecinos: " % self.id,self.neighbors,"\nPadre: %d" % self.father)
				print("NI: %d"%self.id, " P: %d"%self.father," H:",self.mis_hijos,"\n", file = f)

		#Si hay algo en la lista
		else:
			msg = Event("DESCUBRE", self.clock+1.0, self.sin_visitar[0], self.id)
			self.sin_visitar.remove(self.sin_visitar[0])
			self.transmit(msg)


	#La función recibe un evento, un mensaje.
	def receive(self,event):

		
		if(event.name == "DESCUBRE"):

			if(self.visited):
				msg = Event("RECHAZO",self.clock+1.0,event.source,self.id)
				self.transmit(msg)
			else:
				self.visited = True
				self.father = event.source
				if(self.father in self.sin_visitar):	self.sin_visitar.remove(self.father)
				if(self.father in self.mis_hijos):	self.mis_hijos.remove(self.father)
				#print(self.neighbors)
				self.continue_exploration()


		if(event.name == "RECHAZO" or event.name == "REGRESA"):	
			if(event.name == "RECHAZO" and event.source in self.mis_hijos):
				self.mis_hijos.remove(event.source)			
			self.continue_exploration()



#requiere que le agreguemos el archivo de grafo al llamarlo.
if len(sys.argv) != 2:
	print ("Falta en nombre del archivo")
	raise SystemExit(1)

versiones = (1,3,6)

print("KEY: N_0 = Nodo Inicial, N = Nodo, P = Padre, H = Hijos", file=f)

for k in versiones:


	experiment = Simulation(sys.argv[1], 500)

	for i in range(1,len(experiment.graph)+1):
		m = dfs()
		experiment.setModel(m,i)

	#No encontre ponerlo en un for >:()
	print("\nIniciamos con el nodo %d como semilla" % k, file = f)
	seed = Event("DESCUBRE",0.0,k,k)
	experiment.init(seed)
	experiment.run()
