from Lexer import Lexer, Simbol
from Parser import Parser

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
        if len(root.child) == 0:
            q = str(root).split("_")
            if q[0] != "operador":
                aux.h.append(root)
        if len(root.child) > 0:
            for x in root.child:
                support(x, t, root, aux)

def expressRight(root, t, escopo, father):
    a = aux()
    support(root,t,root,a)
    if len(a.h) == 2:
        left = a.h[0]
        right = a.h[1]
        idleft = checkId(str(left), t, escopo)
        idRight = checkId(str(right), t, escopo)
        
        if idleft == False:
            idleft = checkId(str(left), t, "global")
        
        if idRight == False:
            idRight = checkId(str(right), t, "global")
        
        a = t.table.simbols[idleft]
        
        if idRight != False:
            variavelLeft = t.table.simbols[idRight]
            a.inicializada = True
            if a.tipo != variavelLeft.tipo:
                print("Aviso: Coerção implícita do valor de " + a.lexema)
        else:
            z = str(right).split("_")
            if z[0] == "num":
                if str(a.lexema) == str(left):
                    a.inicializada = True
                if str(a.tipo) == z[1]:
                    print("Aviso: Coerção implícita do valor de " + a.lexema)  

    elif len(a.h) == 3:
        left = a.h[0]
        middle = a.h[1]
        right = a.h[2]
        idleft = checkId(str(left), t, escopo)
        m = str(middle).split("_")
        o = checkId(str(middle), t, escopo)
        g = checkId(str(right), t, escopo)
        b = t.table.simbols[g]
        r = t.table.simbols[o]
        a = t.table.simbols[idleft]
        p = str(right).split("_")
        if o == False:
            if p[0] ==  "num" and m[0] == "num":
                if m[1] == p[1]:
                    if str(a.tipo) == m[1]:
                        a.inicializada = True
                    else:
                        print("Aviso: Coerção implícita do valor de " + a.lexema)
        elif g != False:
            if str(b.tipo) == str(r.tipo):
                if str(b.tipo) == str(a.tipo):
                    a.inicializada = True
                else:
                    print("Aviso: Coerção implícita do valor de " + a.lexema)
            else:
                print("Aviso: Coerção implícita do valor de " + a.lexema)

        else:
            if p[0] == "num":
                if p[1] == str(a.tipo) and str(a.tipo) == str(r.tipo):
                   a.inicializada = True
                else:
                    print("Aviso: Atribuição de tipos diferentes")      

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

def prefix(root, t, escopo, tipo, father, func, tam, tam2, var, dim, tamaux):
    if root:
        par = 0
        s = None
        x = None
    
        if str(root) == "atribuicao":
            expressRight(root, t, escopo, father)
        
        if str(root) == "retorna":
        
            funcao = checkId(str(escopo), t, escopo)
            folha = leaf(root)
            variavel = checkId(str(folha), t, escopo)
            
            if variavel == False:
                print("Erro Semântico: Variável "+ str(folha) + " não declarada.")
            
            retorno = checkId(str(variavel), t, escopo)
            
            if funcao != False:
                if t.table.simbols[funcao].tipo == t.table.simbols[retorno].tipo:
                    pass
                else:
                    print("Aviso: Coerção implícita do valor retornado por "+ str(escopo))
                #print(root.child[0])   
                #and root.child[0].child[0].child[0].child[0].child[0].child[0].child[0] != "num_inteiro":
                #print("Erro Semântico: Função Principal deveria retornar inteiro, mas retorna vazio.")
                #return
        
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
            
            if str(root.child[1].child[0].child[0].child[0]) == "indice":
                tipoIndice = leaf(root.child[1])
                
                if str(tipoIndice) != "num_inteiro":
                    print("Erro Semântico: índice de array " + str(root.child[1].child[0].child[0]) + " não inteiro")
                else:
                    insertSimbol(root.child[1].child[0].child[0], t, escopo, tipo, 1, func, tipoIndice.value, tam2)
            
            if str(root.child[1].child[0].child[0]) == "ID":
                x = checkId(root.child[1].child[0].child[0].child[0], t, escopo)
                if x != False:
                    if t.table.simbols[x].tipo:
                        print("Aviso: Variável "+ t.table.simbols[x].lexema + " já declarada")
        
        #if str(root) == "indice":
        #    var = father
        #    dim = 1
        #    if str(root.child[0]) == 'indice':
        #        dim = 2   
        #
        #if len(root.child) == 0:
        #    if str(father) == 'ID':
        #        insertSimbol(root, t, escopo, tipo, dim, func, tam, tam2)
        #    
        #    if str(root) == 'num_inteiro' or str(root) == 'num_flutuante':
        #        if dim == 2:
        #            tam2 = root.value
        #            tam = tamaux
        #        else:
        #            tam = root.value
        #            tamaux = root.value
        #        insertSimbol(var, t, escopo, tipo, dim, func, tam, tam2)
    #
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