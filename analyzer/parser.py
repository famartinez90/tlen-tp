import ply.yacc as yacc
from .lexer import tokens
import objetoParseado as op

def p_if_exp_then_exp_else_exp(p):
    'expression : IF expression THEN expression ELSE expression'
    if p[4].getTipo() != p[6].getTipo():
        print "Error: las dos opciones del if deben tener el mismo tipo"
    elif p[2].getTipo() != 'Bool':
        print "Error: la guarda del if debe ser de tipo Bool"
    elif p[2].getValor() == 'True':
        p[0] = op.objetoParseado(
            'if '+str(p[2].getExpresion())+' then '+str(p[4].getExpresion())+' else '+p[6].getExpresion(),
            'Bool->'+p[4].getTipo(),
            p[4].getValor()
        )
    elif p[2].getValor() == 'False':
        p[0] = op.objetoParseado(
            'if '+str(p[2].getExpresion())+' then '+str(p[4].getExpresion())+' else '+p[6].getExpresion(),
            'Bool->'+p[6].getTipo(),
            p[6].getValor()
        )
    else:
        return "Error: el valor de la guarda debe ser True o False"
#        p[0] = op.objetoParseado(
#            'if '+str(p[2].getExpresion())+' then '+str(p[4].getExpresion())+' else '+p[6].getExpresion(),
#            'Bool->'+p[4].getTipo(),
#            'if '+str(p[2].getExpresion())+' then '+str(p[4].getExpresion())+' else '+p[6].getExpresion()
#        )

def p_exp_iszero(p):
    'bool : ISZERO expression'
    if p[3].getTipo() != 'Nat':
        return "Error: isZero espera un Nat"
    else:
        p[0] = op.objetoParseado('isZero('+p[3].getExpresion()+')', 'Bool', str(p[3].getValor() == 0))

def p_exp_true(p):
    'bool : TRUE'
    p[0] = op.objetoParseado("True", 'Bool', 'True')

def p_exp_false(p):
    'bool : FALSE'
    p[0] = op.objetoParseado("False", 'Bool', 'False')

def p_exp_succ(p):
    'nat : SUCC expression'
    print('p_exp_succ')
    if p[2].getTipo() != 'Nat':
        return "Error: succ espera un Nat como argumento"
    
    p[0] = op.objetoParseado('succ('+str(p[2].getExpresion())+')', 'Nat', p[2].getValor()+1)

def p_exp_pred(p):
    'nat : PRED expression'
    print('p_exp_pred')
    newValue = max(0, p[2].getValor()-1)
    newExpression = ''
    for i in range(newValue):
        newExpression +='succ('
    newExpression +='0'
    for i in range(newValue):
        newExpression +=')'
    p[0] = op.objetoParseado(newExpression, 'Nat', newValue)

def p_exp_zero(p):
    'nat : ZERO'
    print('p_exp_zero')
    p[0] = op.objetoParseado('0', 'Nat', 0)
    
def p_exp_nat(p):
    'expression : nat'
    print('p_exp_nat')
    p[0] = p[1]

def p_exp_bool(p):
    'expression : bool'
    print('p_exp_bool')
    p[0] = p[1]

def p_term_lparen_rparen(p):
    'expression : LPAREN expression RPAREN'
    print('p_term_lparen_rparen')
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
        return str(parseado.getExpresion())+':'+parseado.getTipo()
