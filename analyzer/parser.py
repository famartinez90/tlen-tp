import ply.yacc as yacc
from .lexer import tokens

def p_e_c(p):
    'E : C'
    p[0] = p[1]

def p_e_b(p):
    'E : B'
    p[0] = p[1]

def p_e_n(p):
    'E : N'
    p[0] = p[1]

def p_f_asign(p):
	'F : ASIGN'
	p[0] = (str(p[1]), )

def p_if_e_then_e_else_e(p):
    'C : IF E THEN E ELSE E'
    if p[4][1] != p[6][1]:
        print "Error: las dos opciones del if deben tener el mismo tipo"
    elif p[2]:
        p[0] = (str(p[1]+' '+p[2][0]+' '+p[3]+' '+p[4][0]+' '+p[5]+' '+p[6][0]), '('+p[2][1]+'->'+p[4][1]+')')
    else:
        p[0] = (str(p[1]+' '+p[2][0]+' '+p[3]+' '+p[4][0]+' '+p[5]+' '+p[6][0]), '('+p[2][1]+'->'+p[6][1]+')')

def p_t_b(p):
    'T : BOOL R'
    p[0] = ('Bool', 'Bool')

def p_t_n(p):
    'T : NAT R'
    p[0] = ('Nat', 'Nat')

def p_t_arrow(p):
    'R : ARROW T R'
    p[0] = (str(p[1][0]+' '+p[2][0]+' '+p[3][0]), '')

def p_r_lambda(p):
    'R : '
    p[0] = ('', '')

def p_b_iszero(p):
    'B : ISZERO LPAREN N RPAREN'
    if p[3][1] != 'Nat':
        return "Error: isZero espera un Nat"
    else:
        p[0] = (str(p[1]+p[2]+p[3][0]+p[4]), 'Bool')

def p_b_true(p):
    'B : TRUE'
    p[0] = (str(p[1]), 'Bool')

def p_b_false(p):
    'B : FALSE'
    p[0] = (str(p[1]), 'Bool')

def p_n_succ(p):
    'N : SUCC LPAREN N RPAREN'
    p[0] = (str(p[1]+p[2]+p[3][0]+p[4]), 'Nat')

def p_n_pred(p):
    'N : PRED LPAREN N RPAREN'
    if p[3][0] == '0':
        p[0] = ('0', 'Nat')
    else:
        p[0] = (str(p[1]+p[2]+p[3][0]+p[4]), 'Nat')

def p_n_nat(p):
    'N : ZERO'
    p[0] = (str(p[1]), 'Nat')

def p_error(p):
    print "Hubo un error en el parseo."

    parser.restart()


# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(string):
    parseado = parser.parse(string)

    if parseado is not None:
        return parseado[0]+':'+parseado[1]
