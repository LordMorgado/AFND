#include <iostream>
#include "automata.h"
#include "estado.h"
#include "transicion.h"
#include <vector> // http://www.cplusplus.com/reference/vector/vector/ (documentación de librería) 
using namespace std;
/**
    Constructores de clase Automata
*/
Automata::Automata(){
    Alfabeto.clear();
    EdosAceptacion.clear();
    EdosAFN.clear();
}
Automata::Automata(char simbolo){
    Estado estadoAceptacion;
    EdoInicial = new Estado(0);
    Alfabeto.clear();
    Alfabeto.push_back(simbolo);
    EdosAceptacion.clear();
    EdosAceptacion.push_back(estadoAceptacion);
    EdosAFN.clear();
    EdosAFN.push_back(EdoInicial);
    EdosAFN.push_back(estadoAceptacion);
    EdoInicial.transiciones.push_back(new Transicion(simbolo, estadoAceptacion));
}


/**
    Constructores de clase Estado
*/
Estado::Estado(int id){
    _id = id;
}


/**
    Constructores de clase Transicion
*/
Transicion::Transicion(char s, Estado ed){
    simbolo = s;
    estadoDestino = ed;
}

main() {
	return 0;
}
