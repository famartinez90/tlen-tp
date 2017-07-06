class objetoParseado(object):

    def __init__(self, expresion, tipo, valor, tipoDinamico=None,valorDinamico=None):
        self.expresion = expresion
        self.tipo = tipo
        self.valor = valor
        self.tipoDinamico = tipoDinamico
        self.valorDinamico = valorDinamico
        # self.variablesLigadas = []

    def getExpresion(self):
        return self.expresion
    
    def getTipo(self):
        return self.tipo
    
    def getValor(self):
        return self.valor

    def getTipoDinamico(self, data):
        return self.tipoDinamico % data 

    def getValorDinamico(self, data):
        return self.valorDinamico()
    
    def pushVariable(self,var):
        self.variablesLigadas.append(var)

    def popVariable(self):
        return self.variablesLigadas[-1]

