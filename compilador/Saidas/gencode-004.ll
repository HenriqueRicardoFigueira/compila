; ModuleID = "./testes/geracao-codigo-testes/gencode-004.tpp"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

@"n" = common global i32 0, align 4
@"soma" = common global i32 0, align 4
define i32 @"main"() 
{
main.start:
  %"return" = alloca i32
  store i32 10, i32* @"n"
  store i32 0, i32* @"soma"
  %"leftvar" = load i32, i32* @"n"
  br label %"body"
body:
  %"tempRight" = load i32, i32* @"soma"
  %"tempLeft" = load i32, i32* @"n"
  %"tempPlus" = add i32 %"tempLeft", %"tempRight"
  store i32 %"tempPlus", i32* @"soma"
  %"tempRight.1" = load i32, i32* @"n"
  %"tempPlus.1" = sub i32 %"tempRight.1", 1
  store i32 %"tempPlus.1", i32* @"n"
  %"var" = load i32, i32* @"n"
  call void @"escrevaInteiro"(i32 %"var")
  br label %"cond"
cond:
  %"iflass" = icmp eq i32 %"leftvar", 0
  br i1 %"iflass", label %"end", label %"body"
end:
  %"retorna" = load i32, i32* %"return", align 4
  br label %"endmain"
endmain:
  store i32 0, i32* %"return"
  %"reeet" = load i32, i32* %"return"
  ret i32 %"reeet"
}
