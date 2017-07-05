class objetoParseado(object):

    def __init__(self, expresion, tipo, valor, tipoDinamico=None):
        self.expresion = expresion
        self.tipo = tipo
        self.valor = valor
        self.tipoDinamico = tipoDinamico

    def getExpresion(self):
        return self.expresion
    
    def getTipo(self):
        return self.tipo
    
    def getValor(self):
        return self.valor

    def getTipoDinamico(self, data):
        return self.tipoDinamico % data 