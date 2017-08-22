from pila import *
import sys

class Nodo:
	def __init__(self , valor):
		self.valor = valor
		self.izquierda = None
		self.derecha = None

class ArbolPosFijo:        

        def buscarOperador(self, caracter):
                if (caracter == '+' or caracter == '-' or caracter == '*'
                        or caracter == '/'):
                        return True
                else:
                        return False

        def construirArbol(self, posfijo):
                pilaOperador = Pila()
                #Recorra todo el string 
                for char in posfijo :

                        # si NO es operador lo apila
                        if not self.buscarOperador(char):
                                arbol = Nodo(char)
                                pilaOperador.apilar(arbol)

                        # Operador
                        else:
                                # desapila dos nodos
                                arbol = Nodo(char)
                                arbol1 = pilaOperador.desapilar()
                                arbol2 = pilaOperador.desapilar()

                                # los convierte en hijos
                                arbol.derecha = arbol1
                                arbol.izquierda = arbol2

                                # Anade nuevo arbol a la pila
                                pilaOperador.apilar(arbol)

                # Al final el ultimo elemento de la pila sera el arbol
                arbol = pilaOperador.desapilar()
                return arbol

        def evaluar(self, arbol):
            if arbol.valor=='+':
                return self.evaluar(arbol.izquierda)+self.evaluar(arbol.derecha)
            if arbol.valor=='-':
                return self.evaluar(arbol.izquierda)-self.evaluar(arbol.derecha)
            if arbol.valor=='*':
                return self.evaluar(arbol.izquierda)*self.evaluar(arbol.derecha)
            if arbol.valor=='/':
                try:
                        return self.evaluar(arbol.izquierda)/self.evaluar(arbol.derecha)
                except ZeroDivisionError:
                        print("No esta permitida la division entre cero")
                        sys.exit()
            return float(arbol.valor)


class Main:        
        obj = ArbolPosFijo()
        print("Ingrese los valores del arbol en PosFija separados por un espacio:")
        valorIngresado = input() #Python 2.x raw_input(), 3.x input() 
        aux = valorIngresado.split(" ")
        r = obj.construirArbol(aux)
        print ("El valor resultante es: ")
        print(obj.evaluar(r))
