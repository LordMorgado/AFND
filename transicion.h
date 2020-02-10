#ifndef TRANSICION_H
#define TRANSICION_H

#include "estado.h"
#include <vector> // http://www.cplusplus.com/reference/vector/vector/ (documentación de librería) 
using namespace std;

class Transicion {
    char simbolo;
    Estado estadoDestino;
  public:
        Transicion(char s, Estado ed);
};

#endif