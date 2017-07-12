
class objetoParseado(object):

    def __init__(self, expresion, tipo, valor):
        self.expresion = expresion
        self.tipo = [tipo]                
        self.valor = valor

    def getExpresion(self):
        return self.expresion
    
    def getTipo(self):
        return self.tipo

    def printTipo():
        if len(self.tipo) == 1:
            return self.tipo
    
    def printExpresion(self):
        return  'juancho'

    def printValue(self):        
        return '0'

    def getValor(self):
        return self.valor


def construirLambda():
    return LAMBDA()

def construirBool(valor):
    return EBool(valor)

def construirAplicacion(lamb, param):
    # 1. evaluar si p[1] acepta tipo de p[2]
    # 2. resolver tipos en p[1] en base a la aplicacion de p[2]
    # 3. tratar de resolver un valor en base  a la aplicacion.
    return EAplicacion(lamb,param)


def construirZero():
    return EZero()

def construirSucc(param):
    return ESucc(param)

def construirPred(param):
    return EPred(param)

def construirIsZero(param):
    return EIsZero(param)

def construirLambda(var,tipo,expr):
    return ELambda(var,tipo, expr)

def construirVariable(var):
    return EVariable(var)


def construirIfThenElse(cond,exprIf,exprElse):
    return EIfThenElse(cond,exprIf,exprElse)


class EIfThenElse(objetoParseado):
    def __init__(self,cond,exprIf,exprElse):
        self.cond = cond
        self.exprIf = exprIf
        self.exprElse = exprElse

    def getValor(self,scope={}):
        # TODO: chequear q la condicion sea bool         
        if self.cond.getValor(scope).getValor():
            if  self.exprIf.getValor(scope).getTipo() != 'Indefinido':
                return self.exprIf.getValor(scope)
        else:    
            if  self.exprElse.getValor(scope).getTipo() != 'Indefinido':
                return self.exprElse.getValor(scope)
        return EValor('Indefinido','None' )
        # if p[4].getTipo() != p[6].getTipo():
        #     print "Error: las dos opciones del if deben tener el mismo tipo"
        # elif p[2].getTipo() != 'Bool':
        #     print "Error: la guarda del if debe ser de tipo Bool"
        # else:
        #     return "Error: el valor de la guarda debe ser True o False"

    def printTipo(self):
        return self.exprIf.printTipo()

    def printExpresion(self):

        if self.getValor().getTipo() != 'Indefinido':            
            return self.getValor().printValor()

        return  'if %s then %s else %s' % (self.cond.printExpresion(),
            self.exprIf.printExpresion(),
            self.exprElse.printExpresion())


class EAplicacion(objetoParseado):

    def __init__(self,lamb,param):
        self.lamb = lamb
        self.param = param

    def printTipo(self):
        # print self.param.getValor()
        # print  self.lamb.getValor(self.param.getValor())
        if self.getValor().getTipo() != 'Indefinido':        
            return self.getValor().getTipo()
        return 'ERROR'

    def printExpresion(self):
        if self.getValor().getTipo() != 'Indefinido':        
            return self.lamb.getValor(self.param.getValor({})).printValor()

        return  '%s %s' % (self.lamb.printExpresion(),self.param.printExpresion())
        return 'a'

    def getValor(self,scope={}):
        return self.lamb.getValor(self.param.getValor(scope))


class EVariable(objetoParseado):
    def __init__(self,var):
        self.var = var

    def printTipo(self):
        return '--'

    def printExpresion(self):        
        return  self.var

    def getValor(self,scope={}):                
        if scope.has_key(self.var): 
            if scope[self.var].getTipo() != 'Indefinido':
                return scope[self.var]  
        return EValor('Indefinido',None )

class ELambda(objetoParseado):    
    def __init__(self,var, tipo,expr):
        self.var = var
        self.tipo = tipo
        self.expr = expr

    def getValor(self,param=None,scope={}):        
        if param is not None:            
            # print self.expr
            if self.expr.getValor({ self.var.printExpresion():  param}).getTipo() != 'Indefinido':                            
                return self.expr.getValor({ self.var.printExpresion():  param})
        return EValor('Indefinido',None )

    def printTipo(self):
        return '%s -> %s' % (self.tipo, self.expr.printTipo())

    def printExpresion(self):
        return  '\\%s:%s.%s' % (self.var.printExpresion(),self.tipo,self.expr.printExpresion())

class EZero(objetoParseado):
    def __init__(self):
        pass

    def getValor(self,scope={}):
        return EValor('Nat',0)

    def printTipo(self):
        return 'Nat'

    def printExpresion(self):
        return '0'

class ESucc(objetoParseado):
    def __init__(self,param):
        self.hijo = param

    def printTipo(self):
        return 'Nat'

    def printExpresion(self):
        return 'succ(%s)' % self.hijo.printExpresion()

    def getValor(self,scope={}):         
        if (self.hijo.getValor(scope).getTipo() == 'Nat'):
            return EValor('Nat',self.hijo.getValor(scope).getValor()+1 )
        return EValor('Indefinido',None )


class EPred(objetoParseado):
    def __init__(self,param):
        self.hijo = param

    def printTipo(self):
        return 'Nat'

    def printExpresion(self):
        if self.getValor().getTipo() == 'Nat':
            return self.getValor().printValor()
        return 'pred(%s)' % self.hijo.printExpresion()

    def getValor(self,scope={}):
        if (self.hijo.getValor(scope).getTipo() == 'Nat'):
            return EValor('Nat',self.hijo.getValor(scope).getValor()-1 )
        return EValor('Indefinido',None )


class EIsZero(objetoParseado):
    
    def __init__(self,param):
        self.hijo = param        
        
    def printTipo(self):
        return 'Bool'

    def printExpresion(self):        
        if self.getValor().getTipo() == 'Bool':
            return self.getValor().printValor()
        return 'iszero(%s)' % self.hijo.printExpresion()
    
    def getValor(self,scope={}):
        if  self.hijo.getValor(scope).getTipo() == 'Nat':
                return EValor('Bool',not bool(self.hijo.getValor(scope).getValor()) )        
        return EValor('Indefinido','None' )        


class EBool(objetoParseado):
    def __init__(self, valor):
        self.valor = valor

    def getValor(self,scope={}):
        return EValor('Bool',bool(self.valor))

    def printTipo(self):        
        return 'Bool'         

    def printExpresion(self):
        if self.valor:
            return 'true'
        else:
            return 'false'




class EValor(object):
    def __init__(self,tipo,valor):
        self.tipo  = tipo
        self.valor = valor

    def getTipo(self):
        return self.tipo

    def getValor(self):
        return self.valor

    def printValor(self):
        if self.tipo == 'Nat':
            return self.printNat()
        elif self.tipo == 'Bool':
            return self.printBool()
        else:
            return self.printIndefinido()

    def printBool(self):
        return  'true' if self.valor else 'false'
    
    def printNat(self):
        num = '0'
        for i in range(max(0,int(self.valor))):
            num  = 'succ(%s)' % num
        return '%s' % num

    def printIndefinido(self):
        return 'Indefinido'

    def __str__(self):
        return 'DEBUG: %s : %s ' % (self.tipo,self.valor)

