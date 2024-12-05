class Historial:
    def guardar_operacion(self, operacion, resultado):
        """Guarda una operacion en el archivo \"historial.csv\""""
        with open("historial.csv", "a", encoding="utf-8") as file:
            file.write(f"{operacion},{resultado}\n")

    def get_operaciones(self):
        """Devuelve un diccionario con las operaciones anteriores, Key = Operacion, Value = Resultado"""
        dicc = {}
        with open("historial.csv", "r", encoding="utf-8") as file:
            for linea in file:
                linea = linea.strip()
                datos = linea.split(",")
                dicc[datos[0]] = datos[1]
        return dicc
    
    def borrar_historial(self, events = None):
        """Elimina el historial de operaciones"""
        print("Historial borrado")
        with open("historial.csv", "w", encoding="utf-8") as file:
            #Al abrir el archivo en modo "w" y no hacer nada, se borra el contenidos
            pass