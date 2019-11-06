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

def searchEscopo (lexema, t):
    escopo = []
    for simbol in t.table.simbols:
        if simbol.lexema == str(lexema):
                escopo.append(simbol.escopo)
    return escopo

def checkId (lexema, t, escopo):
    i = 0
    ant = None
    idx = 0
    flag = False
    for simbol in t.table.simbols:
        if simbol.lexema == ant:
            for x in range(i, len(t.table.simbols)-1):
                    if ant == str(t.table.simbols[x].lexema) and t.table.simbols[x].escopo == escopo :
                        idx = x
                        flag = True
                        break
        if simbol.lexema == lexema and simbol.escopo == escopo:
             idx = i
             flag = True
             break
        i += 1
        ant = str(simbol.lexema)
    if flag == True:
        return idx
    else:
        return False

def expressRight(root, t, escopo):
    flag = False
    if str(root) == "expressao_simples":
        pass
        #if len(root.child) == 3:
        #print(root.child[1].value)
    if str(root) == "var":
        if str(root.child[0]) != "ID":
            x = searchEscopo(root.child[0], t)
        else:
            x = searchEscopo(root.child[0].child[0], t)
        if len(x) == 1:
            esc = x[0]
        else:
            z = -1
            for v in x:
                z += 1
                if v == escopo:
                    break
            esc = x[z]
        
        i = checkId(str(root.child[0]), t, esc)
        tp = t.table.simbols[i].tipo
        print(t.table.simbols[i].lexema, t.table.simbols[i].escopo)

        if str(root.child[0].child[0]) == "indice":
            flag = True
    if len(root.child) > 0:
        for s in root.child:
            expressRight(s, t, escopo)

def navega(root, t, escopo):
    if str.__len__(str(root.value)) > 0:
        if str(root.child[0]) == "TIPO":
            if str(root.child[0].child[0]) == "inteiro" or str(root.child[0].child[0]) == "flutuante":
                insertSimbol(root.value, t, escopo, root.child[0].child[0], 0, False, 0, 0)
    for son in root.child:
        if len(son.child) > 0:
            navega(son, t, escopo)
       
def insertSimbol(simbol, t, escopo, tipo, dim, func, tam, tam2):
    ant = None
    cont = 0
    j = 0
    flag = False
    for node in t.table.simbols:
        if str(simbol) == node.lexema:
            if ant == str(simbol):
                for x in range(j, len(t.table.simbols)-1):
                    if ant == str(t.table.simbols[x].lexema):
                        cont = x
                        flag = True
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
        j += 1
    if flag == True:
        t.table.simbols[cont].escopo = escopo
        t.table.simbols[cont].tipo = tipo
        t.table.simbols[cont].din = dim
        t.table.simbols[cont].func = func
        t.table.simbols[cont].tam[0] = tam
        t.table.simbols[cont].tam[1] = tam2
        t.table.simbols[cont].visitada = True       
 
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
        x = None


        if str(root) == "atribuicao":
            typ = None
            h = checkId(str(root.child[0].child[0].child[0]), t, escopo)
            t.table.simbols[h].inicializada = True
            if str(t.table.simbols[h].tipo) == "inteiro":
                typ = "num_inteiro"
            if str(t.table.simbols[h].tipo) == "flutuante":
                typ = "num_flutuante"
            util = root.child[1].child[0].child[0].child[0].child[0].child[0].child[0]
            if str(util) == "num_inteiro" or str(util) == "num_flutuante":
                typ2 = str(root.child[1].child[0].child[0].child[0].child[0].child[0].child[0])
                if typ != typ2:
                    print("Aviso: Atribuição de tipos distintos.")
                

        if str(root) == "expressao":
            #if str(root.child[0]) == "expressao_simples":
            expressRight(root.child[0], t, escopo)
            #if str(root.child[0].child[0].child[0]) == "ID":
            #    x = checkId(str(root.child[0].child[0].child[0].child[0]), t, escopo)
            #    if x == False:
            #        print("Aviso: Variável " + str(root.child[0].child[0].child[0].child[0]) + " não declarada")
            #    else:
            #        t.table.simbols[x].inicializada = True

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
                    if par == 1:
                        tei = root.child[2].child[0].value
                        tp = root.child[2].child[0].child[0].child[0]
                        insertSimbol(tei, t, escopo, tp, 0, False, 0, 0)
                if len(root.child[2].child) > 1:
                   navega(root.child[2], t, escopo)            
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
            if s == 0:
                t.table.simbols[idx].inicializada = True
            if s == 1 :
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
            if str(root.child[1].child[0].child[0]) == "ID":
                x = checkId(root.child[1].child[0].child[0].child[0], t, escopo)
                if x != False:
                    if t.table.simbols[x].tipo:
                        print("Aviso: Variável "+ t.table.simbols[x].lexema + " já declarada")
        
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