PESO = 0
VALOR = 1

def mochilaBinaria( valorAtual, capacidadeAtual, i, conjuntoAtual):

    global capacidadeMochila
    global itens
    global qntdItens
    global conjunto
    global maiorValor

    if i <= qntdItens:

        if capacidadeAtual <= capacidadeMochila:
          
            if valorAtual > maiorValor:

                maiorValor = valorAtual
                conjunto = conjuntoAtual
        
        for iten in xrange(i, qntdItens):
    
           # Parte abaixo necessária pois em python, não é passado listas como parámetros, mas sim a referência para a lista, implicitamente,
           #o que ocaciona da lista continuar modificada por chamadas recursivas a frente, mesmo depois de ter voltado na recursão
           #gerando um comportamento inesperado tendo em vista a teoria da recursão.
            conjuntoAtual2 = conjuntoAtual[:]
            conjuntoAtual2.append(itens[iten])
            
            mochilaBinaria( itens[iten][VALOR] + valorAtual, capacidadeAtual + itens[iten][PESO], iten + 1, conjuntoAtual2) 
            

capacidadeMochila = int(raw_input())
qntdItens = int(raw_input())
itens = []
maiorValor = 0
conjunto = []


for iten in xrange(qntdItens):

    peso, valor = map(int, raw_input().split())
    itens.append((peso, valor))

itens.sort()

mochilaBinaria(0,0,0,[])

print maiorValor
print conjunto




