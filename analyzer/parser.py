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
        p[0] = op.objetoParseado(
            'if '+str(p[2].getExpresion())+' then '+str(p[4].getExpresion())+' else '+p[6].getExpresion(),
            'Bool->'+p[4].getTipo(),
            'if '+str(p[2].getExpresion())+' then '+str(p[4].getExpresion())+' else '+p[6].getExpresion()
        )

def p_exp_iszero(p):
    'expression : ISZERO LPAREN expression RPAREN'
    if p[3].getTipo() != 'Nat':
        return "Error: isZero espera un Nat"
    else:
        p[0] = op.objetoParseado('isZero('+p[3].getExpresion()+')', 'Bool', str(p[3].getValor() == 0))

def p_exp_true(p):
    'expression : TRUE'
    p[0] = op.objetoParseado("True", 'Bool', 'True')

def p_exp_false(p):
    'expression : FALSE'
    p[0] = op.objetoParseado("False", 'Bool', 'False')

def p_expression_succ(p):
    'expression : SUCC LPAREN expression RPAREN'
    if p[3].getTipo() != 'Nat':
        return "Error: succ espera un Nat como argumento"
    
    p[0] = op.objetoParseado('succ('+str(p[3].getExpresion())+')', 'Nat', 'succ('+str(p[3].getValor())+')')

def p_exp_pred_succ(p):
    'expression : PRED LPAREN SUCC LPAREN expression RPAREN RPAREN'
    p[0] = op.objetoParseado(str(p[5].getExpresion()), 'Nat', p[5].getValor())

def p_exp_pred(p):
    'expression : PRED LPAREN ZERO RPAREN'
    p[0] = op.objetoParseado('pred('+str(p[3])+')', 'Nat', '0')

def p_exp_zero(p):
    'expression : ZERO'
    p[0] = op.objetoParseado('0', 'Nat', 0)

def p_error(p):
    print ("Hubo un error en el parseo.")

    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(string):
    parseado = parser.parse(string)

    if parseado is not None:
        return str(parseado.getValor())+':'+parseado.getTipo()
