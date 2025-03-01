class Procesos:
    def __init__(self, nombre, tiempo_llegada, rafaga):
        self.nombre = nombre 
        self.tiempo_llegada = tiempo_llegada
        self.rafaga = rafaga
        self.tiempo_final = 0
        self.tiempo_inicio = 0
        self.prioridad = 0

    def set_prioridad(self):
        self.prioridad = input(f"Que prioridad quiere tener el proceso {self.nombre}: ") #Definir priridad por teclado

    def crear_proceso(self):
        self.nombre = input("Ingrese el nombre del proceso: ")
        self.tiempo_llegada = int(input("Ingrese el tiempo de llegada del proceso: "))
        self.rafaga = int(input("Ingrese la rafaga del proceso: "))

def crear_procesos():
    procesos = [] #Lista que me permitira almacenar los procesos
    cantidad_procesos = int(input("Cuantos procesos desea crear: ")) #Defino la cantidad de procesos que se crearan
    for i in range(cantidad_procesos): #Recorro la cantidad de procesos que se crearan
        proceso = Procesos("", 0, 0) #Creo un objeto de la clase Procesos
        proceso.crear_proceso() #Llamo al metodo crear_proceso
        procesos.append(proceso) #Agrego el proceso a la lista
    return procesos

def Fifo(procesos): #Funcion que implementa el algoritmo FIFO

    fifo_list = [] #Lista que me permitira almacenar los procesos

    for proceso in procesos: #Recorro la lista de procesos
        fifo_list.append(proceso) #Agrego el proceso a la lista

    tiempo_ejecucion = 0 #Me permite conocer el tiempo de ejecucion en le que me encuentro
    tiempo_espera = 0 #Me permite conocer el tiempo de espera de todos los procesos
    tiempo_sistema = 0 #Me permite conocer el tiempo de sistema de todos los procesos
    total = 0 #Me permite conocer el tiempo total de ejecucion de todos los procesos

    for proceso in fifo_list:
        total += proceso.rafaga #Calculo el tiempo total de ejecucion de todos los procesos  

    while (total > 0): #Mientras el tiempo total sea mayor a 0
        for proceso in fifo_list:
            if(tiempo_ejecucion >= proceso.tiempo_llegada): #Verifico si el proceso ya existe 
                    
                tiempo_espera += tiempo_ejecucion - proceso.tiempo_llegada #Calculo el tiempo de espera
                tiempo_ejecucion += proceso.rafaga #Calculo el tiempo de ejecucion

                #Estas me permiteran graficar el diagrama de Gantt
                proceso.tiempo_final = proceso.rafaga + tiempo_ejecucion #Calculo el tiempo final del proceso
                proceso.tiempo_inicio = tiempo_ejecucion - proceso.rafaga #Calculo el tiempo de inicio del proceso

                tiempo_sistema += tiempo_ejecucion - proceso.tiempo_llegada #Calculo el tiempo de sistema
                    
                total -= proceso.rafaga #Resto el tiempo de ejecucion del proceso al tiempo total
                    
                fifo_list.remove(proceso) #Elimino el proceso de la lista
                break

    print("El tiempo de espera es :", tiempo_espera/4) #Imprimo el tiempo de espera
    print("El tiempo de sistema es: ", tiempo_sistema/4) #Imprimo el tiempo de sistema

def SJF(procesos): #Funcion que implementa el algoritmo SJF

    sjf_list = [] #Lista que me permitira almacenar los procesos

    for proceso in procesos: #Recorro la lista de procesos
        sjf_list.append(proceso) #Agrego el proceso a la lista

    sjf_list.sort(key=lambda x: x.rafaga) #Ordeno la lista de procesos por rafaga

    Fifo(sjf_list) #Llamo a la funcion FIFO    

def Prioridad(procesos): #Funcion que implementa el algoritmo de prioridad
    for proceso in procesos: #Recorro la lista de procesos
        proceso.set_prioridad() #Defino la prioridad de cada proceso

    prioridad_list = [] #Lista que me permitira almacenar los procesos

    for proceso in procesos: #Recorro la lista de procesos
        prioridad_list.append(proceso) #Agrego el proceso a la lista

    prioridad_list.sort(key=lambda x: x.prioridad) #Ordeno la lista de procesos por rafaga

    Fifo(prioridad_list) #Llamo a la funcion

    #Pendo