import ply.yacc as yacc
from .lexer import tokens

def p_e_be(p):
    'E : BE'
    p[0] = p[1]

def p_e_n(p):
    'E : N'
    p[0] = p[1]

def p_e_paren_e(p):
    'E : LPAREN E RPAREN'
    p[0] = p[2]

def p_be_c(p):
    'BE : C'
    p[0] = p[1]

def p_be_n(p):
    'BE : N'
    p[0] = p[1]

def p_be_b(p):
    'BE : B'
    p[0] = p[1]

def p_if_be_then_e_else_e(p):
    'C : IF BE THEN E ELSE E'
    if p[4] != p[6]:
        print "Error: las dos opciones del if deben tener el mismo tipo"
    elif p[2]:
        p[0] = p[4]
    else:
        p[0] = p[6]

def p_n_succ(p):
    'N : SUCC LPAREN N RPAREN'
    p[0] = 'Nat'

def p_n_pred(p):
    'N : PRED LPAREN N RPAREN'
    if p[3] < 1:
        print "Error: no se puede hacer pred de 0"
    else:
        p[0] = 'Nat'

def p_b_iszero(p):
    'B : ISZERO LPAREN N RPAREN'
    if p[3] != 'Nat':
        return "Error: isZero espera un Nat"
    else:
        p[0] = p[3]+'->Bool'

def p_b_true(p):
    'B : TRUE'
    p[0] = 'Bool'

def p_b_false(p):
    'B : FALSE'
    p[0] = 'Bool'

def p_n_nat(p):
    'N : ZERO'
    p[0] = 'Nat'

def p_error(p):
    print "Hubo un error en el parseo."

    parser.restart()


# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(string):
    if parser.parse(string) is not None:
        return string+':'+parser.parse(string)
