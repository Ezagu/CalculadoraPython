class Operaciones:
    """Realiza las operaciones"""

    def __init__(self):
        self.__stack = []

    def resultado(self, operation):
        """Devuelve el resultado de la operación"""
        op = self.infijo_a_polaca_inversa(operation)

        #Si hubo un error en la conversion a polaca inversa, muestra syntax error
        if op == "SyntaxError":
            return op
        
        for element in op:
            try:
                if element == '+':
                    pop1 = self.__stack.pop()
                    pop2 = self.__stack.pop()
                    self.__stack.append(pop2 + pop1)
                elif element == '-':
                    pop1 = self.__stack.pop()
                    pop2 = self.__stack.pop()
                    self.__stack.append(pop2 - pop1)
                elif element == '/':
                    pop1 = self.__stack.pop()
                    pop2 = self.__stack.pop()
                    self.__stack.append(pop2 / pop1)
                elif element == 'x':
                    pop1 = self.__stack.pop()
                    pop2 = self.__stack.pop()
                    self.__stack.append(pop2 * pop1)
                else:
                    # El caracter es un numero
                    self.__stack.append(float(element))
            except:
                return "SyntaxError"

        result = self.__stack.pop() if self.__stack else None

        #Convierte el resultado a int si no tiene decimales
        if result != None and int(result) == result:
            result = int(result)

        return result

    def infijo_a_polaca_inversa(self, string):
        """Cambia strings de infija a polaca inversa"""
        tokens = self.str_to_list(string)
        precedencia = {'+': 1, '-': 1, 'x': 2, '/': 2}
        operadores = {'+', '-', 'x', '/'}
        pila_operadores = []  # Pila para operadores
        salida = []  # Lista para la salida (RPN)

        try:
            for token in tokens:
                if token in operadores:  # Es un operador
                    while (pila_operadores and pila_operadores[-1] in operadores and
                        precedencia[token] <= precedencia[pila_operadores[-1]]):
                        salida.append(pila_operadores.pop())
                    pila_operadores.append(token)
                elif token == '(':
                    pila_operadores.append(token)
                elif token == ')':
                    while pila_operadores and pila_operadores[-1] != '(':
                        salida.append(pila_operadores.pop())
                    pila_operadores.pop()  # Elimina el paréntesis izquierdo
                else:  # Es un numero
                    salida.append(token)
        except:
            return "SyntaxError"
        # Vacía cualquier operador restante en la pila
        while pila_operadores:
            salida.append(pila_operadores.pop())

        return salida
    
    def str_to_list(self, string):
        list_str = []
        caracteres = ['+', '-', 'x', '/', '(', ')']
        digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        current:str = ""
        for s in string:
            
            if s in caracteres:
                if current != "":
                    list_str.append(current)
                    current = ""
                list_str.append(s)
            elif s in digitos:
                current += s

        if current != "":
            list_str.append(current)

        return list_str
                

