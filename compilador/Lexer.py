# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# lex.py
# Análise Léxica para disciplina de compiladores 2019/01
# by henrislip
# -------------------------------------------------------------------------

import ply.lex as lex

class Table:

    def __init__(self):
        self.simbols = []
    
    def tablePrint(self):
        for node in self.simbols:
            node.nodeprint()

class Node:

    def __init__(self, token, lexema, tipo, din, tam, escopo, inicializada, linha, coluna):
        self.token = token
        self.lexema = lexema
        self.tipo = tipo
        self.din = din
        self.tam = tam
        self.escopo = escopo
        self.inicializada = False
        self.linha = linha
        self.coluna = coluna
    
    def nodeprint(self):
        print(self.token, self.lexema, self.tipo, self.din, self.tam, self.escopo, self.inicializada, self.linha, self.coluna)

class Lexer:

    def __init__(self):
        self.lexer = lex.lex(debug=False, module=self, optimize=False)
        self.table = Table()

    def insertSimbols(self, code):
        flag = False
        lex.input(code)
        while True:
            token = lex.token()
            if not token:
                break
            if token.type == "ID":
                if len(self.table.simbols) > 0:
                    for n in self.table.simbols:
                        if n.lexema == token.value:
                            flag = True
                            break
                if flag == False:
                    node = Node(token.type, token.value, "", "", "", "", "", token.lineno, token.lexpos)
                    self.table.simbols.append(node)
            flag = False


    chaves = {
        'até': 'ATE',
        'então': 'ENTAO',
        'escreva': 'ESCREVA',
        'fim': 'FIM',
        'flutuante': 'FLUTUANTE',
        'inteiro': 'INTEIRO',
        'leia': 'LEIA',
        'repita': 'REPITA',
        'retorna': 'RETORNA',
        'se': 'SE',
        'senão': 'SENAO',
    }

    # Tokens para o PLY

    tokens = [
        'ATRIBUICAO',
        'ADICAO',
        'ABRE_COL',
        'FECHA_COL',
        'CIENTIFICO',
        'DIFERENTE',
        'DIVISAO',
        'DOIS_PONTOS',
        'E_LOGI',
        'ID',
        'IGUAL',
        'MAIORIGUAL',
        'MAIOR',
        'MAIS',
        'MENORIGUAL',
        'MENOR',
        'MENOS',
        'MULTIPLICACAO',
        'NEGACAO',
        'OU_LOGI',
        'ABRE_PAR',
        'FECHA_PAR',
        'SUBTRACAO',
        'VIRGULA'
    ] + list(chaves.values())

    # Regex para definir tokens

    t_ADICAO = r'\+'
    t_ATRIBUICAO = r':='
    #t_CIENTIFICO = r'\([+-]?('
    t_FECHA_COL = r'\]'
    t_ABRE_COL = r'\['
    t_DIFERENTE = r'\!\='
    t_DIVISAO = r'/'
    t_DOIS_PONTOS = r':'
    t_E_LOGI = r'\&\&'
    t_IGUAL = r'='
    t_MAIORIGUAL = r'>='
    t_MAIOR = r'>'
    t_MENORIGUAL = r'<='
    t_MENOR = r'<'
    t_MULTIPLICACAO = r'\*'
    t_NEGACAO = r'\!'
    t_OU_LOGI = r'\|\|'
    t_FECHA_PAR = r'\)'
    t_ABRE_PAR = r'\('
    t_SUBTRACAO = r'\-'
    t_VIRGULA = r'\,'

    # Identificar ids

    def t_ID(self, t):
        r'[a-zA-Zá-ñÁ-Ñ][a-zA-Zá-ñÁ-Ñ0-9_]*'
        t.type = self.chaves.get(t.value, 'ID')
        return t

    # Identificar comentarios

    def t_COMMENT(self, t):
        r'\{[^}]*[^{]*\}'

    # Identificar números flutuantes

    def t_FLUTUANTE(self, t):
        r'[0-9]+[\.][0-9]*'
        t.value = float(t.value)
        return t
    # Identificar números inteiros

    def t_INTEIRO(self, t):
        r'[0-9]+'
        t.value = int(t.value)
        return t

    # Contador de linhas documentação PLY

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Ignorar expressões documentação PLY

    t_ignore = ' \t'

    # Identificar erros documentação PLY

    def t_error(self, t):
        print("Item ilegal: '%s', linha %d, coluna %d" %
              (t.value[0], t.lineno, t.lexpos))
        t.lexer.skip(1)

    def print(self, code):
        lex.input(code)
        while True:
            token = lex.token()
            if not token:
                break
            print(token.type, token.value)


if __name__ == '__main__':
    from sys import argv
    lexer = Lexer()
    f = open(argv[1])
    table = lexer.table
    lexer.insertSimbols(f.read())
    lexer.print(f.read())
    table.tablePrint()