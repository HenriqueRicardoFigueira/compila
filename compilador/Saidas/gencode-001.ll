; ModuleID = "./testes/geracao-codigo-testes/gencode-001.tpp"
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
  %"b" = alloca i32, align 4
  %"c" = alloca i32, align 4
  store i32 10, i32* @"a"
  store i32 5, i32* %"c"
  %"tempRight" = load i32, i32* @"a"
  %"tempLeft" = load i32, i32* %"c"
  %"tempPlus" = sub i32 %"tempRight", %"tempLeft"
  store i32 %"tempPlus", i32* %"b"
  %"var" = load i32, i32* %"b"
  call void @"escrevaInteiro"(i32 %"var")
  %"retorna" = load i32, i32* %"return", align 4
  br label %"endmain"
endmain:
  store i32 0, i32* %"return"
  %"reeet" = load i32, i32* %"return"
  ret i32 %"reeet"
}
