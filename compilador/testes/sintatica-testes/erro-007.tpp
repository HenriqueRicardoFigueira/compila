inteiro: a[1024]
inteiro: c[1024]
inteiro: c[1024]

init()
    inteiro: i
    i := 1
    repita
        a[i] = 1
        b[i] = 1
        i := i + 1
    até i = 1024
fim

vecAdd()    
    inteiro: i
    i := 1
    repita
        c[i] := a[i] + b[i]
        i := i + 1
    até i = 1024
fim

imprimir()    
    inteiro: i
    i := 1
    repita
        escreva(c[i])
        i := i + 1
    até i = 1024
fim

inteiro principal()
    init()
    vecAdd()
    imprimir()
    
    retorna(0)
fim
