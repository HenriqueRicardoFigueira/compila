
inteiro: A[20]

inteiro busca(inteiro: n)
	
	inteiro: retorno
	inteiro: i

	retorno := 0
	i := 0

	repita 
		se A[i] = n
			retorno := 1
		fim		
		i := i + 1
	até i = 20

	retorna(retorno)
fim

inteiro principal()

	inteiro: i

	i := 0

	repita 
		A[i] := i
		i := i + 1
	até i = 20

	leia(n)
	escreva(busca(n))
	retorno(0)
fim