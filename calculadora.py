class Calculadora:
    def __init__(self):
        self.__stack = []
        self.__elements_list = []

    def get_element_list(self):
        """the element list for the operation"""
        return self.__elements_list

    def add_element(self, element):
        """add elements for the operation

        Args:
            element (str): element to introduce to operation.
        """
        self.__elements_list.append(element)

    def result(self):
        """Result of the operation"""

        for element in self.__elements_list:
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


c = Calculadora()
print(c.result())
c.add_element("4")
c.add_element("2")
c.add_element("*")
c.add_element("3")
c.add_element("+")
print(c.result())
print("PROBANDO GITHUBB")
