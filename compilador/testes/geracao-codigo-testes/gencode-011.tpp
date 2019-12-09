{Condicional com operadores lógicos}
inteiro: a

inteiro principal()
	inteiro: b
	a := 10 
	se (a >= 5) && (a <= 20) então
		b := 50	
	senão
		b := 100
  	fim

  	escreva(b)
  	retorna(0)
fim
