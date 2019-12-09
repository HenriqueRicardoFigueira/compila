{Maior de 4 número: contribuição do Kawamoto}

inteiro maiorde2(inteiro:x,y)
	se (x > y) então
		retorna(x)
	fim
	retorna(y)
fim

inteiro maiorde4(inteiro:a,b,c,d)
	retorna(maiorde2(maiorde2(a,b),maiorde2(c,d)))
fim

inteiro principal()
	inteiro: A,B,C,D
	
	leia(A)
	leia(B)
	leia(C)
	leia(D)
	
	escreva(maiorde4(A,B,C,D))	

  	retorna(0)
fim
