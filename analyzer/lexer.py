#! coding: utf-8
import ply.lex as lex

tokens = [
    'TRUE',
    'FALSE',
    'ZERO',
    'ISZERO',
    'LPAREN',
    'RPAREN',
    'SUCC',
    'PRED',
    'IF',
    'THEN',
    'ELSE',
    'ARROW'
]

t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_ARROW(t):
    r'->'
    return t

def t_IF(t):
    r'(?i)if'
    return t

def t_THEN(t):
    r'(?i)then'
    return t

def t_ELSE(t):
    r'(?i)else'
    return t

def t_SUCC(t): 
    r'(?i)succ' 
    return t

def t_PRED(t): 
    r'(?i)pred' 
    return t

def t_TRUE(t): 
    r'(?i)true' 
    return t

def t_FALSE(t):
    r'(?i)false' 
    return t

def t_ZERO(t):
    r'0'
    t.value = int(t.value)
    return t

def t_ISZERO(t):
    r'(?i)iszero'
    return t

t_ignore = ' \t'

def t_error(t):
    print 'Illegal character '+str(t)
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def apply_lexer(string):
    lexer.input(string)

    return list(lexer)
