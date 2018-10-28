PESO = 0
VALOR = 1

def mochilaBinaria(item, valorAtual, capacidadeAtual, conjuntoAtual ):

    global capacidadeMochila
    global qntdItens
    global itens
    global conjunto
    global maiorValor

    if item < qntdItens:

        if capacidadeAtual + itens[item][PESO] > capacidadeMochila:

            if valorAtual > maiorValor:

                maiorValor = valorAtual
                conjunto = conjuntoAtual
        else:
         
            #pegar item
            if (itens[item][PESO] + capacidadeAtual) <= capacidadeMochila:

                conjuntoAtual2 = conjuntoAtual[:]
                conjuntoAtual2.append(itens[item])
                mochilaBinaria(item + 1, valorAtual + itens[item][VALOR], capacidadeAtual + itens[item][PESO], conjuntoAtual2[:])
                
            #nao pegar item
            mochilaBinaria(item + 1, valorAtual, capacidadeAtual, conjuntoAtual[:])
    else:

        if capacidadeAtual <= capacidadeMochila:

            if valorAtual > maiorValor:

                maiorValor = valorAtual
                conjunto = conjuntoAtual
    
                
capacidadeMochila = int(raw_input())
qntdItens = int(raw_input())
itens = []
conjunto = []
maiorValor = 0

for item in xrange(qntdItens):

    peso, valor = map(int, raw_input().split())
    itens.append((peso, valor))

itens.sort()  
mochilaBinaria(0,0,0,[])
print maiorValor
print conjunto
