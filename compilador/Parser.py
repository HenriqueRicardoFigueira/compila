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
        'lista_declaracoes : lista_declaracoes declaracao'
        p[0] = Tree('lista_declaracoes', [p[1],p[2]])

    def p_lista_declaracoes1(self, p):
        'lista_declaracoes : lista_declaracoes'
        p[0] = Tree('lista_declaracoes', [p[1]])

    def p_declaracao(self, p):
        '''
            declaracao  :   declaracao_variaveis
                                |   inicializacao_variaveis
                                |   declaracao_funcao
        '''
        p[0] = Tree('declaracao', [p[1]])
    
    def p_declaracao_variaveis(self, p):
        'declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis'
        p[0] = Tree('declaracao_variaveis', [p[1],p[3]])

    def p_inicializacao_variaveis(self, p):
        'inicializacao_variaveis : atribuicao'
        p[0] = Tree('inicializacao_variaveis', [p[1]])

    def p_lista_variaveis(self, p):
        'lista_variaveis : lista_variaveis VIRGULA var'
        p[0] = Tree('lista_variaveis', [p[1], p[3]])

    def p_lista_variaveis1(self, p):
        'lista_variaveis : var'
        p[0] = Tree('lista_variaveis', [p[1]])

    def p_var(self, p):
        'var : ID'
        p[0] = Tree('var', [], p[1])

    def p_var1(self, p):
        'var : ID indice'
        p[0] = Tree('indice', [p[2], p[1]])
    
    def p_indice(self, p):
        'indice : indice ABRE_COL expressao FECHA_COL'
        p[0] = Tree('indice', [p[1], p[3]])

    def p_indice1(self, p):
        'indice : ABRE_COL expressao FECHA_COL'
        p[0] = Tree('indice', [p[2]])
    
    def p_tipo(self,p):
    	'tipo : INTEIRO'
    	p[0] = Tree('inteiro')  
   
    def p_tipo1(self,p):
    	'tipo : FLUTUANTE'
    	p[0] = Tree('flutuante')    
    
    def p_tipo2(self,p):
    	'tipo : CIENTIFICO'
    	p[0] = Tree('cientifico') 

    def p_error(self, p):
        if p:
                print("Erro sintático: '%s', linha %d" % (p.value, p.lineno))
                exit(1)
        else:
                #yacc.restart()
                print('Erro sintático: definições incompletas! ')
                exit(1)
    
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