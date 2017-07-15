import ply.yacc as yacc
from .lexer import tokens
import objetoParseado as op
import sys,traceback

def p_exp_expression_1(p):
    'expression : openexpression'            
    p[0] = p[1] 

def p_exp_expression_openexpression(p):
    'expression : closeexpression'        
    print "aca"
    p[0] = p[1] 

def p_if_exp_then_exp_else_exp(p):
    'openexpression : IF openexpression THEN openexpression ELSE openexpression'
    p[0] = op.construirIfThenElse(p[2],p[4],p[6])

# def p_if_exp_then_exp_else_exp(p):
#     'baseexpression : IF expression THEN expression ELSE baseexpression'
#     p[0] = op.construirIfThenElse(p[2],p[4],p[6])


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
    # print 'contruyo variable' 
    # print p[1]
    p[0] = op.construirVariable(p[1])        


def p_exp_variable_expresion(p):
    'openexpression : variable'    
    p[0] = p[1]    

def p_exp_iszero(p):
    'bool : ISZERO LPAREN expression RPAREN'    
    p[0] = op.construirIsZero(p[3])

def p_exp_true(p):
    'bool : TRUE'
    p[0] = op.construirBool(True)
    
def p_exp_false(p):
    'bool : FALSE'
    p[0] = op.construirBool(False)

def p_exp_succ(p):
    'nat : SUCC LPAREN expression RPAREN'    
    p[0] = op.construirSucc(p[3])

def p_exp_pred(p):
    'nat : PRED LPAREN expression RPAREN'
    p[0] = op.construirPred(p[3])


def p_exp_zero(p):
    'nat : ZERO'
    p[0] = op.construirZero()
    
def p_exp_nat(p):
    'openexpression : nat'
    #print('p_exp_nat')
    p[0] = p[1]

def p_exp_bool(p):
    'openexpression : bool'    
    p[0] = p[1]

# def p_exp_apply(p):
#     'expression : lambda expression'
#     #'expression : LPAREN lambda RPAREN expression'
#     #print 'p_exp_lambda_expresion' 
#     # 1. evaluar si p[1] acepta tipo de p[2]
#     # 2. resolver tipos en p[1] en base a la aplicacion de p[2]
#     # 3. tratar de resolver un valor en base  a la aplicacion.    
#     p[0] = op.construirAplicacion(p[1] , p[2])
#     #p[0] = op.construirAplicacion(p[2] , p[4])


# def p_lambda_baseexpression(p):
#     'expression : openexpression'            
#     p[0] = op.construirAplicacion(p[1] , p[2])

def p_baselambda_baseexpression(p):
    'closeexpression : LPAREN openlambda  openexpression RPAREN'            
    print "aca"
    p[0] = op.construirAplicacion(p[2] , p[3])

def p_baselambda_baseexpressiona(p):
    'closeexpression : LPAREN openlambda RPAREN'            
    # print "aca"
    p[0] = p[2]


def p_exp_expression_lambda(p):
    'openexpression : openlambda'    
    # print "en lambda"
    # print p[1]
    # print "aca" 
    # print p[1]
    p[0] = p[1]


def p_exp_lambda(p):    
    'openlambda : LAMBDA variable DOBLEDOT type DOT openexpression'    
    # print "contruyo lambda"
    # print p[2].getValor()
    p[0] = op.construirLambda(p[2],p[4],p[6])

def p_exp_lambda_2(p):    
    'openlambda : LAMBDA variable DOBLEDOT type DOT closeexpression'    
    # print "contruyo lambda"
    # print p[2].getValor()
    p[0] = op.construirLambda(p[2],p[4],p[6])

# def p_exp_complexlambda(p):    
#     'baselambda : LAMBDA variable DOBLEDOT type DOT LPAREN complexexpression RPAREN'    
#     # print "contruyo lambda"
#     p[0] = op.construirLambda(p[2],p[4],p[7])

def p_exp_lambda_baselambda_2(p):    
    'openexpression : LPAREN openexpression RPAREN openexpression '
    # print "en lambda"
    # print p[1]
    print "aca"
    p[0] = p[1]

def p_exp_lambda_baselambda(p):
    'openexpression : closeexpression  openexpression'    
    # print p[1]    
    p[0] = op.construirAplicacion(p[1] , p[2]) 

# def p_exp_lambda_baselambda(p):
#     'expression : LPAREN  openexpression RPAREN  openexpression'
#     # print "en lambda"
#     # print p[1]
#     p[0] = op.construirAplicacion(p[2] , p[4]) 


# def p_exp_expression_complexexpression(p):
#     'expression : complexexpression'
#     p[0] = p[1]




# def p_exp_apply(p):    
#     'openexpression : closeexpression  openexpression'
#     # print "contruyo alla" lambda
#     p[0] = op.construirAplicacion(p[1] , p[2])

# def p_exp_apply_2(p):
#     'expression : expression baseexpression'
#     # print "contruyo aca"
#     # print p[1]
#     p[0] = op.construirAplicacion(p[1] , p[2])




    
def p_error(p):
    # print ("Hubo un error en el parseo.")
    # print (p)
    parser.restart()

# Build the parser
#yacc.yacc(debug=1, write_tables=1)
parser = yacc.yacc(debug=1, write_tables=1)

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
