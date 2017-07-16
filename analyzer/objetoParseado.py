
class objetoParseado(object):

    def __init__(self, expresion, tipo, valor):
        self.expresion = expresion
        self.tipo = [tipo]                
        self.valor = valor
        self.bindedVariables = {}

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

    def bind(self,var,expression):
        self.bindedVariables[var]  = expression


def construirBool(valor):
    return EBool(valor)

def construirAplicacion(lamb, param):
    # 1. evaluar si p[1] acepta tipo de p[2]
    # 2. resolver tipos en p[1] en base a la aplicacion de p[2]
    # 3. tratar de resolver un valor en base  a la aplicacion.
    #print lamb
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


class ETipo(object):
    def __init__(self,tipo,tipo2=None):
        if tipo2 == None:
            self.tipoClase = 'atomico'
            self.tipo = tipo
        else:
            self.tipoClase = 'lambda'
            if type(tipo) == str or type(tipo2) == str:
                raise Exception('tipo y tipo2 deben ser instancias de la clase ETipo')
            self.tipo = tipo
            self.tipo2 = tipo2

    def __str__(self):
        if self.tipoClase == 'atomico':
            return self.tipo
        else:
            if self.tipo.tipoClase == 'atomico':
                a = '%s' %  self.tipo
            else:
                a = '(%s)' %  self.tipo

            if self.tipo2.tipoClase == 'atomico':
                b = '%s' %  self.tipo2
            else:
                b = '(%s)' %  self.tipo2
            return '%s -> %s' %s (a,b)

class EIfThenElse(objetoParseado):
    def __init__(self,cond,exprIf,exprElse):
        self.cond = cond
        self.exprIf = exprIf
        self.exprElse = exprElse

    def getValor(self,scope={}):
        # TODO: chequear q la condicion sea bool         
        c = self.cond.getValor(scope)
        if c.getTipo() != 'Indefinido' :
            if c.getValor() and self.exprIf.getValor(scope).getTipo() != 'Indefinido':
                print "salgo aca"
                return self.exprIf.getValor(scope)
            elif c.getValor() and self.exprElse.getValor(scope).getTipo() != 'Indefinido':
                print "salgo aca2"
                return self.exprElse.getValor(scope)
        print "salgo aca3"
        return EValor('Indefinido','None' )
        # if p[4].getTipo() != p[6].getTipo():
        #     print "Error: las dos opciones del if deben tener el mismo tipo"
        # elif p[2].getTipo() != 'Bool':
        #     print "Error: la guarda del if debe ser de tipo Bool"
        # else:
        #     return "Error: el valor de la guarda debe ser True o False"

    def printTipo(self):
        if  self.exprIf.getValor().getTipo() !=  'Indefinido' :
            return self.exprIf.getValor().getTipo()
        elif   self.exprElse.getValor().getTipo() !=  'Indefinido' :
            return self.exprElse.getValor().getTipo()
        return ETipo('Indefinido')

    def printExpresion(self):

        if self.getValor().getTipo() != 'Indefinido':            
            return self.getValor().printValor()

        return  'if %s then %s else %s' % (self.cond.printExpresion(),
            self.exprIf.printExpresion(),
            self.exprElse.printExpresion())


class EAplicacion(objetoParseado):

    def __init__(self,lamb,param):
        self.lamb = lamb
        # print lamb
        self.param = param

    def printTipo(self):
        #print "tiipo"
        # print self.getValor()
        # print self.param.getValor()
        # print  self.lamb.getValor(self.param.getValor())
        if self.getValor().getTipo() != 'Indefinido':        
            return self.getValor().getTipo()
        return 'ERROR'

    def printExpresion(self):
        #print "print valor de expresion %s" % self.getValor().getTipo()
        if self.getValor().getTipo() != 'Indefinido':        
            #print "imprimo el valor %s" % self.getValor()
            return self.getValor().printValor()
        return  '%s %s' % (self.lamb.printExpresion(),self.param.printExpresion())        

    def getValor(self,scope={}):
        #print 'get valor aplicacion'
        s = {'_':self.param.getValor(scope)}
        # print s
        # print self.lamb
        return self.lamb.getValor(s)


class EVariable(objetoParseado):
    def __init__(self,var):
        self.var = var

    def printTipo(self):
        return ETipo('Indefinido')

    def printExpresion(self):        
        return  self.var

    def getValor(self,scope={}):                
        if scope.has_key(self.var): 
            if scope[self.var].getTipo() != 'Indefinido':
                return scope[self.var]  
        return EValor('Indefinido',None )

class ELambda(objetoParseado):    
    def __init__(self,var, tipo,expr):
        print "contrui una lambda con %s %s %s" % (var.var, tipo, expr)
        self.bindedVariables = {}
        self.var = var
        self.tipo = tipo
        self.expr = expr

    def getValor(self,scope={}):        
        self.bindedVariables.update(scope)      
        if scope.has_key('_'):            
            param = scope['_']            
            self.bindedVariables.update({ self.var.printExpresion():  param})
            if self.expr.getValor(self.bindedVariables).getTipo() != 'Indefinido':                                            
                return self.expr.getValor(self.bindedVariables)            
            
            return EValor('Lambda',self.expr.bind(self.bindedVariables) )
        return EValor('Lambda',self.expr )    
        
        
    def printTipo(self):
        return '%s -> %s' % (self.tipo, self.expr.printTipo())

    def printExpresion(self):
        return  '\\%s:%s.%s' % (self.var.printExpresion(),self.tipo,self.expr.printExpresion())

class EZero(objetoParseado):
    def __init__(self):
        pass

    def getValor(self,scope={}):
        return EValor(ETipo('Nat'),0)

    def printTipo(self):
        return ETipo('Nat')

    def printExpresion(self):
        return '0'

class ESucc(objetoParseado):
    def __init__(self,param):
        self.hijo = param

    def printTipo(self):
        return ETipo('Nat')

    def printExpresion(self):
        # print "en print expresion"
        # print self.getValor().getTipo()
        if self.getValor().getTipo() == 'Nat':
            return self.getValor().printValor()        
        return 'succ(%s)' % self.hijo.printExpresion()

    def getValor(self,scope={}):                 
        if (self.hijo.getValor(scope).getTipo() == 'Nat'):
            #print "pido el valor del hijo %s "  % self.hijo.getValor(scope).getValor()            
            return EValor('Nat',self.hijo.getValor(scope).getValor()+1 )
        return EValor('Indefinido',None )


class EPred(objetoParseado):
    def __init__(self,param):
        self.hijo = param

    def printTipo(self):
        return ETipo('Nat')

    def printExpresion(self):
        if self.getValor().getTipo() == 'Nat':
            return self.getValor().printValor()
        return 'pred(%s)' % self.hijo.printExpresion()

    def getValor(self,scope={}):
        if (self.hijo.getValor(scope).getTipo() == 'Nat'):
            if self.hijo.getValor(scope).getValor() > 0:
                return EValor(ETipo('Nat'), self.hijo.getValor(scope).getValor()-1)
            else:
                return EValor('Nat', self.hijo.getValor(scope).getValor())

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
        return EValor( ETipo('Bool'), bool(self.valor) )

    def printTipo(self):        
        return  ETipo('Bool')

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
        elif self.tipo == 'Lambda':
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

    def printLambda(self):
        print "estras son binded"
        print self.bindedVariables
        return 'Lambda'

    def printIndefinido(self):
        return 'Indefinido'

    def __str__(self):
        return 'DEBUG: %s : %s ' % (self.tipo,self.valor)

    def __repr__(self):
        return 'DEBUG: %s : %s ' % (self.tipo,self.valor)

