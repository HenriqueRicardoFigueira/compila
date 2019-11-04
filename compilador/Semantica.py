from Lexer import Lexer, Simbol
from Parser import Parser

class Semantica:
    def __init__(self, code):
        self.lex = Lexer()
        self.tokens = self.lex.tokens
        self.parser = Parser(code)
        self.lex.insertSimbols(code, "")
        self.table = self.lex.table        

def insertFunc(simbol, t, escopo, tipo, par):
    x = Simbol("FUNC", str(simbol), tipo, 0, 0, escopo, 0, 0, True, par)
    t.table.simbols.append(x)

def checkId (lexema, t):
    i = 0
    idx = 0
    for simbol in t.table.simbols:
        if simbol.lexema == lexema:
             idx = i
             break
        i += 1
    return idx

def insertSimbol(simbol, t, escopo, tipo, dim, func, tam, tam2):
    ant = None
    i = 0
    cont = 0
    for node in t.table.simbols:
        i += 1
        if str(simbol) == node.lexema:
            if ant == str(simbol):
                cont = i
                print(ant, str(simbol))
                break
            if node.escopo == None:
                node.escopo = escopo
            node.tipo = tipo
            node.din = dim
            node.func = func
            node.tam[0] = tam
            node.tam[1] = tam2
            node.visitada = True
            ant = str(simbol)
    t.table.simbols[cont-1].escopo = escopo
    t.table.simbols[cont-1].tipo = tipo
    t.table.simbols[cont-1].din = dim
    t.table.simbols[cont-1].func = func
    t.table.simbols[cont-1].tam[0] = tam
    t.table.simbols[cont-1].tam[1] = tam2
    t.table.simbols[cont-1].visitada = True        
 

def checkRules(t):
    #função principal
    princ = False
    for simbol in t.table.simbols:
        if simbol.inicializada == False and simbol.token == "FUNC" and simbol.lexema != "principal":
            print("Aviso: Função " + simbol.lexema + " declarada, mas não ultilizada.")
        if simbol.lexema == "principal" and simbol.token == "FUNC":
            princ = True
        if simbol.token == "ID" and simbol.inicializada == False:
            print("Aviso: Variável "+ simbol.lexema + " declarada mas não ultilizada")            
    if princ == False:
        print("Erro Sintático: Função principal não declarada.")
        return      
            
def prefix(root, t, escopo, tipo, father, func, tam, tam2, var, dim, tamaux):
    if root:
        par = 0
        s = None
        
        if str(root) == "retorna":
            if escopo == "principal" and root.child[0].child[0].child[0].child[0].child[0].child[0].child[0] != "num_inteiro":
                print("Erro Semântico: Função Principal deveria retornar inteiro, mas retorna vazio.")
                return
        
        if str(root) == "cabecalho":
            escopo = root.child[0].child[0]
            if(len(father.child) == 2):
                tipo = father.child[0].child[0]
            if str(root.child[2]) == "lista_parametros":
                x = str(root.child[2].child[0])
                x = x.split(" ")
                if str(x[0]) != "vazio":
                    par = len(root.child[2].child)
            insertFunc(root.child[0].child[0], t, escopo, tipo, par)
        
        if str(root) == "chamada_funcao":
            flag = False
            i = 0
            idx = 0
            if str(root.value) == "principal":
                print("Erro Semântico: Chamada para a função principal não permitida")
                return
            for simbol in t.table.simbols:
                if simbol.lexema == root.value and str(simbol.token) == "FUNC":
                   s = simbol.par
                   flag = True
                   idx = i
                   break
                i += 1
            if flag == False:
                print("Erro Semântico: Função " +root.value+ " não declarada")
                return
            y = str(root.child[0].child[0])
            y = y.split(" ")
            
            if s == 1:
                if y[0] != "vazio":
                    t.table.simbols[idx].inicializada = True
                    pass
                else:
                    print("Erro Semântico: Chamada à função com número de parâmetros menor que o declarado")
            if s > 1:
                if s == len(root.child[0].child):
                    t.table.simbols[idx].inicializada = True
                    pass
                else:
                    print("Erro Semânctico: Chamada à função com número de parâmetros menor que o declarado")
                
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
    checkRules(t)
    t.table.tablePrint()