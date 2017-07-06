import ply.yacc as yacc
from .lexer import tokens
import objetoParseado as op
import sys

def p_if_exp_then_exp_else_exp(p):
    'expression : IF expression THEN expression ELSE expression'
    if p[4].getTipo() != p[6].getTipo():
        print "Error: las dos opciones del if deben tener el mismo tipo"
    elif p[2].getTipo() != 'Bool':
        print "Error: la guarda del if debe ser de tipo Bool"
    elif p[2].getValor() == 'True':
        p[0] = op.objetoParseado(
            'if '+str(p[2].getExpresion())+' then '+str(p[4].getExpresion())+' else '+p[6].getExpresion(),
            p[4].getTipo(),
            p[4].getValor()
        )
    elif p[2].getValor() == 'False':
        p[0] = op.objetoParseado(
            'if '+str(p[2].getExpresion())+' then '+str(p[4].getExpresion())+' else '+p[6].getExpresion(),
            p[6].getTipo(),
            p[6].getValor()
        )
    else:
        return "Error: el valor de la guarda debe ser True o False"
#        p[0] = op.objetoParseado(
#            'if '+str(p[2].getExpresion())+' then '+str(p[4].getExpresion())+' else '+p[6].getExpresion(),
#            'Bool->'+p[4].getTipo(),
#            'if '+str(p[2].getExpresion())+' then '+str(p[4].getExpresion())+' else '+p[6].getExpresion()
#        )    

def p_exp_expression_lambda(p):
    'expression : lambda'
    p[0] = p[1]

def p_exp_atomic_type(p):
    'atomictype : TYPE'    
    p[0] = p[1]        

def p_exp_type_arrow(p):
    'type : atomictype ARROW type'
    #print p[0]
    p[0] = '('+p[1]+p[2]+p[3]+')'

def p_exp_type(p):
    'type : atomictype'
    p[0] = p[1]        

def p_exp_variable(p):
    'variable : VARIABLE'       
    p[0] = op.objetoParseado(p[1], None, None, "%("+p[1]+")s" )        


def p_exp_lambda(p):    
    'lambda : LAMBDA variable DOBLEDOT type DOT expression'                    
    if p[6].getTipo() is not None:
        t = p[6].getTipo()
    else:        
        t = p[6].getTipoDinamico({p[2].getExpresion():p[4]})

    o = op.objetoParseado('\\%s:%s.%s' % (p[2].getExpresion(),p[4],p[6].getExpresion()), '%s->%s' % (p[4],t),None)    
    # o.pushVariable(p[2].getExpresion())
    p[0] = o

def p_exp_iszero(p):
    'bool : ISZERO expression'
    if p[2].getTipo() != 'Nat':
        return "Error: isZero espera un Nat"
    else:
        p[0] = op.objetoParseado('isZero('+p[2].getExpresion()+')', 'Bool', str(p[2].getValor() == 0))

def p_exp_true(p):
    'bool : TRUE'
    p[0] = op.objetoParseado("True", 'Bool', 'True')

def p_exp_false(p):
    'bool : FALSE'
    p[0] = op.objetoParseado("False", 'Bool', 'False')

def p_exp_succ(p):
    'nat : SUCC expression'    
    # if p[2].getTipo() != 'Nat':
    #     return "Error: succ espera un Nat como argumento"
    # print p[2]
    v = 0
    if p[2].getValor() is not None:
        v = p[2].getValor()+1
    p[0] = op.objetoParseado('succ('+str(p[2].getExpresion())+')', 'Nat', v)    
    # print('p_exp_succ')

def p_exp_pred(p):
    'nat : PRED expression'

    newValue = max(0, p[2].getValor()-1)
    #newValue = 1
    
    newExpression = 'pred(%s)' % p[2].getExpresion()
    p[0] = op.objetoParseado(newExpression, 'Nat', newValue)


def p_exp_zero(p):
    'nat : ZERO'
    #print('p_exp_zero')    
    #print p[1]
    p[0] = op.objetoParseado('0', 'Nat', p[1])
    
def p_exp_nat(p):
    'expression : nat'
    #print('p_exp_nat')
    p[0] = p[1]

def p_exp_bool(p):
    'expression : bool'
    #print('p_exp_bool')
    p[0] = p[1]

def p_exp_apply(p):
    'expression : lambda expression'
    print('p_exp_lambda_expresion')
    # p[0] = p[1]
    # v = p[2].getValor() 
    # print v
    # if v is not None:        
    #     varName =  p[1].popVariable()
    #     print varName        
    #     print p[1].getValorDinamico( { varName: v } )
    #print p[2].getValorDinamico()
    print('p_exp_lambda_expresion')


def p_exp_variable_expresion(p):
    'expression : variable'    
    p[0] = p[1]    

def p_term_lparen_rparen(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]
    
def p_error(p):
    print ("Hubo un error en el parseo.")
    print (p)
    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(string):
    parseado = parser.parse(string)

    if parseado is not None:
        if parseado.getValor() is not None:
            return str(parseado.getValor())+':'+parseado.getTipo()
        else:
            return str(parseado.getExpresion())+':'+parseado.getTipo()
