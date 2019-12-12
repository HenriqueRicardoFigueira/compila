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

    def searchFunc(self, name):
        for i in self.ponteirosFunc:
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
            if str(auxright.child[0]) != "num_inteiro" and str(auxright.child[0]) != "num_flutuante":
              sideRight = self.searchVar(str(auxright.child[0]))
              tempRight = builder.load(sideRight, name='tempRight')
            
            elif str(auxright.child[0]) == "num_inteiro":
                tempRight = ir.Constant(ir.IntType(32), int(auxright.child[0].value))
            
            elif str(auxright.child[0]) == "num_float":
                tempRight = ir.Constant(ir.FloatType(), float(auxright.child[0].value))
            
            if str(auxright.child[2]) != "num_inteiro" and str(auxright.child[2]) != "num_flutuante":
              sideLeft = self.searchVar(str(auxright.child[2]))
              tempLeft = builder.load(sideLeft, name='tempLeft')
            
            elif str(auxright.child[2]) == "num_inteiro":
                tempLeft = ir.Constant(ir.IntType(32), int(auxright.child[2].value))
            
            elif str(auxright.child[2]) == "num_float":
                tempLeft = ir.Constant(ir.FloatType(), float(auxright.child[2].value))
            
            
            if str(auxright.child[1]) == "+":
                tempPlus = builder.add(tempLeft, tempRight, name="tempPlus")
                x = builder.load(tempPlus, name="x")
                esc = builder.load(left, name="esc")
                builder.store(tempPlus, left)
            
            if str(auxright.child[1]) == "-":
                tempPlus = builder.sub(tempRight, tempLeft, name="tempPlus")
                builder.store(tempPlus, left)



    def walkFunc(self, root, modulo, builder, ret, escopo):
        if root:

            if str(root) == "declaracao_variaveis":
                self.declaracaoVarLocal(root, modulo, builder)

            if str(root) == "retorna":
                self.retorna(root,modulo,builder)

            if str(root) == "atribuicao":
                self.atrib(root, modulo, builder, escopo)
            
            if str(root) == "repita":
                self.lass(root, modulo, builder, escopo)

            if str(root) == "chamada_funcao":
                print(root.value)
                if len(root.child) == 1:
                    var = leaf(root.child[0])
                    vaar = self.searchVar(str(var))
                    func = self.searchFunc(str(root.value))
                    a = []
                    a.append(builder.load(vaar, "no"))
                    builder.call(func, a)
            
            if str(root) == "escreva":    
                if len(root.child[0].child) == 1:
                    varEscreva = self.searchVar(str(leaf(root)))
                    funcInt = self.searchFunc("escrevaInteiro")
                    func = self.searchFunc("escrevaFlutuante")
            
                    a = []
                    a.append(builder.load(varEscreva, "var"))
                    print(a)
                    #if varEscreva.type == ir.IntType(32):
                    
                    builder.call(funcInt, a)  
                    #if varEscreva.type != "i32":
                    #    builder.call(func, a)

            
            if str(root) == "leia":
                varLer = self.searchVar(str(root.value))
                funcInt = self.searchFunc("leiaInteiro")
                func = self.searchFunc("leiaFlutuante")
                a = []
                #if varLer.type == ir.IntType(32):
                builder.store(builder.call(funcInt, a), varLer )

                #else:
                #    builder.call(func, a)

            for i in range(0, len(root.child)):
                self.walkFunc(root.child[i], modulo, builder, ret, escopo)

    def lass(self, root, modulo, builder, escopo):
        start = self.ponteirosFunc[-1].append_basic_block("body")
        cond = self.ponteirosFunc[-1].append_basic_block("cond")
        stop = self.ponteirosFunc[-1].append_basic_block("end")
        body = root.child[0]
        express = root.child[1]
        leftSide = express.child[0]
        leftVar = self.searchVar(str(leftSide))
        TempVar = builder.load(leftVar, name="leftvar")
        
        if str(express.child[2]) != "num_inteiro" and str(express.child[2]) != "num_flutuante": 
            rightVar = self.searchVar(str(express.child[2]))
            TempVarRight = builder.load(rightVar, name="rightvar")
        
        elif str(express.child[2]) == "num_inteiro":
            TempVarRight = ir.Constant(ir.IntType(32), int(express.child[2].value))

        elif str(express.child[2]) == "num_flutuante":
            TempVarRight = ir.Constant(ir.FloatType(), int(express.child[2].value))

        if str(express.child[1]) == "=":
            op = "=="

        builder.position_at_end(start)
        builder.branch(cond)
        builder.position_at_end(cond)
        laco = builder.icmp_signed(op, TempVar, TempVarRight, name="iflass")
        builder.cbranch(laco, start, stop)
        builder.position_at_end(stop)

    def retorna(self, root, modulo, builder):
        r = self.searchVar("return")
        ret = builder.load(r, name="retorna", align=4)
        name = self.ponteirosFunc[-1].name
        stop = self.ponteirosFunc[-1].append_basic_block("end"+name)
        builder.branch(stop)
        builder.position_at_end(stop)
        express = root.child[0].child[0]
        
        if len(express.child) == 1:
            aux = leaf(express.child[0])
            if str(aux) != "num_inteiro" and str(aux) != "num_flutuante": 
                rightVar = self.searchVar(str(leaf(aux)))
                TempVarRight = builder.load(rightVar, name="rightvar")
        
            elif str(aux) == "num_inteiro":
                TempVarRight = ir.Constant(ir.IntType(32), int(aux.value) )
            
            elif str(aux) == "num_flutuante":
                TempVarRight = ir.Constant(ir.FloatType(), int(aux.value))
            
            rets = self.searchVar("return")
            builder.store(TempVarRight, rets)
            builder.ret(builder.load(rets,name="reeet"))
        
        #else:
        #    if str(express.child[0]) != "num_inteiro" and str(express.child[0]) != "num_flutuante":
        #        sideRight = self.searchVar(str(express.child[0]))
        #        tempRight = builder.load(sideRight, name='tempRight')
        #    
        #    elif str(express.child[0]) == "num_inteiro":
        #        tempRight = ir.Constant(ir.IntType(32), int(express.child[0].value))
        #    
        #    elif str(express.child[0]) == "num_float":
        #        tempRight = ir.Constant(ir.FloatType(), float(express.child[0].value))
        #    
        #    if str(express.child[2]) != "num_inteiro" and str(express.child[2]) != "num_flutuante":
        #      sideLeft = self.searchVar(str(express.child[2]))
        #      tempLeft = builder.load(sideLeft, name='tempLeft')
        #    
        #    elif str(express.child[2]) == "num_inteiro":
        #        tempLeft = ir.Constant(ir.IntType(32), int(express.child[2].value))
        #    
        #    elif str(express.child[2]) == "num_float":
        #        tempLeft = ir.Constant(ir.FloatType(), float(express.child[2].value))
        #    
        #    
        #    if str(express.child[1]) == "+":
        #        tempPlus = builder.add(tempLeft, tempRight, name="tempPlus")
        #    
        #    if str(express.child[1]) == "-":
        #        tempPlus = builder.sub(tempLeft, tempRight, name="tempPlus")
#


      
        
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
        else:
            name = str(root.child[1].child[0])

        if str(root.child[0]) == "inteiro":
            returnType = ir.IntType(32)

        else:
            returnType = ir.FloatType()

        funcType = ir.FunctionType(returnType,[])
        func = ir.Function(modulo, funcType, name=name)
        blockStart = func.append_basic_block('%s.start' % name)
        builder = ir.IRBuilder(blockStart)
        ret = builder.alloca(returnType, name='return')
        self.ponteirosVar.append(ret)
        self.ponteirosFunc.append(func)
        self.walkFunc(root, modulo, builder, ret, escopo)
    
    def start(self, module):
        escrevaInteiro = ir.Function(module,ir.FunctionType(ir.VoidType(), [ir.IntType(32)]),name="escrevaInteiro")
        self.ponteirosFunc.append(escrevaInteiro)
        escrevaFlutuante = ir.Function(module,ir.FunctionType(ir.VoidType(),[ir.FloatType()]),name="escrevaFlutuante")
        self.ponteirosFunc.append(escrevaFlutuante)
        leiaInteiro = ir.Function(module,ir.FunctionType(ir.IntType(32),[]),name="leiaInteiro")
        self.ponteirosFunc.append(leiaInteiro)
        leiaFlutuante = ir.Function(module,ir.FunctionType(ir.FloatType(),[]),name="leiaFlutuante")
        self.ponteirosFunc.append(leiaFlutuante)

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
    x.start(modulo)
    x.walk(t.parser.ast, modulo, "global")
    #w = Digraph('G', filename='Saidas/QUBRAnozes'+a[3] + str('.gv'))
    #tree_view(t.parser.ast, '', '', w, 0, 1)
    #t.table.tablePrint()
    #w.view()
    
    z = nameprog.split('/')
    o = z[3].split('.')
    arquivo = open('Saidas/'+o[0]+'.ll','w')
    arquivo.write(str(modulo))
    arquivo.close()
    print(modulo)