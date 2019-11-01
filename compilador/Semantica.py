from Lexer import Lexer, Simbol
from Parser import Parser

class Semantica:
    def __init__(self, code):
        self.lex = Lexer()
        self.tokens = self.lex.tokens
        self.parser = Parser(code)
        self.lex.insertSimbols(code, "")
        self.table = self.lex.table        

def insertFunc(simbol, t, escopo, tipo):
    x = Simbol("FUNC", str(simbol), tipo, escopo, 0, 0, 0, 0, True)
    t.table.simbols.append(x)

def insertSimbol(simbol, t, escopo, tipo, dim, func, tam, tam2):
    for node in t.table.simbols:
        if str(simbol) == node.lexema and node.visitada == False:
            if node.escopo == None:
                node.escopo = escopo
            node.tipo = tipo
            node.din = dim
            node.func = func
            node.tam[0] = tam
            node.tam[1] = tam2
            node.visitada = True
            
        
            
def prefix(root, t, escopo, tipo, father, func, tam, tam2, var, dim, tamaux):
    if root:
        if str(root) == "cabecalho":
            escopo = root.child[0].child[0]
            if(len(father.child) == 2):
                tipo = father.child[0].child[0]
            insertFunc(root.child[0].child[0], t, escopo, tipo)
        if str(root) == "declaracao_variaveis":
            tipo = root.child[0].child[0]
        if str(root) == "indice":
            var = father
            dim = 1
            if str(root.child[0]) == 'indice':
                dim = 2   
        if len(root.child) == 0:
            if str(father) == 'ID':
                insertSimbol(root, t, escopo, tipo, dim, func, tam, tam2)
            
            if str(root) == 'num_inteiro' or str(root) == 'num_flutuante':
                if dim == 2:
                    tam2 = root.value
                    tam = tamaux
                else:
                    tam = root.value
                    tamaux = root.value
                insertSimbol(var, t, escopo, tipo, dim, func, tam, tam2)
       
        father = root
        for son in root.child:
            prefix(son, t, escopo, tipo, father, func, tam, tam2, var, dim, tamaux)

if __name__ == '__main__':
    from sys import argv, exit
    a = argv[1].split('/')
    f = open(argv[1])
    t = Semantica(f.read())
    prefix(t.parser.ast, t, "global", "", "", False, 0, 0, None,0, 0)
    t.table.tablePrint()