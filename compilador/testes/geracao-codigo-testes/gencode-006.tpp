

inteiro soma(inteiro: a, inteiro:b)
    retorna(a + b)
fim

inteiro principal()
    inteiro: a
    inteiro: b
    inteiro: c
    inteiro: i

    i := 0

    repita
        leia(a)
        leia(b)
        c := soma(a, b)
        escreva(c)
        i := i + 1
    até i = 5

    retorna(0)
fim
