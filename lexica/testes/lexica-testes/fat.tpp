inteiro: n
flutuante: a[10]

inteiro fatorial(inteiro: n)
    inteiro: fat
    se n > 0 então {não calcula se n > 0}
        fat := 1
        repita
            fat := fat * n
            n := n - 1
        até n = 0
        retorna(fat) {retorna o valor do fatorial de n}
    senão
        retorna(0)
    fim
fim
 $$
{asdsa}
{

asdasdasdasdasdas


}

inteiro principal()
    leia(n)
    escreva(fatorial(n))
    retorna(0)
fim


