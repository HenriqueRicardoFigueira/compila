from Lexer import Lexer, Simbol
from Parser import Parser

class Semantica:
    def __init__(self, code):
        self.lex = Lexer()
        self.tokens = self.lex.tokens
        self.parser = Parser(code)
        self.lex.insertSimbols(code)
        self.table = self.lex.table        

def prefix(root, t):
    if root:
        if str(root) == "declaracao_variaveis":
            addTipo(root, t)
        for son in root.child:
            prefix(son, t)

def addTipo(node, t):
    child = node.child[1].child[0].child[0].child[0]
    tipo = node.child[0].child[0]
    #for
    print(child)
    print(tipo)



if __name__ == '__main__':
    from sys import argv, exit
    a = argv[1].split('/')
    f = open(argv[1])
    t = Semantica(f.read())
    prefix(t.parser.ast, t)