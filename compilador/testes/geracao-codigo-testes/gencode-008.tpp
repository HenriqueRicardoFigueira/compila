inteiro: A[1024]
inteiro: B[1024]

inteiro principal()
    inteiro: a
    i := 0

    repita
        leia(a)
        A[i] := a
        i := i + 1
    até i = 1024

    repita
        B[1023 - i] := A[i]
        i := i + 1
    até i = 1024

    repita
        escreva(B[i])
        i := i + 1
    até i = 1024    

    retorna(0)
fim
