inteiro: vet[10]
inteiro: tam

tam := 10

{ preenche o vetor no pior caso }
preencheVetor()
  inteiro: i
  inteiro: j
  i := 0
  j := tam
  repita
    vet[i] = j
    i := i + 1
    j := j - 1
  até i < tam
fim

{ implementação do bubble sort }
bubble_sort()
  inteiro: h
  h := 0
  repita
    inteiro: k
    k := 0
    repita
      se vet[h] > v[k] então
        inteiro: temp
        temp := vet[h]
        vet[h] := vet[k]
        vet[k] := temp
      fim
      k := k + 1
    até k < h
    h := h + 1
  até h < tam
fim

{ programa principal }
inteiro principal()
  preencheVetor()
  bubble_sort()
  retorna(0)
fim
