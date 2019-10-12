inteiro: T 
T:= 4

inteiro: V1[T]

inteiro somavet(inteiro: vet[], inteiro: tam)
	inteiro: result 
	result := 0

	inteiro: i 
	i := 0

	repita
		result := result + vet[i]
		i := i + 1
	até i = tam - 1

	retorna(result)	
fim

inteiro principal ()
	inteiro: x
	x := somavet(V1,T)
	retorna(0)
fim
