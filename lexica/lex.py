# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# lex.py
# Análise Léxica para disciplina de compiladores 2019/01
# by henrislip
# -------------------------------------------------------------------------

import ply.lex as lex
import sys

# Palavras reservadas que definem a linguagem

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
    'COLCHETE_D',
    'COLCHETE_E',
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
    'PARENTESE_D',
    'PARENTESE_E',
    'SUBTRACAO',
    'VIRGULA'
] + list(chaves.values())

# Regex para definir tokens

t_ADICAO = r'\+'
t_ATRIBUICAO = r':='
#t_CIENTIFICO = r'\([+-]?('
t_COLCHETE_D = r'\]'
t_COLCHETE_E = r'\['
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
t_PARENTESE_D = r'\)'
t_PARENTESE_E = r'\('
t_SUBTRACAO = r'\-'
t_VIRGULA = r'\,'

# Identificar ids

def t_ID(t):
    r'[a-zA-Zá-ñÁ-Ñ][a-zA-Zá-ñÁ-Ñ0-9_]*'
    t.type = chaves.get(t.value, 'ID')
    return t

# Identificar comentarios

def t_COMMENT(t):
    r'\{[^}]*[^{]*\}'

# Identificar números flutuantes
def t_FLUTUANTE(t):
    r'[0-9]+[\.][0-9]*'
    t.value = float(t.value)
    return t
# Identificar números inteiros

def t_INTEIRO(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

# Contador de linhas documentação PLY

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar expressões documentação PLY

t_ignore = ' \t'

# Identificar erros documentação PLY

def t_error(t):
    print("Item ilegal: '%s', linha %d, coluna %d" %(t.value[0], t.lineno, t.lexpos))
    t.lexer.skip(1)

lex.lex()
f = open(sys.argv[1])
lex.input(f.read())
while True:
    token = lex.token()
    if not token:
        break
    print(token.type )