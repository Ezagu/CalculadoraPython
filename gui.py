"""Interfaz gráfica de la calculadora"""
import tkinter as tk
from operaciones import Operaciones
from historial import Historial


class App:
    """Aplicación base"""

    def __init__(self):

        self.operaciones = Operaciones()
        self.historial = Historial()

        self.operadores = ['+', '-', 'x', '/']
        self.digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        self.ventana.config(bg="black")
        self.ventana.resizable(False, False)

        self.historial_button = tk.Menubutton(self.ventana, text="Historial", bg="black", fg="white", font="Arial 8 italic")
        self.historial_button.grid(row=0,column=0)

        self.menu_historial = tk.Menu(self.historial_button, tearoff=0)
        self.historial_button.config(menu=self.menu_historial)
        self.historial_button.bind("<Button-1>", self.actualizar_historial)

        self.display = tk.Frame(self.ventana, bg="black")
        self.display.grid(row=1,column=0,columnspan=4)

        self.current_operation = tk.Entry(self.display, width=18, justify="right", bg="black", fg="white", bd=0, font="Arial 16")
        self.current_operation.grid(row=0, column=0, pady=10, padx=10)

        self.result = tk.Label(self.display, text="", padx=10, font="Arial 10", bg="black", fg="gray")
        self.result.grid(row=1,column=0, sticky="e")

        self.abrir_parentesis = tk.Button(self.ventana, text="(", width=5, height=2, command= lambda: self.agregar_caracter('('), bg="gray22", fg="white")
        self.abrir_parentesis.grid(row=2, column=0,pady=5)
        self.cerrar_parentesis = tk.Button(self.ventana, text=")", width=5, height=2, command= lambda: self.agregar_caracter(')'), bg="gray22", fg="white")
        self.cerrar_parentesis.grid(row=2, column=1)
        self.borrar = tk.Button(self.ventana, text="C", width=5, height=2, command=self.borrar_display, bg="gray22", fg="white")
        self.borrar.grid(row=2,column=2)
        self.eliminar = tk.Button(self.ventana, text="<-", width=5, height=2, command=self.eliminar_caracter, bg="gray22", fg="white")
        self.eliminar.grid(row=2,column=3)

        self.siete = tk.Button(self.ventana, text="7", width=5, height=2, command= lambda: self.agregar_caracter('7'), bg="gray22", fg="white")
        self.siete.grid(row=3, column=0, pady=5)
        self.ocho = tk.Button(self.ventana, text="8", width=5, height=2, command= lambda: self.agregar_caracter('8'), bg="gray22", fg="white")
        self.ocho.grid(row=3, column=1)
        self.nueve = tk.Button(self.ventana, text="9", width=5, height=2, command= lambda: self.agregar_caracter('9'), bg="gray22", fg="white")
        self.nueve.grid(row=3, column=2)
        self.dividir = tk.Button(self.ventana, text="/", width=5, height=2, command= lambda: self.agregar_caracter('/'), bg="gray22", fg="white")
        self.dividir.grid(row=3, column=3)

        self.cuatro = tk.Button(self.ventana, text="4", width=5, height=2, command= lambda: self.agregar_caracter('4'), bg="gray22", fg="white")
        self.cuatro.grid(row=4, column=0, pady=5)
        self.cinco = tk.Button(self.ventana, text="5", width=5, height=2, command= lambda: self.agregar_caracter('5'), bg="gray22", fg="white")
        self.cinco.grid(row=4, column=1)
        self.seis = tk.Button(self.ventana, text="6", width=5, height=2, command= lambda: self.agregar_caracter('6'), bg="gray22", fg="white")
        self.seis.grid(row=4, column=2)
        self.multiplicar = tk.Button(self.ventana, text="x", width=5, height=2, command= lambda: self.agregar_caracter('x'), bg="gray22", fg="white")
        self.multiplicar.grid(row=4, column=3)

        self.uno = tk.Button(self.ventana, text="1", width=5, height=2, command= lambda: self.agregar_caracter('1'), bg="gray22", fg="white")
        self.uno.grid(row=5, column=0, pady=5)
        self.dos = tk.Button(self.ventana, text="2", width=5, height=2, command= lambda: self.agregar_caracter('2'), bg="gray22", fg="white")
        self.dos.grid(row=5, column=1)
        self.tres = tk.Button(self.ventana, text="3", width=5, height=2, command= lambda: self.agregar_caracter('3'), bg="gray22", fg="white")
        self.tres.grid(row=5, column=2)
        self.sumar = tk.Button(self.ventana, text="+", width=5, height=2, command= lambda: self.agregar_caracter('+'), bg="gray22", fg="white")
        self.sumar.grid(row=5, column=3)

        self.punto = tk.Button(self.ventana, text=".", width=5, height=2, command= lambda: self.agregar_caracter('.'), bg="gray22", fg="white")
        self.punto.grid(row=6, column=0,pady=5)
        self.cero = tk.Button(self.ventana, text="0", width=5, height=2, command= lambda: self.agregar_caracter('0'), bg="gray22", fg="white")
        self.cero.grid(row=6, column=1)
        self.igual = tk.Button(self.ventana, text="=", width=5, height=2, bg="gray22", fg="white", command=self.mostrar_resultado)
        self.igual.grid(row=6, column=2)
        self.menos = tk.Button(self.ventana, text="-", width=5, height=2, command= lambda: self.agregar_caracter('-'), bg="gray22", fg="white")
        self.menos.grid(row=6, column=3)

    def agregar_caracter(self, caracter):
        """Agrega caracteres al display"""
        #Si antes hubo un systax error, lo elimina
        if self.current_operation.get() == "SyntaxError":
            self.borrar_display()
        
        self.current_operation.config(fg="white")
        self.current_operation.insert(tk.END, caracter)
        if caracter in self.digitos:
            self.current_resultado()
        elif caracter in self.operadores:
            self.result.config(text="")

    def agregar_operacion(self, operacion):
        """Pone una operacion en el display"""
        self.borrar_display()
        self.current_operation.config(fg="white")
        self.current_operation.insert(0, operacion)
        self.current_resultado()

    def borrar_display(self):
        """Borra todo el contenido del display"""
        self.current_operation.delete(0,tk.END)
        self.result.config(text="")

    def eliminar_caracter(self):
        """Elimina el ultimo caracter del display"""
        texto_actual = self.current_operation.get()
        self.current_operation.delete(len(texto_actual)-1, tk.END)
        self.current_resultado()

    def mostrar_resultado(self):
        """Muestra el resultado en pantalla"""
        operacion = self.current_operation.get()
        if not self.hay_operacion(operacion):
            return
        resultado = self.operaciones.resultado(operacion)
        self.borrar_display()
        self.current_operation.insert(0, resultado)

        #Si hay SyntaxError lo muestra de color rojo
        if resultado != "SyntaxError":
            self.current_operation.config(fg="green")
            self.historial.guardar_operacion(operacion, resultado)
        else:
            self.current_operation.config(fg="red")

    def current_resultado(self):
        """Muestra el resultado de la operacion actual"""
        operacion = self.current_operation.get()

        if not self.hay_operacion(operacion):
            self.result.config(text="")
            return
        
        resultado = self.operaciones.resultado(operacion)
        if resultado != "SyntaxError": #Si no es un syntaxerror muestra el resultado actual
            self.result.config(text=resultado)

    def hay_operacion(self, operacion):
        """Verifica si al menos hay un operador"""
        cant_operaciones = 0
        for s in operacion:
            if s in self.operadores:
                cant_operaciones += 1
        return not cant_operaciones == 0
    
    def actualizar_historial(self, events = None):
        """Actualiza las operaciones en el menu"""
        self.menu_historial.delete(0, tk.END)
        self.menu_historial.add_command(label="Borrar historial", command=self.historial.borrar_historial)
        dicc = self.historial.get_operaciones()
        for op,res in dicc.items():
            print(op,res)
            self.menu_historial.add_command(label=op, accelerator=f"={res}", command=lambda op=op:self.agregar_operacion(op))

    def iniciar(self):
        """Inicia la aplicación"""
        self.ventana.mainloop()
