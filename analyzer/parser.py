import ply.yacc as yacc
from .lexer import tokens

def p_error(p):
    print "Hubo un error en el parseo."

    parser.restart()


# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(string):
    return parser.parse(string)
