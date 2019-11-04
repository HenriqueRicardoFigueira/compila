{Erro: Chamada à função 'func' com número de parâmetros menor que o declarado}
{Erro: Função principal deveria retornar inteiro, mas retorna vazio}

inteiro func(inteiro: x, inteiro: y)
	retorna(x + y)
fim

inteiro principal()
	inteiro: a
	a := func(10)
fim
