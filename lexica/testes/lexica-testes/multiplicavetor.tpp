flutuante: V[100]
flutuante: V2[100]

multivet(inteiro: t)
	inteiro: i
	i := 0
	repita
		V2[i] = V[i] * 2
		i := i + 1
	até i = t
fim

inteiro principal ()
	inteiro: i
	i := 0
	repita
		V[i] := i+1
		i := i + 1
	até i = 100

	multivet(100)
