class objetoParseado(object):

    def __init__(self, expresion, tipo, valor):
        self.expresion = expresion
        self.tipo = tipo
        self.valor = valor

    def getExpresion(self):
        return self.expresion
    
    def getTipo(self):
        return self.tipo
    
    def getValor(self):
        return self.valor
