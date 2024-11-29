"""Interfaz gráfica de la calculadora"""
import tkinter as tk


class App:
    """Aplicación base"""

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        self.ventana.geometry("300x450")

    def iniciar(self):
        """Inicia la aplicación"""
        self.ventana.mainloop()
