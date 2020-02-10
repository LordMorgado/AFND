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
        self.aceptacion = True

class Automata:
    def __init__(self, simbolo=None):
        self.edosceptacion = []
        self.edosAutomata = []
        if simbolo is None:
            self.edoInicial = Estado()
            self.alfabeto = ["epsi"]
        else:
            self.alfabeto = ["epsi", simbolo]
            self.edoInicial = Estado()
            estadoAceptacion = Estado()
            estadoAceptacion.acepta()
            self.edosceptacion.append(estadoAceptacion)
            self.edosAutomata = [self.edoInicial, estadoAceptacion]
            self.edoInicial.transiciones.append(Transicion(simbolo, estadoAceptacion))

def cerraduraE (e: Estado):
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



auto = Automata("a")
dibujaAutomata(auto)
