#include <iostream>
#include <vector> // http://www.cplusplus.com/reference/vector/vector/ (documentación de librería) 
using namespace std;

class Estado;

class Transicion {
    char simbolo;
    Estado estadoDestino;
  public:
        Transicion(char s, Estado ed);
};

class Estado {
    int _id;
    vector<Transicion> transiciones;
    public:
        Estado (int id);
};

class AFN {
    Estado EdoInicial;
    vector<Estado> EdosAceptacion;
    vector<char> Alfabeto;
    vector<Estado> EdosAFN;
    public:
        AFN();
        AFN(char simbolo);
};
/**
    Constructores de clase AFN
*/
AFN::AFN(){
    this.EdoInicial = NULL;
    this.Alfabeto.clear();
    this.EdosAceptacion.clear();
    this.EdosAFN.clear();
}
AFN::AFN(char simbolo){
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


