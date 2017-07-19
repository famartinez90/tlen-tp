import ply.yacc as yacc
from .lexer import tokens
import objetoParseado as op
import sys,traceback

def p_if_exp_then_exp_else_exp(p):
    'expression : IF expression THEN expression ELSE expression'
    p[0] = op.construirIfThenElse(p[2], p[4], p[6])

def p_exp_nat(p):
    'expression : nat'
    p[0] = p[1]

def p_exp_bool(p):
    'expression : bool'    
    p[0] = p[1]

def p_exp_apply(p):
    'expression : LPAREN lambda RPAREN subexp'
    p[0] = op.construirAplicacion(p[2], p[4])

def p_exp_expression_lambda(p):
    'expression : lambda'
    p[0] = p[1]

def p_exp_variable_expresion(p):
    'expression : variable'    
    p[0] = p[1]    

def p_exp_variable_variable(p):
    'expression : variable variable'
    p[0] = op.construirAplicacion(p[1], [p[2]])

def p_subexp_paren_lambda(p):
    'subexp : LPAREN lambda RPAREN subexp'
    p[0] = [p[2]] + p[4]

def p_subexp_nat(p):
    'subexp : nat subexp'
    p[0] = [p[1]] + p[2]

def p_subexp_bool(p):
    'subexp : bool subexp'
    p[0] = [p[1]] + p[2]

def p_subexp_empty(p):
    'subexp : '
    p[0] = []

def p_exp_lambda(p):    
    'lambda : LAMBDA variable DOBLEDOT type DOT expression'
    p[0] = op.construirLambda(p[2], p[4], p[6])

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

def p_exp_nat_nat(p):
    'expression : nat nat'
    p[0] = op.construirError('La parte izquierda de la aplicacion ('+p[1].getExpresion()+') no es una funcion con dominio en Nat')
    
    
def p_error(p):
    print "Hubo un error en el parseo."
    print p
    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(string):
    try:
        parseado = parser.parse(string)
        if parseado is not None and parseado.getTipo() == 'Var':
            return 'Error: el termino no es cerrado ('+parseado.getExpresion()+' esta libre)'

        if parseado is not None and not isinstance(parseado.getExpresion(), op.EError) and not isinstance(parseado, op.EError):            
            return str(parseado.getExpresion()) + ':'+ parseado.getTipo()
        elif not isinstance(parseado, op.EError):
            return parseado.getExpresion().getExpresion() + parseado.getExpresion().getTipo()
        else:
            return str(parseado.getExpresion()) + parseado.getTipo()

    except:  
        traceback.print_exc(file=sys.stdout)
