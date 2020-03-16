from automata import *
import numpy as np


class LexicAnalyzer:
    def __init__(self, automata, inputString):
        #Atributos del analizador
        self.automaton = afnToafd(automata)
        self.inputString = inputString
        #Atributos de estado
        self.indexStack = []
        self.i = 0
        self.lastLexemIndex = 0


    def reset(self, inputString):
        self.indexStack = []
        self.inputString = inputString

    def setInput(self, inputString):
        self.inputString = inputString

    def getToken(self):#SDDMASDDPDD.DDDMDDDBMTTTLDLLLDMMDD.DPLDLD
        ultimoEstadoAceptado = None
        estadoAnterior = None
        tabla = [("", "")]
        principioDelLexema = 0
        currentState = self.automaton.edoInicial#Empieza en el inicial
        while self.i < len(self.inputString): #Recorremos la cadena
            c = self.inputString[self.i]
            destinoConSimbolo = currentState.getTransitionsBySymbol(c)
            if destinoConSimbolo != None:
                self.i += 1
                currentState = destinoConSimbolo
                
                if currentState.aceptacion: #Si el estado al que nos movimos es de aceptación
                    self.lastLexemIndex = self.i
                    ultimoEstadoAceptado = currentState
                    tabla[len(tabla) -1] = list(tabla[len(tabla) -1])#make a[0] mutable
                    tabla[len(tabla) -1][0] = self.inputString[principioDelLexema:self.i] #now new assignment will be valid
                    tabla[len(tabla) -1][1] = currentState.getToken()
                    tabla[len(tabla) -1] = tuple(tabla[len(tabla) -1]) #make a[0] again a tuple                    
            else:#El siguiente simbolo no tiene transición
                if ultimoEstadoAceptado == None:#hay error
                    currentState = self.automaton.edoInicial#vuelve al estado inicial
                    tabla[len(tabla) -1] = list(tabla[len(tabla) -1])#make a[0] mutable
                    tabla[len(tabla) -1][0] = self.inputString[principioDelLexema:self.i] #now new assignment will be valid
                    tabla[len(tabla) -1][1] = "ERROR"
                    tabla[len(tabla) -1] = tuple(tabla[len(tabla) -1]) #make a[0] again a tuple
                    principioDelLexema = self.i
                    tupla = ("", "")
                    tabla.append(tupla)
                else:     
                    tabla[len(tabla) -1] = list(tabla[len(tabla) -1])#make a[0] mutable
                    tabla[len(tabla) -1][0] = self.inputString[principioDelLexema:self.i] #now new assignment will be valid
                    tabla[len(tabla) -1][1] = currentState.getToken()
                    tabla[len(tabla) -1] = tuple(tabla[len(tabla) -1]) #make a[0] again a tuple
                    tupla = ("", "")
                    tabla.append(tupla)
                    self.i = self.lastLexemIndex
                    principioDelLexema = self.i
                    currentState = self.automaton.edoInicial#vuelve al estado inicial

        
        headers = [("Lexema ","Token")]
        max_length_column = []
        elements_in_tuple = 2

        for i in range(elements_in_tuple):
            max_length_column.append(max(max(len(e[i])+2 for e in tabla), max(len(e[i])+2 for e in headers) ) )    

        for e in headers:
            for i in range(elements_in_tuple):
                print(e[i].ljust(max_length_column[i]), end='')
        print('\n')
        for e in tabla:
            for i in range(elements_in_tuple):
                print(e[i].ljust(max_length_column[i]), end='')
            print('\n')


    def returnToken(self):
        if len(self.indexStack) > 0:
            self.indexStack.pop()
    
    def getCurrentLexem(self):
        if len(self.indexStack) >= 2:
            firstIndex = self.indexStack[len(self.indexStack) - 2]
            secondIndex = self.indexStack[len(self.indexStack) - 1]
            return self.inputString[firstIndex:secondIndex]
        else:
            return None

    def getLexicState(self):
        return [self.i, self.lastLexemIndex, self.indexStack]
        

    def setLexicState(self, lexicState):
        self.i = lexicState[0]
        self.lastLexemIndex = lexicState[1]
        self.indexStack = lexicState[2]
        
