; ModuleID = "./testes/geracao-codigo-testes/gencode-002.tpp"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

@"a" = common global i32 0, align 4
define i32 @"main"() 
{
main.start:
  %"return" = alloca i32
  %"ret" = alloca i32, align 4
  %"leftvar" = load i32, i32* @"a"
  %"testecond" = icmp sgt i32 %"leftvar", 5
  br i1 %"testecond", label %"iftrue", label %"iffalse"
iftrue:
  br label %"ifend"
iffalse:
  br label %"ifend"
ifend:
  %"var" = load i32, i32* %"ret"
  call void @"escrevaInteiro"(i32 %"var")
  br label %"endmain"
endmain:
  %"rightvar" = load i32, i32* %"ret"
  store i32 %"rightvar", i32* %"return"
  %"reeet" = load i32, i32* %"return"
  ret i32 %"reeet"
}