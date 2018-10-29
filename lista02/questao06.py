
PESO = 1
VALOR = 2

def fraciona(capacidadeAtual, item, espacoSobrando):

    global capacidadeMochila
    global itens

    result = (espacoSobrando * itens[item][VALOR]) / itens[item][PESO]
    
    return result

def mochilaFracionaria():

    global itens
    global qntdItens
    global capacidadeMochila
    melhorValor = 0
    capacidadeAtual = 0

    for item in xrange(qntdItens):

        if capacidadeAtual >= capacidadeMochila: break 

        if itens[item][PESO] + capacidadeAtual <= capacidadeMochila:

            melhorValor += itens[item][VALOR]
            capacidadeAtual += itens[item][PESO]
        
        else:

            espacoSobrando = capacidadeMochila - capacidadeAtual
            melhorValor += fraciona(capacidadeAtual, item, espacoSobrando)
            capacidadeAtual += espacoSobrando
    
    return melhorValor

capacidadeMochila = int(raw_input())
qntdItens = int(raw_input())
itens = []

for item in xrange(qntdItens):

    peso, valor = map(float, raw_input().split())
    itens.append(((valor/peso), peso, valor))

itens.sort(reverse = True)

print mochilaFracionaria()

