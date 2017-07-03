import ply.yacc as yacc
from .lexer import tokens


def p_n_succ(p):
    'N : SUCC LPAREN N RPAREN'
    p[0] = p[3] + 1

def p_n_pred(p):
    'N : PRED LPAREN N RPAREN'
    if p[3] < 1:
        print "Error: no se puede hacer pred de 0"
    else:
        p[0] = p[3] - 1

def p_b_iszero(p):
    'B : ISZERO LPAREN N RPAREN'
    p[0] = 'isZero()'

def p_b_true(p):
    'B : TRUE'
    p[0] = True

def p_b_false(p):
    'B : FALSE'
    p[0] = False

def p_n_nat(p):
    'N : ZERO'
    p[0] = 0

def p_error(p):
    print "Hubo un error en el parseo."

    parser.restart()


# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(string):
    return parser.parse(string)
