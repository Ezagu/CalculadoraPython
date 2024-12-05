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

if __name__ == "__main__":
    h = Historial()
    h.guardar_operacion("2+2", "4")
    h.guardar_operacion("3x6", "18")
    print("Operaciones:", h.get_operaciones())
    h.borrar_historial()
    print("Operaciones:", h.get_operaciones())
    h.guardar_operacion("3x6", "18")
    print("Operaciones:", h.get_operaciones())