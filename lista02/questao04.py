import math

def distancia(x1,y1,x2,y2):

    v1 = pow((x2 - x1), 2)
    v2 = pow((y2 - y1), 2)
    r = math.sqrt((v1 + v2))

    return r

def calculaMenorDistancia():

    global pontos
    global distancias
    global qntdPontos
    global menorDistancia

    for i in xrange(qntdPontos):

        for j in xrange(qntdPontos):

            ponto = pontos[i]
            ponto2 = pontos[j]

            if ponto != ponto2:

                d = distancia(ponto[0], ponto[1], ponto2[0], ponto2[1])

                if d < menorDistancia: menorDistancia = d

                if d in distancias: 
         
                    x = (ponto2, ponto)

                    if not( x in distancias[d]):
                        distancias[d].add((ponto, ponto2))

                else: distancias[d] = set([(ponto, ponto2)])

INF = 100000000000000
qntdPontos = int(raw_input())
pontos = []
distancias = {}
menorDistancia = INF

for ponto in xrange(qntdPontos):

    x,y = map(int, raw_input().split())
    pontos.append((x,y))

calculaMenorDistancia()

print "menor distancia: %.4f" %menorDistancia
for ponto in distancias[menorDistancia]:

    print "pontos: ", ponto

