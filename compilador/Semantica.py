from Lexer import Lexer, Simbol
from Parser import Parser

class Semantica:
    def __init__(self, code):
        self.lex = Lexer()
        self.tokens = self.lex.tokens
        self.parser = Parser(code)
        self.lex.insertSimbols(code)
        self.table = self.lex.table        

def prefix(root, t, escopo):
    if root:
        if str(root) == "cabecalho":
            escopo = root.child[0].child[0]
        if str(root) == "declaracao_variaveis":
            addTipo(root, t, escopo)

        for son in root.child:
            prefix(son, t, escopo)

def addTipo(node, t, escopo):
    child = node.child[1].child[0].child[0].child[0]
    tipo = node.child[0].child[0]
    for simbol in t.table.simbols:
        if simbol.lexema == str(child):
            simbol.tipo = tipo
            simbol.escopo = escopo

if __name__ == '__main__':
    from sys import argv, exit
    a = argv[1].split('/')
    f = open(argv[1])
    t = Semantica(f.read())
    escopo = "global"
    prefix(t.parser.ast, t, escopo)
    t.table.tablePrint()