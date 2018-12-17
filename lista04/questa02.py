#dfs
BRANCO = 1
CINZA = 2
PRETO = 3

def myDFS(no):

    global listaAdjacencia
    global cor

    cor[no] = CINZA
    temCiclo = False
 
    for adjacente in listaAdjacencia[no]:

        if cor[adjacente] == BRANCO: temCiclo = temCiclo or myDFS(adjacente)
        elif cor[adjacente] == PRETO: temCiclo = True
    
    cor[no] = PRETO    
    return temCiclo

#lendo o grafo nao direcionado
qntdNos, qntdArestas = map(int, raw_input("quantidade de vertices, quantidade de arestas:").split())
cor = {}
listaAdjacencia = {}
print "no1, no2:"
for aresta in xrange(qntdArestas):

    no1, no2 = raw_input().split()

    if no1 not in listaAdjacencia:
        listaAdjacencia[no1] = [no2]
        cor[no1] = BRANCO
    else: listaAdjacencia[no1].append(no2)

    if no2 not in listaAdjacencia:
        listaAdjacencia[no2] = [no1]
        cor[no2] = BRANCO
    
    else: listaAdjacencia[no2].append(no1)

root = raw_input("escolha o vertice inicial:")
print myDFS(root)