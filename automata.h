#ifndef AUTOMATA_H
#define AUTOMATA_H

#include "estado.h"
#include <vector> // http://www.cplusplus.com/reference/vector/vector/ (documentación de librería) 
using namespace std;

class Automata {
    Estado EdoInicial;
    vector<Estado> EdosAceptacion;
    vector<char> Alfabeto;
    vector<Estado> EdosAFN;
    public:
        Automata();
        Automata(char simbolo);
};

#endif