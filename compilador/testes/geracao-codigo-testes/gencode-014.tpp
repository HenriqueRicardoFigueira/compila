{Fibonacci}

{Fibonacci Recursivo}
inteiro fibonacciRec(inteiro: n)
	se (n <= 1) então
		retorna(n)
	senão
		retorna(fibonacciRec(n - 1) + fibonacciRec(n - 2))
	fim
fim

{Fibonacci Iterativo}
inteiro fibonacciIter(inteiro: n)
	inteiro: i, f, k
	i := 1
	f := 0
	k := 1

	repita
		f := i + f
		i := f - i
		k := k + 1
	até (k <= n)

	retorna(f)
fim

inteiro principal()
	inteiro: n, i
		
	leia(n)

	i := 1
	repita
		escreva(fibonacciIter(i))
		i := i + 1
	até(i < n)
	
	i := 1
	repita
		escreva(fibonacciRec(i))
		i := i + 1
	até(i < n)

	retorna(0)
fim
