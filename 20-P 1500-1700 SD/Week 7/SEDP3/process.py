# This file contains the description of the "Process" class
# first version in python2, by R.Marcelin-Jimenez (11.11.10)
# support of concurrent algorithms using multiports by R.Marcelin-Jimenez (27.09.20)
# support of weighted graphs by M.Lopez-Chavira (27.09.20)
# python3-style getters by I.Martinez-Vargas (27.09.20)

""" An instance of "Process" represents the active entity that lives at each
node of the communications graph, aka network. """

# -----------------------------------------#---------------------------------------------
class Process:                             # Descends from "Object" (default)
    """ Process attributes: "neighbors", "weights", "engine", "id" & "models", 
    contains constructor and getters in python3-style, as well as the 
    methods "setModel()", "setTime()", "receive()" & "transmit()". """


    def __init__(self, neighbors, weights, engine, id):
        """ Builds an instance of "Process", including its list of neighbor nodes,
        the weights of the links to its neighbors, the events engine, its id & a list
        to allocate each of its working models. """

        self.__neighbors = neighbors
        self.__weights = weights
        self.__engine = engine
        self.__id = id
        self.__models = []
		
    def setModel(self, model, port=0):
        """ asocia al proceso con el modelo que debe ejecutar y viceversa """
        self.__models.insert(port, model)
        model.setProcess(self, self.__neighbors, self.__weights, self.__id, port)
        model.init()

    @property
    def neighbors(self):
        return self.__neighbors

    @property
    def weights(self):
        return self.__weights

    @property
    def engine(self):
        return self.__engine

    @property
    def id(self):
        return self.__id

    @property
    def models(self):
        return self.__models

    def setTime(self, time, port=0):
        """ actualiza el valor del reloj local """	
        model = self.__models[port]
        model.setTime(time)
		
    def receive(self, event, port=0):
        """ consulta a su modelo para decidir la atencion de un evento """
        model = self.__models[port]
        model.receive(event)

    def transmit(self, event):	
        """ invoca al motor para insertar un evento en su agenda """
        self.__engine.insertEvent(event)
		

        
