"""Interfaz gráfica de la calculadora"""
import tkinter as tk
from operaciones import Operaciones
from historial import Historial


class App:
    """Aplicación base"""

    def __init__(self):

        self.operaciones = Operaciones()
        self.historial = Historial()

        #Ventana
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        self.ventana.config(bg="black")
        self.ventana.resizable(False, False)

        #Historial
        self.historial_button = tk.Menubutton(self.ventana, text="Historial", bg="black", fg="white", font="Arial 8 italic")
        self.historial_button.grid(row=0,column=0)

        self.menu_historial = tk.Menu(self.historial_button, tearoff=0)
        self.historial_button.config(menu=self.menu_historial)
        self.historial_button.bind("<Button-1>", self.actualizar_historial)

        #Display
        self.display = tk.Frame(self.ventana, bg="gray8")
        self.display.grid(row=1,column=0,columnspan=4, pady=10)

        self.operacion_actual = tk.Entry(self.display, width=21, justify="right", bg="gray8", fg="white", bd=0, font="Arial 16")
        self.operacion_actual.grid(row=0, column=0, pady=10, padx=10)

        self.result = tk.Label(self.display, text="", font="Arial 10", bg="gray8", fg="gray")
        self.result.grid(row=1,column=0, sticky="e", padx=10, pady=3)

        #Botones
        caracteres_botones = ('(', ')', 'C', '<-', '7', '8', '9', '/', '4', '5', '6', 'x', '1', '2', '3', '+', '.', '0', '=', '-')
        index = 0

        for i in range(5):
            i += 2
            for j in range(4):
                caracter = caracteres_botones[index]
                index += 1
                boton = tk.Button(self.ventana, text=caracter, width=8,height=3, command= lambda c=caracter:self.agregar_caracter(c), bg="gray22", fg="white")
                boton.grid(row=i, column=j, pady=5, padx=5)

                #Botones especiales
                if caracter == 'C':
                    boton.config(command=self.borrar_display)
                elif caracter == '<-':
                    boton.config(command=self.eliminar_caracter)
                elif caracter == '=':
                    boton.config(command=self.mostrar_resultado)

    def agregar_caracter(self, caracter):
        """Agrega caracteres al display"""
        #Si antes hubo un systax error, lo elimina
        if self.operacion_actual.get() == "SyntaxError":
            self.borrar_display()
        
        self.operacion_actual.config(fg="white")
        self.operacion_actual.insert(tk.END, caracter)

        self.mostrar_resultado_actual()

    def agregar_operacion(self, operacion):
        """Pone una operacion en el display"""
        self.borrar_display()
        self.operacion_actual.config(fg="white")
        self.operacion_actual.insert(0, operacion)
        self.mostrar_resultado_actual()

    def borrar_display(self):
        """Borra todo el contenido del display"""
        self.operacion_actual.delete(0,tk.END)
        self.result.config(text="")

    def eliminar_caracter(self):
        """Elimina el ultimo caracter del display"""
        texto_actual = self.operacion_actual.get()
        self.operacion_actual.delete(len(texto_actual)-1, tk.END)
        self.mostrar_resultado_actual()

    def mostrar_resultado(self):
        """Muestra el resultado en pantalla"""
        operacion = self.operacion_actual.get()
        if not self.hay_operacion(operacion):
            return
        resultado = self.operaciones.resultado(operacion)
        self.borrar_display()
        self.operacion_actual.insert(0, resultado)

        #Si hay SyntaxError lo muestra de color rojo
        if resultado != "SyntaxError":
            self.operacion_actual.config(fg="green")
            self.historial.guardar_operacion(operacion, resultado)
        else:
            self.operacion_actual.config(fg="red")

    def mostrar_resultado_actual(self):
        """Muestra el resultado de la operacion actual"""
        operacion = self.operacion_actual.get()
        resultado = self.operaciones.resultado(operacion)

        if not self.hay_operacion(operacion):
            self.result.config(text="")
            return
                
        if resultado != "SyntaxError": #Si no es un syntaxerror muestra el resultado actual
            self.result.config(text=resultado)
        else:
            self.result.config(text="")

    def hay_operacion(self, operacion):
        """Verifica si al menos hay un operador"""
        operadores = ['+', '-', 'x', '/']
        cant_operaciones = 0
        for s in operacion:
            if s in operadores:
                cant_operaciones += 1
        return not cant_operaciones == 0
    
    def actualizar_historial(self, events = None):
        """Actualiza las operaciones en el menu"""
        self.menu_historial.delete(0, tk.END)
        self.menu_historial.add_command(label="Borrar historial", command=self.historial.borrar_historial)
        dicc = self.historial.get_operaciones()
        for op,res in dicc.items():
            self.menu_historial.add_command(label=op, accelerator=f"={res}", command=lambda op=op:self.agregar_operacion(op))

    def iniciar(self):
        """Inicia la aplicación"""
        self.ventana.mainloop()
