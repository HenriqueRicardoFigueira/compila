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
  store i32 10, i32* @"a"
  %"leftvar" = load i32, i32* @"a"
  %"testecond" = icmp sgt i32 %"leftvar", 5
  br i1 %"testecond", label %"if", label %"end"
if:
  store i32 1, i32* %"ret"
  br label %"end"
end:
  %"var" = load i32, i32* %"ret"
  call void @"escrevaInteiro"(i32 %"var")
  br label %"startmain"
startmain:
  %"rightvar" = load i32, i32* %"ret"
  store i32 %"rightvar", i32* %"return"
  %"reeet" = load i32, i32* %"return"
  ret i32 %"reeet"
}
