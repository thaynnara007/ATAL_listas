
def transposta():

        global listaAdjacencia
        listaAdjacenciaTransposta = {}
        
        for vertice1 in listaAdjacencia.keys():
                for vertice2 in listaAdjacencia[vertice1]:

                        if vertice1 not in  listaAdjacenciaTransposta: listaAdjacenciaTransposta[vertice1] = []
                        if vertice2 not in listaAdjacenciaTransposta: listaAdjacenciaTransposta[vertice2] = [vertice1]
                        else: listaAdjacenciaTransposta[vertice2].append(vertice1)
        
        return listaAdjacenciaTransposta

def myDfs(no, raiz, componente):

    global listaTransposta
    global visitados
    
    visitados[no] = True
    result = False

    for adjacente in listaTransposta[no]:
        
        if not visitados[adjacente]: result = myDfs(adjacente, raiz, componente)
        else: 
            if adjacente == raiz: 
                result = True
  
    return result

def ehFortementeConectado(componente):

    global visitados
   
    result = myDfs(componente[0], componente[0], componente)

    for vertice in componente:
        result = result and visitados[vertice]
   
    return result

def grafoFortementeConectado(componentes):

    result = True

    for componente in componentes:

        r = ehFortementeConectado(componente)
        result = result and r
    
    return result


#LEITURA DO GRAFO

listaAdjacencia = {}
visitados = {}
qntdArestas = int(raw_input("Quantidade de arestas:"))
print "defina as arestas:"
for aresta in xrange(qntdArestas):

    no1, no2 = map(str, raw_input().split())

    if no1 not in listaAdjacencia: 
        listaAdjacencia[no1] = [no2]
        if no2 not in listaAdjacencia: listaAdjacencia[no2] = []
        visitados[no1] = False
        visitados[no2] = False
    else: 
        listaAdjacencia[no1].append(no2)
        if no2 not in listaAdjacencia: listaAdjacencia[no2] = []
        visitados[no2] = False
    
quntComponentes = int(raw_input("Quantidade componentes:"))
componentes = [0] * quntComponentes
for i in xrange(quntComponentes):
    componente = raw_input("componente:").split()
    componentes[i] = componente

listaTransposta = transposta()
r = grafoFortementeConectado(componentes)
print "True" if r else "False"