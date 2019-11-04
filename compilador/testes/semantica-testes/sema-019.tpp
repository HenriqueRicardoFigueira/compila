{VERIFICAR AS DECLARAÇÕES DE VARIÁVEIS COM VÍRGULA}

inteiro: n
flutuante: x, y, z

inteiro fatorial(inteiro: n, flutuante: m)
	{NOTAÇÃO CIENTÍFICA}
	{WARNING: 'm' ESTÁ RECEBENDO VALORES DE TIPOS DIFERENTES}
	m := 5
	
	se n>0 então
		retorna(n)
	senão
		repita 
			flutuante: p
		até n = 0
	fim
	
	z := 1.9 {SEM ERRO, FOI INICIALIZADO}
	z := z+1 {ERRO, ID NAO FOI INICIALIZADO}

	{WARNING DE RETORNO: PASSANDO TIPO DIFERENTE}
	retorna(m)
fim

inteiro principal()
	leia(n)
	escreva(fatorial(1, 1.0)) {TIPOS DOS PARAMETROS DIFERENTES, TESTAR E VER SE ACUSA UM WARNING}
fim

{VERIFICAR SE A VARIÁVEL 'a' ESTÁ NO ESCOPO 'global'}

inteiro: a
flutuante: b

inteiro fatorial2(inteiro: fat, flutuante: fat2, inteiro: fat3)
	{VERIFICAÇÃO DE ATRIBUIÇÃO}

	a := 1
	{WARNING: 'a' = 'inteiro' -> ESTÁ RECEBENDO 'flutuante'}
	
	{SEM WARNING}
	

	{CHAMADA DE FUNÇÃO UMA DENTRO DA OUTRA!}
	escreva(fatorial(fatorial(1, 1.0), 1.0))

	a := fatorial(1, 1.0)

	{WARNING: VARIÁVEL 'b' é 'flutuante' E A FUNÇÃO È 'inteiro'}
	b := fatorial(1, 1.0)

	{CHAMADA DE FUNÇÃO NORMAL}
	fatorial(1, 1.0)
fim

{WARNING}

{WARNING: ID m está recebendo valores incompatíveis: flutuante -> inteiro}
{WARNING: função fatorial está retornando tipos incompatíveis: inteiro -> flutuante}
{WARNING: ID a está recebendo valores incompatíveis: inteiro -> flutuante}
{WARNING: ID b está recebendo valores incompatíveis: flutuante -> inteiro}

{RESULTADO DA TABELA DE SIMBOLOS CORRETA!}

{'fatorial': ['funcao', 'inteiro', ['inteiro', 'flutuante']],}
{'fatorial.m': ['variável', 'flutuante', 0, True],}
{'fatorial.n': ['variável', 'inteiro', 0, True],}
{'fatorial.p': ['variável', 'flutuante', 0, False],}
{'fatorial2': ['funcao', 'inteiro', ['inteiro', 'flutuante', 'inteiro']],}
{'fatorial2.fat': ['variável', 'inteiro', 0, True],}
{'fatorial2.fat2': ['variável', 'flutuante', 0, True],}
{'fatorial2.fat3': ['variável', 'inteiro', 0, True],}
{'global.a': ['variável', 'inteiro', 0, True],}
{'global.b': ['variável', 'flutuante', 0, True],}
{'global.n': ['variável', 'inteiro', 0, True],}
{'global.x': ['variável', 'flutuante', 0, False],}
{'global.y': ['variável', 'flutuante', 0, False],}
{'global.z': ['variável', 'flutuante', 0, True],}
{'principal': ['funcao', 'inteiro', []]}
