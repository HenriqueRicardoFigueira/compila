; ModuleID = "./testes/geracao-codigo-testes/gencode-010.tpp"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

@"n" = common global i32 0, align 4
define i32 @"fatorial"(i32 %".1") 
{
fatorial.start:
  %"n" = alloca i32, align 4
  store i32 %".1", i32* @"n"
  %"return" = alloca i32
  %"fat" = alloca i32, align 4
  %"leftvar" = load i32, i32* @"n"
  %"testecond" = icmp sgt i32 %"leftvar", 0
  br i1 %"testecond", label %"if", label %"else"
if:
  store i32 1, i32* %"fat"
  br label %"condlaco"
else:
  br label %"startfatorial"
ifend:
body:
  %"leftvar.1" = load i32, i32* @"n"
  %"iflass" = icmp eq i32 %"leftvar.1", 0
  br i1 %"iflass", label %"end", label %"condlaco"
condlaco:
  %"tempRight" = load i32, i32* %"fat"
  %"tempLeft" = load i32, i32* @"n"
  %"tempMult" = mul i32 %"tempRight", %"tempLeft"
  store i32 %"tempMult", i32* %"fat"
  %"tempRight.1" = load i32, i32* @"n"
  %"tempSub" = sub i32 %"tempRight.1", 1
  store i32 %"tempSub", i32* @"n"
  br label %"body"
end:
  br label %"ifend"
startfatorial:
  %"rightvar" = load i32, i32* %"fat"
  store i32 %"rightvar", i32* %"return"
  %"reeet" = load i32, i32* %"return"
  ret i32 %"reeet"
endfatorial:
}

define i32 @"main"() 
{
main.start:
  %"return" = alloca i32
  %".2" = call i32 @"leiaInteiro"()
  store i32 %".2", i32* @"n"
  %"var" = load i32, i32* @"n"
  call void @"escrevaInteiro"(i32 %"var")
  br label %"startmain"
startmain:
  store i32 0, i32* %"return"
  %"reeet" = load i32, i32* %"return"
  ret i32 %"reeet"
endmain:
}
