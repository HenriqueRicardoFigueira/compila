from Lexer import Lexer, Simbol
from Parser import Parser, Tree
from graphviz import Digraph

class aux:
    def __init__(self):
        self.h = []
        
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

def searchEscopo(lexema, t):
    escopo = []
    for simbol in t.table.simbols:
        if simbol.lexema == str(lexema):
                escopo.append(simbol.escopo)
    return escopo

def checkId(lexema, t, escopo):
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

def support(root, t, father, aux):
    if root:
        if str(root) == "chamada_funcao":
            aux.h.append(root)
            return
        if len(root.child) == 0:
            aux.h.append(root)
        if len(root.child) > 0:
            for x in root.child:
                support(x, t, root, aux)

def expressRight(root, t, escopo, father):
    a = aux()
    tiposExp = aux()
    support(root,t,root,a)
    for z in a.h:
        y = str(z).split("_")
        if y[0] == "chamada":
            for o in t.table.simbols:
                if str(z.value) == str(o.lexema) and str(o.token) == "FUNC":
                    tiposExp.h.append(o.tipo)
                    break
            break
        if y[0] == "num":
            tiposExp.h.append(y[1])
            break 
        if y[0] == "operador":
            pass
        else:
            x = checkId(str(z), t, escopo)
            if type(x) != int:
                x = checkId(str(z), t, "global")
            if type(x) == int:
                tiposExp.h.append(t.table.simbols[x].tipo)
                if str(a.h[0]) == str(t.table.simbols[x].lexema):
                    right = t.table.simbols[x]
                    if right.inicializada == False:
                        right.inicializada = True    
            else:
                print("Erro: Variável "+ str(z) + " não declarada.")
    
    for l in tiposExp.h:
        if str(tiposExp.h[0]) != str(l):
            print("Aviso: Atribuição de tipos distintos " + str(right.lexema)+ " " + str(right.tipo)) 
     
def navega(root, t, escopo):
    if str.__len__(str(root.value)) > 0:
        if str(root.child[0]) == "TIPO":
            if str(root.child[0].child[0]) == "inteiro" or str(root.child[0].child[0]) == "flutuante":
                insertSimbol(root.value, t, escopo, root.child[0].child[0], 0, False, 0, 0)
                id = checkId(str(root.value), t, escopo)
                t.table.simbols[id].inicializada = True
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
            print("Aviso: Variável "+ simbol.lexema + " declarada, mas não ultilizada")            
    if princ == False:
        print("Erro Sintático: Função principal não declarada.")
        return      

def retPrincipal(root):
    if str(root) == "retorna":
        x = leaf(root)
        if str(x) != "num_inteiro":
            print("Erro Semântico: Função principal deveria retornar inteiro, mas retorna vazio")
            return True
    if len(root.child) > 0:
        for i in root.child:
            retPrincipal(i)
    return False

def leaf(root):
    if len(root.child) == 0:
        return root
    else:
        for x in root.child:
            h = leaf(x)
            if h:
                return h
            else:
                leaf(x)
                
def auxLeaf(root):
    if len(root.child) == 0:
        return root
    else:
        return auxLeaf(root.child[0])

def auxVar(root, t, tipo, escopo, func, tam2, tam):
    if str(root) == "lista_variaveis":
        addVar(root, t, tipo, escopo, func, tam2, tam)
    if len(root.child) > 1:
        print(root.child[1].child[0].child[0], escopo, tipo)
        auxVar(root.child[1], t, tipo, escopo, func, tam, tam2)

def addVar(root, t, tipo, escopo, func, tam2, tam):
    if str(root.child[0].child[0].child[0]) == "indice":
        tipoIndice = leaf(root.child[0])
        if str(tipoIndice) != "num_inteiro":
            print("Erro Semântico: índice de array " + str(root.child[0].child[0]) + " não inteiro")
        else:
            insertSimbol(root.child[0].child[0], t, escopo, tipo, 1, func, tipoIndice.value, tam2)
    if str(root.child[0]) == "var":  
        var = leaf(root.child[0])
    else:
        if len(root.child) > 0:
            var = auxLeaf(root.child[1])
    if str(var) != "num_inteiro" or str(var) != "num_flutuante":
        x = checkId(str(var), t, escopo)
        if type(x) == int:
            if str(t.table.simbols[x].lexema) == str(var):
                if str(t.table.simbols[x].escopo) == str(escopo):
                    print(var, escopo)
                    print("Aviso: Variável "+ t.table.simbols[x].lexema + " já declarada")
                    del t.table.simbols[x]
            else:
                insertSimbol(var, t, escopo, tipo, 0, func, tam, tam2)
        else:
            insertSimbol(var, t, escopo, tipo, 0, func, tam, tam2)
            

def prefix(root, t, escopo, tipo, father, func, tam, tam2, var, dim, tamaux):
    if root:
        par = 0
        s = None
        x = None
    
        if str(root) == "atribuicao":
            expressRight(root, t, escopo, father)
            pass
            
        
        if str(root) == "retorna":
            funcao = checkId(str(escopo), t, escopo)
            folha = leaf(root)
            variavel = checkId(str(folha), t, escopo)
            if variavel == False:
                variavel = checkId(str(folha), t, "global")
              
            j = 0
            expressao = aux()
            support(root, t, root, expressao)
            for i in expressao.h:
                z = str(i).split("_")
                j += 1
                if z[0] == "operador":
                    break
            k = str(expressao.h[j-1]).split("_")

            if k[0] == "operador":
                idLeft = checkId(str(expressao.h[0]),t, escopo)
                idRight = checkId(str(expressao.h[2]),t, escopo)
                if str(t.table.simbols[idLeft].tipo) !=  str(t.table.simbols[idRight].tipo):
                    print("Aviso: Coerção implícita do valor retornado por "+ str(escopo))
            
            else:
                if type(variavel) == int:
                    if t.table.simbols[funcao].tipo == t.table.simbols[variavel].tipo:
                        pass
                    else:
                        print("Aviso: Coerção implícita do valor retornado por "+ str(escopo))
                
                else:
                    print("Aviso: Coerção implícita do valor retornado por "+ str(escopo))
                    print("Variável " + str(folha) + " não declarada.")

        if str(root) == "cabecalho":
            escopo = root.child[0].child[0]
            if str(escopo) == "principal":
               flagRet = retPrincipal(root)
               if flagRet == False:
                   print("Erro: Função principal deveria retornar inteiro, mas retorna vazio")
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
                        id = checkId(tei, t, escopo)
                        t.table.simbols[id].inicializada = True
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
                t.table.simbols[idx].inicializada = True
                if y[0] != "vazio":
                    print("Erro Semântico: Chamada à função com número de parâmetros menor que o declarado")
            if s > 1:
                t.table.simbols[idx].inicializada = True
                if s != len(root.child[0].child):
                    print("Erro Semânctico: Chamada à função com número de parâmetros menor que o declarado")
                
        if str(root) == "declaracao_variaveis":
            tipo = root.child[0].child[0]
            
        if str(root) == "lista_variaveis":
            auxVar(root, t, tipo, escopo, func, tam2, tam)
            
        
        father = root
        for son in root.child:
            prefix(son, t, escopo, tipo, father, func, tam, tam2, var, dim, tamaux)
        

def podaTree(root, father, grandpa):
    nameBreak = str(root).split("_")
    if str(root) == "declaracao_variaveis":
        father.child[0] = leaf(root.child[1])
    if str(root) == "atribuicao":
        root.child[0] = leaf(root.child[0])
        root.child[1] = root.child[1].child[0].child[0]
    if str(nameBreak[0]) == "expressao":
        if len(root.child) == 3:
            print(root)
            root.child[0] = leaf(root.child[0])
            root.child[1] = Tree(root.child[1].value)
            root.child[2] = leaf(root.child[2])
    for son in root.child:
        podaTree(son, root, father)
            


def tree_view(node, strson, father, w, i, j):
    if node != None:
        i = i + 1
        father = str(node) + " " + str(i-1) + " " +str(j-1)
        for son in node.child:
            strson = str(son) + " " + str(i) + " "   + str(j)
            w.edge(father, strson)
            j = j + 1
            tree_view(son, strson, father, w, i, j)


if __name__ == '__main__':
    from sys import argv, exit
    a = argv[1].split('/')
    f = open(argv[1])
    t = Semantica(f.read())
    prefix(t.parser.ast, t, "global", "", "", False, 0, 0, None,0, 0)
    checkRules(t)
    podaTree(t.parser.ast, "", "")
    w = Digraph('G', filename='Saidas/nozes'+a[3] + str('.gv'))
    tree_view(t.parser.ast, '', '', w, 0, 1)
    t.table.tablePrint()
    w.view()
    