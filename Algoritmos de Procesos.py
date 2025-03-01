import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import pygame
from ttkthemes import ThemedTk

        
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmos de Procesos")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.config(bg="black")

        self.label = tk.Label(self.root, text="Algoritmos de Procesos", font=("Arial", 20), bg="black", fg="white")
        self.label.pack(pady=20)

        self.button_iniciar = tk.Button(self.root, text="Iniciar", font=("Arial", 15), bg="black", fg="white", command=self.abrir_grafica)
        self.button_iniciar.pack(pady=20)

        self.button_salir = tk.Button(self.root, text="Salir", font=("Arial", 15), bg="black", fg="white", command=self.root.quit)
        self.button_salir.pack(pady=20)

    def abrir_grafica(self):
        self.root.withdraw()  # Oculta la ventana principal
        
        # Crea una nueva instancia de la clase 'Grafica'
        self.grafica_window = Grafica(self.root)


class Grafica:
    def __init__(self, root):
        self.root = tk.Toplevel(root)  # Crea una nueva ventana de tipo Toplevel, es decir, una ventana secundaria
        self.root.title("Graficar")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.config(bg="black")

        self.label = tk.Label(self.root, text="Ingrese la cantidad de procesos que desea ejecutar (máximo 10)", font=("Arial", 20), bg="black", fg="white")
        self.label.pack(padx=10, pady=10)

        self.num_procesos = tk.Entry(self.root, font=("Arial", 20))
        self.num_procesos.pack(padx=10, pady=10)

        self.button_ejecutar = tk.Button(self.root, text="Ejecutar Algoritmo", font=("Arial", 15), bg="black", fg="white", command=self.ejecutar_algoritmo)
        self.button_ejecutar.pack(pady=20)

        self.button_volver = tk.Button(self.root, text="Volver al inicio", font=("Arial", 15), bg="black", fg="white", command=self.volver_inicio)
        self.button_volver.pack(pady=20)

    def ejecutar_algoritmo(self):
        try:
            num_procesos = int(self.num_procesos.get())  # Obtener el número de procesos
            if num_procesos <= 10:
                self.mostrar_animacion(num_procesos)  # Ejecutar animación
            else:
                print("Por favor, ingrese un número de procesos válido (máximo 10).")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    def mostrar_animacion(self, num_procesos):
        # Aquí puedes agregar el código para la animación de los algoritmos
        print(f"Ejecutando animación con {num_procesos} procesos.")  # Ejemplo de mensaje

        # Puedes utilizar matplotlib o cualquier otro medio para la animación aquí
        plt.figure()
        plt.plot(np.random.rand(10))
        plt.title(f"Animación con {num_procesos} procesos")
        plt.show()

    def volver_inicio(self):
        self.root.destroy()  # Cierra la ventana de 'Grafica'
        self.root.master.deiconify()  # Muestra la ventana principal de nuevo
    

if __name__ =="__main__":
    root = ThemedTk(theme="arc")
    app = App(root)
    root.mainloop()