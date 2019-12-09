flutuante: A[1024]
flutuante: B[1024]
flutuante: C[1024]

somaVetores(inteiro: n)
    inteiro: i
    i := 0
    repita
        C[i] := A[i] + B[i]
        i := i + 1
    até i = n 
fim

inteiro principal()
    inteiro: i
    i := 0
    repita
        A[i] := 1
        B[i] := 1
        i := i + 1
    até i = 1024

    somaVetores(1024)

    i := 0
    repita
        escreva(C[i])
        i := i + 1
    até i = 1024

    retorna(0)
fim
