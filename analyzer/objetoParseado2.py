def construirBool(valor):
    return EBool(valor)

def construirZero():
    return EZero()

def construirIsZero(param):
    return EIsZero(param)

def construirSucc(param):
    return ESucc(param)

def construirPred(param):
    return EPred(param)

def construirVariable(var):
    return EVariable(var)

def construirIfThenElse(cond, exprIf, exprElse):
    return EIfThenElse(cond, exprIf, exprElse)

def construirLambda(var, tipo, expr):
    return ELambda(var, tipo, expr)

def construirAplicacion(lamb, param):
    return EAplicacion(lamb, param)

def construirError(mensaje):
    return EError(mensaje)


class objetoParseado2(object):

    def __init__(self, expresion, tipo, valor):
        self.expresion = expresion
        self.tipo = [tipo]                
        self.valor = valor

    def getExpresion(self):
        return self.expresion
    
    def getTipo(self):
        return self.tipo

    def getValor(self):
        return self.valor


class EAplicacion(objetoParseado2):

    def __init__(self, lamb, param):
        self.lamb = lamb
        self.param = param

    def getLamb(self):
        return self.lamb

    def setParam(self, param):
        self.param = param

    def getExpresion(self):
        if self.getValor().getTipo() != 'Indefinido':      
            return self.getValor().getExpresion()

        return  '%s %s' % (self.lamb.getExpresion(), '')        
    
    def getTipo(self):
        if self.getValor().getTipo() != 'Indefinido':        
            return self.getValor().getTipo()
        
        return self.lamb.getTipo()

    def getValor(self, scope={}):
        if len(self.param) == 0 and len(scope) == 0:
            return EValor('Indefinido', None)

        s = {
            'assignment': self.param[0].getValor(scope),
            'passDown': self.param[1:]
        }
        s.update(scope)

        if self.lamb.getTipo() == 'Var' and self.lamb.getValor(scope).getValor() is not None:
            return self.lamb.getValor(scope).getValor().getValor(s)

        return self.lamb.getValor(s)


class ELambda(objetoParseado2):    
    def __init__(self, var, tipo, expr):
        self.var = var
        self.tipo = tipo
        self.expr = expr

    def getExpresion(self):
        return  '\\%s:%s.%s' % (self.var.getExpresion(), self.tipo, self.expr.getExpresion())
    
    def getTipo(self):
        if self.expr.getTipo() == 'Var':
            return '%s->%s' % (self.tipo, self.tipo)

        return '%s->%s' % (self.tipo, self.expr.getTipo())
    
    def getValor(self, scope={}):
        if scope.has_key('assignment'):
            param = scope['assignment']

            if isinstance(self.expr, EAplicacion):
                self.expr.setParam(scope['passDown'])
           
            scope.pop('assignment', None)
            scope.pop('passDown', None)

            newScope = scope
            newScope.update({self.var.getExpresion(): param})

            if self.expr.getValor(newScope).getTipo() != 'Indefinido':
                return self.expr.getValor(newScope)
        
        return EValor('Lambda', self)


class EVariable(objetoParseado2):
    def __init__(self, var):
        self.var = var

    def getExpresion(self):        
        return self.var
    
    def getTipo(self):
        return 'Var'

    def getValor(self, scope={}):
        if scope.has_key(self.var):
            if scope[self.var].getTipo() != 'Indefinido':
                return scope[self.var]
        
        return EValor('Indefinido', None)


class EIfThenElse(objetoParseado2):
    def __init__(self, cond, exprIf, exprElse):
        self.cond = cond
        self.exprIf = exprIf
        self.exprElse = exprElse
    
    def getExpresion(self):
        if isinstance(self.getValor(), EError):
            return self.getValor()

        if self.getValor().getTipo() != 'Indefinido' and self.getValor().getTipo() != 'Var':            
            return self.getValor().getExpresion()

        return  'if %s then %s else %s' % (self.cond.getExpresion(), self.exprIf.getExpresion(), self.exprElse.getExpresion())

    def getTipo(self):
        if self.cond.getTipo() == 'Var':
            if self.exprIf.getTipo() == 'Var':
                return self.exprElse.getTipo()

            return self.exprIf.getTipo()

        return self.exprIf.getTipo()

    def getValor(self, scope={}):
        # TODO: chequear q la condicion sea bool

        # print scope
        
        if self.cond.getTipo() == 'Var' and self.cond.getValor(scope).getValor() is None:
            return self.cond

        if self.cond.getValor(scope).getValor() is None:
            print 'La condicion del if esta indefinida'

        if self.exprIf.getValor(scope).getTipo() != self.exprElse.getValor(scope).getTipo():
            if self.exprIf.getValor(scope).getTipo() != 'Indefinido' and self.exprElse.getValor(scope).getTipo() != 'Indefinido':
                return EError('las dos opciones del if deben tener el mismo tipo')

        if self.cond.getValor(scope).getValor():
            if self.exprIf.getValor(scope).getTipo() != 'Indefinido':
                return self.exprIf.getValor(scope)
        else:    
            if self.exprElse.getValor(scope).getTipo() != 'Indefinido':
                return self.exprElse.getValor(scope)
        
        return EValor('Indefinido', 'None')


class EPred(objetoParseado2):
    def __init__(self,param):
        self.hijo = param

    def getExpresion(self):
        if self.getValor().getTipo() == 'Nat':
            return self.getValor().getValor()
        
        return 'pred(%s)' % self.hijo.getExpresion()
    
    def getTipo(self):
        return 'Nat'

    def getValor(self, scope={}):
        if self.hijo.getValor(scope).getTipo() == 'Nat':
            if self.hijo.getValor(scope).getValor() > 0:
                return EValor('Nat', self.hijo.getValor(scope).getValor()-1)
            else:
                return EValor('Nat', self.hijo.getValor(scope).getValor())

        return EValor('Indefinido', None)


class ESucc(objetoParseado2):
    def __init__(self, param):
        self.hijo = param

    def getExpresion(self):
        if self.getValor().getTipo() == 'Nat':
            return self.getValor().getExpresion()        
        
        return 'succ(%s)' % self.hijo.getExpresion()
    
    def getTipo(self):
        return 'Nat'

    def getValor(self, scope={}):                 
        if self.hijo.getValor(scope).getTipo() == 'Nat':
            return EValor('Nat', self.hijo.getValor(scope).getValor()+1)
        
        return EValor('Indefinido', None)


class EIsZero(objetoParseado2):
    
    def __init__(self, param):
        self.hijo = param        
        
    def getExpresion(self):
        if self.getValor().getTipo() == 'Bool':
            return self.getValor().getExpresion()

        if self.getValor().getTipo() == 'Var':
            return 'iszero('+self.getValor().getExpresion()+')'

        return EError('iszero espera un valor de tipo Nat')
    
    def getTipo(self):
        return 'Bool'

    def getValor(self, scope={}):
        if self.hijo.getValor(scope).getTipo() == 'Nat':
            return EValor('Bool', not bool(self.hijo.getValor(scope).getValor()))        
        
        if self.hijo.getTipo() == 'Var':
            return self.hijo

        return EValor('Indefinido', 'None')


class EZero(objetoParseado2):
    def __init__(self):
        pass

    def getExpresion(self):
        return '0'
    
    def getTipo(self):
        return 'Nat'
    
    def getValor(self, scope={}):
        return EValor('Nat', 0)
    

class EBool(objetoParseado2):
    def __init__(self, valor):
        self.valor = valor

    def getExpresion(self):
        if self.valor:
            return 'true'
        else:
            return 'false'
    
    def getTipo(self):
        return 'Bool'

    def getValor(self, scope={}):
        return EValor('Bool', bool(self.valor))


class EValor(object):
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def getExpresion(self):
        if self.tipo == 'Nat':
            return self.printNat()
        elif self.tipo == 'Bool':
            return self.printBool()
        elif self.tipo == 'Lambda':
            return self.valor.getExpresion()
        else:
            return self.printIndefinido()

    def getTipo(self):
        if self.tipo == 'Lambda':
            return '('+self.valor.getTipo()+')'

        return self.tipo

    def getValor(self):
        return self.valor

    def printBool(self):
        return  'true' if self.valor else 'false'
    
    def printNat(self):
        num = '0'
        for _ in range(max(0, int(self.valor))):
            num = 'succ(%s)' % num        
        return '%s' % num

    def printIndefinido(self):
        return 'Indefinido'

    def __str__(self):
        return 'DEBUG: %s : %s ' % (self.tipo, self.valor)


class EError(object):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def getExpresion(self):
        return 'Error: '

    def getTipo(self):
        return self.mensaje

    def getValor(self):
        return 'Explota'
