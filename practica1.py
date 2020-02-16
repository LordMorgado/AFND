from os import system
from graphviz import Digraph

def dibujaAutomata(afnd):
    
    f = Digraph('finite_state_machine', filename='afnd.gv')
    f.attr(rankdir='LR', size='5,5')
    f.attr('node', shape='doublecircle')
    for estado in afnd.edosceptacion:
        f.node(str(estado.id))
    
    f.attr('node', shape='circle')
    afnd.edosAutomata.sort(key=lambda x: x.id, reverse=False)
    for estado in afnd.edosAutomata:
        for trs in estado.transiciones:
            f.edge(str(estado.id), str(trs.estadoDestino.id), label=trs.simbolo)
    f.view()

class Transicion:
    def __init__(self, simbolo: str, estadoDestino):
        self.simbolo = simbolo
        self.estadoDestino = estadoDestino

class Estado:
    _id = 0
    def __init__(self, transiciones=None):
        self.id = Estado._id
        if transiciones is None:
            self.transiciones = []
        else:
            self.transiciones = transiciones
        Estado._id = Estado._id + 1
        self.aceptacion = False
        
    def acepta(self):
        if self.aceptacion:
            self.aceptacion = False
        else:
            self.aceptacion = True

class Automata:
    def __init__(self, simbolo=None):
        self.edosceptacion = []
        self.edosAutomata = []
        self.kleene = False
        self.positiva = False
        self.signo = False
        if simbolo is None:
            self.edoInicial = Estado()
            self.alfabeto = ["ε"]
        else:
            self.alfabeto = ["ε", simbolo]
            self.edoInicial = Estado()
            estadoAceptacion = Estado()
            estadoAceptacion.acepta()
            self.edosceptacion.append(estadoAceptacion)
            self.edosAutomata = [self.edoInicial, estadoAceptacion]
            self.edoInicial.transiciones.append(Transicion(simbolo, estadoAceptacion))
    
    def unirAutomata(self, automata):
        e1 = Estado()
        e2 = Estado()
        e1.transiciones.append(Transicion("ε", self.edoInicial))
        e1.transiciones.append(Transicion("ε", automata.edoInicial))
        for estTran in self.edosceptacion:
          estTran.transiciones.append(Transicion("ε", e2))
          estTran.acepta()

        for estTran2 in automata.edosceptacion:
          estTran2.transiciones.append(Transicion("ε", e2))
          estTran2.acepta()
        e2.acepta()

        self.alfabeto = list(set(self.alfabeto) | set(automata.alfabeto) )
        self.edosAutomata = list(set(self.edosAutomata) | set(automata.edosAutomata) )
        self.edosAutomata.append(e1)
        self.edosAutomata.append(e2)
        self.edosceptacion = []
        self.edosceptacion.append(e2)
        self.edoInicial = e1
        automata = None
        return self
    
    def concatena(self, automata):

        for e in self.edosceptacion:
            e.transiciones = list(set(e.transiciones) | set(automata.edoInicial.transiciones) )
            e.acepta()
        automata.edoInicial.transiciones = []
        self.alfabeto = list(set(self.alfabeto) | set(automata.alfabeto) )
        self.edosceptacion = []
        self.edosceptacion = automata.edosceptacion
        self.edosAutomata = list(set(self.edosAutomata) | set(automata.edosAutomata) )
        self.edosAutomata.remove(automata.edoInicial)
        automata = None
        return self

    def cerraduraPositiva(self):
        if not self.kleene and not self.signo:
            self.positiva = True
            en1 = Estado()
            en2 = Estado()
            eAux = self.edoInicial

            for e in self.edosceptacion:
                e.transiciones.append(Transicion("ε", en1))
                e.acepta()
                e.transiciones.append(Transicion("ε", self.edoInicial))
            self.edosceptacion = []
            en1.acepta()
            self.edosceptacion.append(en1)
            self.edosAutomata.append(en1)

            self.edosAutomata.remove(self.edoInicial)
            self.edosAutomata.append(eAux)
            en2.transiciones.append(Transicion("ε", eAux))
            self.edoInicial = en2

            for e in self.edosAutomata:
                if e.id == 0:
                    e.id = self.edoInicial.id
                    self.edoInicial.id = 0
                    break


            self.edosAutomata.append(self.edoInicial)
            
            
        return self

    def cerraduraKleene(self):
        if not self.positiva and not self.signo:
            self.cerraduraPositiva()
            for e in self.edosceptacion:
                self.edoInicial.transiciones.append(Transicion("ε", e))
            self.kleene = True
        return self

    def cerraduraSigno(self):
        if not self.kleene and not self.positiva:
            for e in self.edosceptacion:
                self.edoInicial.transiciones.append(Transicion("ε", e))
            self.signo = True

def cerraduraE (self, e: Estado):
    R = []
    pila = []
    pila.append(e)
    while pila:
        e2 = pila.pop()
        if e2 in R:
            continue
        R.append(e2)
        for trn in e2.transiciones:
            if trn.simbolo == "epsi":
                if not (trn.estadoDestino in R):
                    pila.append(trn.estadoDestino)
    return R
    
def cerraduraEestados(conjunto):
    R = []
    for e in conjunto:
        R = list(set(R) | set(cerraduraE(e)))
    return R

ans = True
automatas = []
while ans:
    system('clear')
    print("""
    1.crear automata
    2.unir automata
    3.concatenar automatas
    4.cerradura positiva de un autómata
    5.cerradura de Kleene de un autómata
    6.cerradura signo '?'
    7.dibuja autómata
    8.Exit/Quit
    """)
    ans = input("elige una opción ")

    if ans=="1":
        print("\nintroduce simbolo: ")
        simboloNuevoAlfabeto = input()
        automatas.append(Automata(simboloNuevoAlfabeto))
    
    elif ans=="2":
        print("\n Unir dos autómatas")
        print("Selecciona los autómatas a unir:\n")
        for i in range(0,len(automatas)):
            print("automata " + str(i+1) + " = " + str(automatas[i].alfabeto))

        while True:
            opc1 = int(input("Primer autómata a unir: "))
            opc2 = int(input("Segundo autómata a unir: "))
            if opc1 in range(1,len(automatas)+1) and opc2 in range(1,len(automatas)+1):
                automatas[opc1-1].unirAutomata(automatas[opc2-1])
                automatas.pop(opc2-1)
                print("automatas Unidos")
                for i in range(0,len(automatas)):
                    print("automata " + str(i+1) + " = " + str(automatas[i].alfabeto))
                break
            else:
                print("Una o más entradas no son válidas")

        #automatas[0].unirAutomata(automatas[1])
    
    elif ans=="3":
        print("\n Concatenar dos automatas")
        print("Selecciona los autómatas a concatenar:\n")
        for i in range(0,len(automatas)):
            print("automata " + str(i+1) + " = " + str(automatas[i].alfabeto))

        while True:
            opc1 = int(input("Primer autómata a concatenar: "))
            opc2 = int(input("Segundo autómata a concatenar: "))
            if opc1 in range(1,len(automatas)+1) and opc2 in range(1,len(automatas)+1):
                automatas[opc1-1].concatena(automatas[opc2-1])
                automatas.pop(opc2-1)
                print("automatas concatenados")
                for i in range(0,len(automatas)):
                    print("automata " + str(i+1) + " = " + str(automatas[i].alfabeto))
                break
            else:
                print("Una o más entradas no son válidas")
    
    elif ans=="4":#+
        for i in range(0,len(automatas)):
            print("automata " + str(i+1) + " = " + str(automatas[i].alfabeto))

        while True:
            opc1 = int(input())
            if opc1 in range(1,len(automatas)+1):
                automatas[opc1-1].cerraduraPositiva()
                break
            else:
                print("Opción no son válida")

    elif ans=="5":#*
        for i in range(0,len(automatas)):
            print("automata " + str(i+1) + " = " + str(automatas[i].alfabeto))

        while True:
            opc1 = int(input())
            if opc1 in range(1,len(automatas)+1):
                automatas[opc1-1].cerraduraKleene()
                break
            else:
                print("Opción no son válida")
    
    elif ans=="6":#?
        for i in range(0,len(automatas)):
            print("automata " + str(i+1) + " = " + str(automatas[i].alfabeto))

        while True:
            opc1 = int(input())
            if opc1 in range(1,len(automatas)+1):
                automatas[opc1-1].cerraduraSigno()
                break
            else:
                print("Opción no son válida")

    elif ans=="7":
        for i in range(0,len(automatas)):
            print("automata " + str(i+1) + " = " + str(automatas[i].alfabeto))

        while True:
            opc1 = int(input())
            if opc1 in range(1,len(automatas)+1):
                dibujaAutomata(automatas[opc1-1])
                break
            else:
                print("Opción no son válida")

    elif ans=="8":
        print("\n Adios")
        ans = None
    else:
        print("\n Esa no es una opción")


dibujaAutomata(automatas[0])
