
inteiro soma(inteiro: x, inteiro: y)
    retorna(x + y)
fim

inteiro sub(inteiro: z, inteiro: t)
    retorna(z + t)
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
        c := soma(soma(a,b), sub(a,b))
        escreva(c)
        i := i + 1
    até i = 5

    retorna(0)
fim
