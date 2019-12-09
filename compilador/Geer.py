from Lexer import Lexer, Simbol
from Parser import Parser, Tree
from graphviz import Digraph
from llvmlite import ir
from ctypes import CFUNCTYPE, c_int32
import sys
from Semantica import Semantica, prefix, podaTree, checkRules, checkId, leaf

class Ger:
    def __init__(self, table):
        self.table = table
        self.ponteirosVar = []
        self.ponteirosFunc = []

    def walk(self, root, modulo, escopo):
        if root:
            if str(root) == "declaracao_variaveis":

                if escopo == "global":
                    self.declaracaoVarGlobal(root, modulo)

                else: 
                    pass
                
            if str(root) == "declaracao_funcao":
                escopo = root.child[1].child[0]
                self.declaracaoFunc(root, modulo, escopo)

        if root.child:

            for i in range(0,len(root.child)):
                self.walk(root.child[i], modulo, escopo)

    
    def searchVar(self, name):
        for i in self.ponteirosVar:
            if i.name == name:
                return i
    
    def atrib(self, root, modulo, builder, escopo):
        left = self.searchVar(str(root.child[0]))
        auxright = root.child[1].child[0]
        if len(auxright.child) == 1:
            right = leaf(auxright)
            
            if str(right) == "num_inteiro":
                varRight = ir.Constant(ir.IntType(32), int(right.value))
                builder.store(varRight, left)
            
            elif str(right) == "num_flutuante":
                varRight = ir.Constant(ir.FloatType(), float(right.value))
                builder.store(varRight, left)
            
            else:
                varRight = self.searchVar(str(right))
                varTemp = builder.load(varRight, "varTemp")
                builder.store(varTemp, left)
        
        if len(auxright.child) == 3:
            if str(auxright.child[0]) != "num_inteiro" or str(auxright.child[0]) != "num_flutuante":
              sideRight = self.searchVar(str(auxright.child[0]))
              tempRight = builder.load(sideRight, name='tempRight')
            
            elif str(auxright.child[0]) == "num_inteiro":
                tempRight = ir.Constant(ir.IntType(32), int(auxright.child[0].value))
            
            elif str(auxright.child[0]) == "num_float":
                tempRight = ir.Constant(ir.FloatType(), float(auxright.child[0].value))
            
            if str(auxright.child[2]) != "num_inteiro" or str(auxright.child[2]) != "num_flutuante":
              sideLeft = self.searchVar(str(auxright.child[2]))
              tempLeft = builder.load(sideLeft, name='tempLeft')
            
            elif str(auxright.child[2]) == "num_inteiro":
                tempLeft = ir.Constant(ir.IntType(32), int(auxright.child[2].value))
            
            elif str(auxright.child[2]) == "num_float":
                tempLeft = ir.Constant(ir.FloatType(), float(auxright.child[2].value))
            
            
            if str(auxright.child[1]) == "+":
                tempPlus = builder.add(tempLeft, tempRight, name="tempPlus")
            
            if str(auxright.child[1]) == "-":
                tempPlus = builder.sub(tempLeft, tempRight, name="tempPlus")



    def walkFunc(self, root, modulo, builder, ret, escopo):
        if root:

            if str(root) == "declaracao_variaveis":
                self.declaracaoVarLocal(root, modulo, builder)

            if str(root) == "atribuicao":
                self.atrib(root, modulo, builder, escopo)

            for i in range(0, len(root.child)):
                self.walkFunc(root.child[i], modulo, builder, ret, escopo)

    def declaracaoVarLocal(self, root, modulo, builder):
        tipo = root.child[0]

        if str(tipo) == "inteiro":
            variavel = builder.alloca(ir.IntType(32), name=str(root.child[1]))
            variavel.align = 4
            self.ponteirosVar.append(variavel)

        if str(tipo) == "flutuante":
            variavel = builder.alloca(ir.FloatType(), name=str(root.child[1]))
            variavel.align = 4
            self.ponteirosVar.append(variavel)

    def declaracaoVarGlobal(self, root, modulo):
        tipo = root.child[0]

        if str(tipo) == "inteiro":
            variavel = ir.GlobalVariable(modulo, ir.IntType(32), str(root.child[1]))
            variavel.initializer = ir.Constant(ir.IntType(32), 0)
            variavel.linkage = "common"
            variavel.align = 4
            self.ponteirosVar.append(variavel)

        if str(tipo) == "flutuante":
            variavel = ir.GlobalVariable(modulo, ir.FloatType(), str(root.child[1]))
            variavel.initializer = ir.Constant(ir.FloatType(), 0.0)
            variavel.linkage = "common"
            variavel.align = 4
            self.ponteirosVar.append(variavel)

    def declaracaoFunc(self, root, modulo, escopo):
        if str(root.child[1].child[0]) == "principal":
            name = "main"

        if str(root.child[0]) == "inteiro":
            returnType = ir.IntType(32)

        else:
            returnType = ir.FloatType()

        funcType = ir.FunctionType(returnType,[])
        func = ir.Function(modulo, funcType, name=name)
        blockStart = func.append_basic_block('%s.start' % name)
        builder = ir.IRBuilder(blockStart)
        ret = builder.alloca(returnType, name='return')
        self.ponteirosFunc.append(func)
        self.walkFunc(root, modulo, builder, ret, escopo)


if __name__ == '__main__':
    
    a = sys.argv[1].split('/')
    f = open(sys.argv[1])
    t = Semantica(f.read())
    nameprog = sys.argv[1]
    modulo = ir.Module(nameprog)
    prefix(t.parser.ast, t, "global", "", "", False, 0, 0, None,0, 0)
    checkRules(t)
    x = Ger(t.table)
    podaTree(t.parser.ast, t.parser.ast , t.parser.ast, 0)
    x.walk(t.parser.ast, modulo, "global")
    #w = Digraph('G', filename='Saidas/QUBRAnozes'+a[3] + str('.gv'))
    #tree_view(t.parser.ast, '', '', w, 0, 1)
    #t.table.tablePrint()
    #w.view()
    

    #arquivo = open(nameprog+'.ll','w')
    #arquivo.write(str(modulo))
    #arquivo.close()
    print(modulo)