class Transicion:
    def __init__(self, simbolo, estadoDestino):
        self.simbolo = simbolo
        self.estadoDestino = estadoDestino

class Estado:
    def __init__(self, _id):
        self._id = _id
        self.transiciones = []


class AFN:
Estado EdoInicial;
vector<Estado> EdosAceptacion;
vector<char> Alfabeto;
vector<Estado> EdosAFN;
public:
    AFN();
    AFN(char simbolo);
    def __init__(self, simbolo=None):
        if simbolo is None:
            self.edoInicial = None
            self.wordList = []
        else:
            self.wordList = wordList
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




