from Lexer import Lexer, Simbol
from Parser import Parser

class Semantica:
    def __init__(self, code):
        self.lex = Lexer()
        self.tokens = self.lex.tokens
        self.parser = Parser(code)
        self.lex.insertSimbols(code)
        self.table = self.lex.table        

def prefix(root, t, escopo, tipo, father):
    if root:
        if str(root) == "cabecalho":
            escopo = root.child[0].child[0]
        if str(root) == "declaracao_variaveis":
            tipo = root.child[0].child[0]
        if len(root.child) == 0:
            if str(root.value) != 'inteiro' and str(root.value) != 'flutuante' and str(root.value) != 'num_inteiro' and str(root.value) != 'num_flutuante':
                for node in t.table.simbols:
                    if str(root) == node.lexema:
                        node.tipo = tipo
                        node.escopo = escopo
        father = root
        for son in root.child:
            prefix(son, t, escopo, tipo, father)

#def addTipo(node, t, escopo):
#    tipo = node.child[0].child[0]
#    for simbol in t.table.simbols:
#        if simbol.lexema == str(child):
#            simbol.tipo = tipo
#            simbol.escopo = escopo
#            simbol.tam = tamanho
#            simbol.din = dim

if __name__ == '__main__':
    from sys import argv, exit
    a = argv[1].split('/')
    f = open(argv[1])
    t = Semantica(f.read())
    escopo = "global"
    tipo = ""
    father = ""
    prefix(t.parser.ast, t, escopo, tipo, father)
    t.table.tablePrint()