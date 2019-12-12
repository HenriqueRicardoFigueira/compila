inteiro: n
inteiro: soma

inteiro principal()
	n := 10
	soma := 0
	repita
		soma := soma + n
		n := n - 1
		escreva(n)
	até n = 0
	retorna(0)
fim
