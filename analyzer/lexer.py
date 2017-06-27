#! coding: utf-8
import ply.lex as lex

tokens = (
)

# Build the lexer
lexer = lex.lex()

def apply_lexer(string):
    lexer.input(string)

    return list(lexer)
