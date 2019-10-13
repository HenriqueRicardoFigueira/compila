inteiro: n, g

inteiro fatorial(inteiro: n)
	flutuante: d
	d := 5.6 
	inteiro: fat
	se n > 10 então
		se n > 0 então {não calcula se n > 0}
			fat := 1
			repita
				repita
					fat := fat * n
				até n = 0
				fat := fat * n
			até n = 0
		senão
			fat := 5
		fim
	fim
	inteiro: teste
	teste := (5+10)*14
	teste := 5+10*14
	teste := -5-(1+5)
	teste := 5-1
	teste := 10*8
fim

inteiro principal()
	leia(n)
	escreva(fatorial(fatorial(1)))
fim

1+2