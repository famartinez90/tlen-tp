import ply.yacc as yacc
from .lexer import tokens
import objetoParseado as op

# def p_if_be_then_e_else_e(p):
#     'C : IF BE THEN E ELSE E'
#     if p[4][1] != p[6][1]:
#         print "Error: las dos opciones del if deben tener el mismo tipo"
#     elif p[2]:
#         p[0] = (str(p[1]+' '+p[2][0]+' '+p[3]+' '+p[4][0]+' '+p[5]+' '+p[6][0]), '('+p[2][1]+'->'+p[4][1]+')')
#     else:
#         p[0] = (str(p[1]+' '+p[2][0]+' '+p[3]+' '+p[4][0]+' '+p[5]+' '+p[6][0]), '('+p[2][1]+'->'+p[6][1]+')')

def p_b_iszero(p):
    'expression : ISZERO LPAREN N RPAREN'
    if p[3].getTipo() != 'Nat':
        return "Error: isZero espera un Nat"
    else:
        p[0] = op.objetoParseado('isZero('+p[3].expresion+')', 'Bool', str(p[3].valor == 0))

def p_expression_true(p):
    'expression : TRUE'
    p[0] = op.objetoParseado("True", 'Bool', 'True')

def p_expression_false(p):
    'expression : FALSE'
    p[0] = op.objetoParseado("False", 'Bool', 'False')

def p_expression_succ(p):
    'expression : SUCC LPAREN expression RPAREN'
	if(p[3].getTipo() != 'Nat') return "Error: succ espera un Nat como argumento"
	p[0] = op.objetoParseado('succ('+p[3].getExpresion()')', 'succ('+p[3].getExpresion()')', 'Nat')

def p_n_pred(p):
    'N : PRED LPAREN N RPAREN'
    if p[3][0] == '0':
        p[0] = ('0', 'Nat')
    else:
        p[0] = (str(p[1]+p[2]+p[3][0]+p[4]), 'Nat')

def p_n_nat(p):
    'N : ZERO'
    p[0] = op.objetoParseado('0', 'Nat', 0)

def p_error(p):
    print ("Hubo un error en el parseo.")

    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(string):
    parseado = parser.parse(string)

    if parseado is not None:
        return parseado.getExpresion()+':'+parseado.getTipo()
