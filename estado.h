#ifndef ESTADO_H
#define ESTADO_H

#include "transicion.h"
#include <vector> // http://www.cplusplus.com/reference/vector/vector/ (documentación de librería) 
using namespace std;

class Estado {
    int _id;
    vector<Transicion> transiciones;
    public:
        Estado (int id);
};

#endif