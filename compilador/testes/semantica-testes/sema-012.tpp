{Erro: Variável 'c' não declarada}
{Aviso: Coerção implícita do valor de 'b'}
{Aviso: Coerção implícita do valor retornado por 'func'}
{Erro: Função principal deveria retornar inteiro, mas retorna vazio}

flutuante: a
inteiro: b

inteiro func()
  retorna(c)
fim

inteiro principal()
	b := 18
	a := b

	a := func()
fim
