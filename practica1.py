from graphviz import Digraph

def dibujaAutomata(afnd):
    
    f = Digraph('finite_state_machine', filename='afnd.gv')
    f.attr(rankdir='LR', size='8,5')
    for estado in afnd.edosAutomata:
        if estado.aceptacion:
            f.attr('node', shape='doublecircle')
        else:
            f.attr('node', shape='circle')
        f.node(str(estado.id))
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
        self.aceptacion = not self.aceptacion

class Automata:
    def __init__(self, simbolo=None):
        self.edosceptacion = []
        self.edosAutomata = []
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
    print("""
    1.crear automata
    2.unir automata
    3.cerradura epsilon
    4.Exit/Quit
    """)
    ans = input("elige una opción ")
    if ans=="1":
        print("\nintroduce simbolo: ")
        simboloNuevoAlfabeto = input()
        automatas.append(Automata(simboloNuevoAlfabeto))
    elif ans=="2":
        print("\n Unir automatas")
        for 
    elif ans=="3":
        print("\n Student Record Found")
    elif ans=="4":
        print("\n Adios")
        ans = None
    else:
        print("\n Esa no es una opción")


dibujaAutomata(automatas.pop())
