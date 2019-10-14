# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# lex.py
# Análise Sintática para disciplina de compiladores 2019/01
# by henrislip
# -------------------------------------------------------------------------

from ply import yacc
from Lexer import Lexer

class Tree:

    def __init__(self, type_node, child=[], value=" ", line=""):
        self.type = type_node
        self.child = child
        self.value = value
        self.line = line

    def __str__(self):
        return self.type

class Parser:

    def __init__(self, code):
        self.lex = Lexer()
        self.tokens = self.lex.tokens
        self.precedence = (
            ('left','SENAO'),
            ('left', 'IGUAL', 'MAIORIGUAL', 'MAIOR', 'MENORIGUAL', 'MENOR'),
            ('left', 'ADICAO', 'SUBTRACAO'),
            ('left', 'MULTIPLICACAO', 'DIVISAO'),
        )
        parser = yacc.yacc(debug=False, module=self, optimize=False)
        self.ast = parser.parse(code)

    def p_programa(self, p):
        'programa : lista_declaracoes'
        p[0] = Tree('programa', [p[1]])

    def p_lista_declaracoes(self, p):
        'lista_declaracoes : lista_declaracoes', p[[1]]
        
    
    def seeTree(node, level="\n"):
        if node != None:
            print("%s %s %s" %(level, node.type, node.value))
            for son in node.child:
                seeTree(son, level+"\n")


if __name__ == '__main__':
    from sys import argv, exit
    f = open(argv[1])
    t = Parser(f.read())
    seeTree(t.ast)