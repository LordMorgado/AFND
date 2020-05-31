from os import system
from graphviz import Digraph
from automata import *
from lexico import *

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
    8.pasar a AFD
    9.análisis léxico
    10.Indicar clase léxica de automata
    11.duplicar automata
    12.Exit/Quit
    """)
    ans = input("elige una opción ")

    if ans=="1":
        print("\nintroduce simbolo: ")
        simboloNuevoAlfabeto = input()
        automatas.append(Automata(simboloNuevoAlfabeto))
    
    elif ans=="2":
        if len(automatas) < 2:
            continue
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
        if len(automatas) < 2:
            continue
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
        if len(automatas) == 0:
            continue
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
        if len(automatas) == 0:
            continue
        for i in range(0,len(automatas)):
            print("automata " + str(i+1) + " = " + str(automatas[i].alfabeto))

        while True:
            opc1 = int(input())
            if opc1 in range(1,len(automatas)+1):
                automatas[opc1-1] = afnToafd(automatas[opc1-1])
                break
            else:
                print("Opción no son válida")

    elif ans=="9":
        if len(automatas) == 0:
            continue
        print("Elige el automata")
        for i in range(0,len(automatas)):
            print("automata " + str(i+1) + " = " + str(automatas[i].alfabeto))
        while True:
            opc1 = int(input())
            if opc1 in range(1,len(automatas)+1):
                automatas[opc1-1].tablaDeTransiciones()
                cadena = input("Introduce la cadena a analizar: ")
                LexicAnalyzer(automatas[opc1-1], cadena)
                s = input("esperando...")
                break
            else:
                print("Opción no son válida")

    elif ans=="10":
        if len(automatas) == 0:
            continue
        print("Elige el automata")
        for i in range(0,len(automatas)):
            print("automata " + str(i+1) + " = " + str(automatas[i].alfabeto))
        while True:
            opc1 = int(input())
            if opc1 in range(1,len(automatas)+1):
                cadena = input("Introduce El nombre de la clase léxica: ")
                automatas[opc1-1].setClaseLexica(cadena)
                break
            else:
                print("Opción no son válida")

    elif ans=="11":
        if len(automatas) == 0:
            continue
        print("Elige el automata a Duplicar")
        for i in range(0,len(automatas)):
            print("automata " + str(i+1) + " = " + str(automatas[i].alfabeto))
        while True:
            opc1 = int(input())
            if opc1 in range(1,len(automatas)+1):
                automatas.append(automatas[opc1-1].duplicar())
                break
            else:
                print("Opción no son válida")
    
    elif ans=="12":
        print("\n Adeu")
        ans = None
    
    else:
        print("\n Esa no es una opción")
