; ModuleID = "./testes/geracao-codigo-testes/gencode-007.tpp"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

define i32 @"soma"(i32 %".1", i32 %".2") 
{
soma.start:
  %"y" = alloca i32, align 4
  %"x" = alloca i32, align 4
  %"return" = alloca i32
  %"retorna" = load i32, i32* %"return", align 4
  br label %"endsoma"
endsoma:
  %"tempRight" = load i32, i32* %"x"
  %"tempLeft" = load i32, i32* %"y"
  %"tempPlus" = add i32 %"tempLeft", %"tempRight"
  store i32 %"tempPlus", i32* %"return"
  %"reeet" = load i32, i32* %"return"
  ret i32 %"reeet"
}

define i32 @"sub"(i32 %".1", i32 %".2") 
{
sub.start:
  %"t" = alloca i32, align 4
  %"z" = alloca i32, align 4
  %"return" = alloca i32
  %"retorna" = load i32, i32* %"return", align 4
  br label %"endsub"
endsub:
  %"tempRight" = load i32, i32* %"z"
  %"tempLeft" = load i32, i32* %"t"
  %"tempPlus" = add i32 %"tempLeft", %"tempRight"
  store i32 %"tempPlus", i32* %"return"
  %"reeet" = load i32, i32* %"return"
  ret i32 %"reeet"
}

define i32 @"main"() 
{
main.start:
  %"return" = alloca i32
  %"a" = alloca i32, align 4
  %"b" = alloca i32, align 4
  %"c" = alloca i32, align 4
  %"i" = alloca i32, align 4
  store i32 0, i32* %"i"
  br label %"cond"
body:
  %"leftvar" = load i32, i32* %"i"
  %"iflass" = icmp eq i32 %"leftvar", 5
  br i1 %"iflass", label %"end", label %"cond"
cond:
  %".4" = call i32 @"leiaInteiro"()
  store i32 %".4", i32* %"a"
  %".6" = call i32 @"leiaInteiro"()
  store i32 %".6", i32* %"b"
  %"arg1" = load i32, i32* %"a"
  %"arg2" = load i32, i32* %"b"
  %"TempVar" = alloca i32
  %".8" = call i32 @"soma"(i32 %"arg1", i32 %"arg2")
  store i32 %".8", i32* %"TempVar"
  %".10" = load i32, i32* %"TempVar"
  %"arg1.1" = load i32, i32* %"a"
  %"arg2.1" = load i32, i32* %"b"
  %"TempVar.1" = alloca i32
  %".11" = call i32 @"soma"(i32 %"arg1.1", i32 %"arg2.1")
  store i32 %".11", i32* %"TempVar.1"
  %".13" = load i32, i32* %"TempVar"
  %".14" = call i32 @"soma"(i32 %".10", i32 %".13")
  store i32 %".14", i32* %"c"
  %"varTemp" = load i32, i32* %"a"
  store i32 %"varTemp", i32* %"c"
  %"var" = load i32, i32* %"c"
  call void @"escrevaInteiro"(i32 %"var")
  %"tempRight" = load i32, i32* %"i"
  %"tempPlus" = add i32 1, %"tempRight"
  store i32 %"tempPlus", i32* %"i"
  br label %"body"
end:
  %".21" = call i32 @"leiaInteiro"()
  store i32 %".21", i32* %"a"
  %".23" = call i32 @"leiaInteiro"()
  store i32 %".23", i32* %"b"
  %"arg1.2" = load i32, i32* %"a"
  %"arg2.2" = load i32, i32* %"b"
  %"TempVar.2" = alloca i32
  %".25" = call i32 @"soma"(i32 %"arg1.2", i32 %"arg2.2")
  store i32 %".25", i32* %"TempVar.2"
  %".27" = load i32, i32* %"TempVar"
  %"arg1.3" = load i32, i32* %"a"
  %"arg2.3" = load i32, i32* %"b"
  %"TempVar.3" = alloca i32
  %".28" = call i32 @"soma"(i32 %"arg1.3", i32 %"arg2.3")
  store i32 %".28", i32* %"TempVar.3"
  %".30" = load i32, i32* %"TempVar"
  %".31" = call i32 @"soma"(i32 %".27", i32 %".30")
  store i32 %".31", i32* %"c"
  %"varTemp.1" = load i32, i32* %"a"
  store i32 %"varTemp.1", i32* %"c"
  %"var.1" = load i32, i32* %"c"
  call void @"escrevaInteiro"(i32 %"var.1")
  %"tempRight.1" = load i32, i32* %"i"
  %"tempPlus.1" = add i32 1, %"tempRight.1"
  store i32 %"tempPlus.1", i32* %"i"
  %"retorna" = load i32, i32* %"return", align 4
  br label %"endmain"
endmain:
  store i32 0, i32* %"return"
  %"reeet" = load i32, i32* %"return"
  ret i32 %"reeet"
}
