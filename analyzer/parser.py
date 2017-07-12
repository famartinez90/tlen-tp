import ply.yacc as yacc
from .lexer import tokens
import objetoParseado as op
import sys,traceback


def p_if_exp_then_exp_else_exp(p):
    'expression : IF expression THEN expression ELSE expression'
    p[0] = op.construirIfThenElse(p[2],p[4],p[6])

def p_exp_expression_lambda(p):
    'expression : lambda'
    p[0] = p[1]

def p_exp_atomic_type(p):
    'atomictype : TYPE'    
    p[0] = p[1]        

def p_exp_type_arrow(p):
    'type : atomictype ARROW type'    
    p[0] = '('+p[1]+p[2]+p[3]+')'

def p_exp_type(p):
    'type : atomictype'
    p[0] = p[1]        

def p_exp_variable(p):
    'variable : VARIABLE'       
    p[0] = op.construirVariable(p[1])        

def p_exp_lambda(p):    
    'lambda : LAMBDA variable DOBLEDOT type DOT expression'
    p[0] = op.construirLambda(p[2],p[4],p[6])

def p_exp_iszero(p):
    'bool : ISZERO expression'    
    p[0] = op.construirIsZero(p[2])

def p_exp_true(p):
    'bool : TRUE'
    p[0] = op.construirBool(True)
    
def p_exp_false(p):
    'bool : FALSE'
    p[0] = op.construirBool(False)

def p_exp_succ(p):
    'nat : SUCC expression'    
    p[0] = op.construirSucc(p[2])

def p_exp_pred(p):
    'nat : PRED expression'
    p[0] = op.construirPred(p[2])


def p_exp_zero(p):
    'nat : ZERO'
    p[0] = op.construirZero()
    
def p_exp_nat(p):
    'expression : nat'
    #print('p_exp_nat')
    p[0] = p[1]

def p_exp_bool(p):
    'expression : bool'    
    p[0] = p[1]

def p_exp_apply(p):
    'expression : lambda expression'
    #print 'p_exp_lambda_expresion' 
    # 1. evaluar si p[1] acepta tipo de p[2]
    # 2. resolver tipos en p[1] en base a la aplicacion de p[2]
    # 3. tratar de resolver un valor en base  a la aplicacion.    
    p[0] = op.construirAplicacion(p[1] , p[2])

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
    try:
        parseado = parser.parse(string)
        if parseado is not None:            
            return parseado.printExpresion() + ':'+ parseado.printTipo()            
    except :  
        traceback.print_exc(file=sys.stdout)
        # print sys.exc_info()[0]          
        # print sys.exc_info()[1]    
        # print sys.exc_info()[2]    


        #if parseado.getValor() is not None:
            #return str(parseado.getValor())+':'+parseado.getTipo()
            #return str(parseado.getValor())+':'+parseado.getTipo()
        #else:
            #return str(parseado.getExpresion())+':'+parseado.getTipo()
