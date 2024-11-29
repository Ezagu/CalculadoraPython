class Calculadora:
    def __init__(self):
        self.__stack = []
        self.__elements_list = []

    def resultado(self, operation_RPN):
        """Resultado de la operación

        Args:
            operation_RPN (list(char)): lista de caracteres en polaca inversa que representa la operación
        """
        for element in operation_RPN:
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
            elif element == '*':
                pop1 = self.__stack.pop()
                pop2 = self.__stack.pop()
                self.__stack.append(pop2 * pop1)
            else:
                # El caracter es un numero
                self.__stack.append(int(element))
        return self.__stack.pop() if self.__stack else None

    def infijo_a_polaca_inversa(self, tokens):
        """Cambia lista de caracteres de infija a polaca inversa

        Args:
            tokens (list(char)): Operacion en infija.
        """

        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
        operadores = {'+', '-', '*', '/'}
        pila_operadores = []  # Pila para operadores
        salida = []  # Lista para la salida (RPN)

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

        # Vacía cualquier operador restante en la pila
        while pila_operadores:
            salida.append(pila_operadores.pop())

        return salida


c = Calculadora()
lista = ['8', '/', '2', '*', '(', '2', '+', '2', ')']
print(c.resultado(c.infijo_a_polaca_inversa(lista)))
