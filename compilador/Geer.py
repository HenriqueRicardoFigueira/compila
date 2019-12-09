from Lexer import Lexer, Simbol
from Parser import Parser, Tree
from graphviz import Digraph
from llvmlite import ir
from ctypes import CFUNCTYPE, c_int32
import sys
from Semantica import Semantica, prefix, podaTree, checkRules

class Ger:
    def __init__(self, table):
        self.table = table

def walk(root, modulo, table):
    if root:
        if str(root) == "declaracao_variaveis":
            declaracaoVarGlobal(root, modulo, table)
        
        if str(root) == "declaracao_funcao":
            declaracaoFunc(root, modulo, table)
    if root.child:
        for i in range(0,len(root.child)):
            walk(root.child[i], modulo, table)


def declaracaoVarGlobal(root, modulo, table):
    tipo = root.child[0]
    
    if str(tipo) == "inteiro":
        variavel = ir.GlobalVariable(modulo, ir.IntType(32), str(root.child[1]))
        variavel.initializer = ir.Constant(ir.IntType(32), 0)
        variavel.linkage = "common"
        variavel.align = 4
    
    if str(tipo) == "flutuante":
        variavel = ir.GlobalVariable(modulo, ir.FloatType(), str(root.child[1]))
        variavel.initializer = ir.Constant(ir.FloatType(), 0.0)
        variavel.linkage = "common"
        variavel.align = 4

def declaracaoFunc(root, modulo, table):
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


if __name__ == '__main__':
    
    a = sys.argv[1].split('/')
    f = open(sys.argv[1])
    t = Semantica(f.read())
    nameprog = sys.argv[1]
    modulo = ir.Module(nameprog)
    code = Ger(t.table)
    prefix(t.parser.ast, t, "global", "", "", False, 0, 0, None,0, 0)
    checkRules(t)
    podaTree(t.parser.ast, t.parser.ast , t.parser.ast, 0)
    walk(t.parser.ast, modulo, code.table)
    #w = Digraph('G', filename='Saidas/QUBRAnozes'+a[3] + str('.gv'))
    #tree_view(t.parser.ast, '', '', w, 0, 1)
    #t.table.tablePrint()
    #w.view()
    

    arquivo = open(nameprog+'.ll','w')
    arquivo.write(str(modulo))
    arquivo.close()
    print(modulo)