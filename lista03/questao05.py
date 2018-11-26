import Queue

tempo = 0
BRANCO = 0
CINZA = 1
PRETO = 2
INICIO = 0
FINAL = 1

def DFS(no):

    global tempo
    global listaAdjacencia
    global cores
    global distancias

    cores[no] = CINZA
    pilha = Queue.LifoQueue()
    pilha.put(no)
    tempo += 1
    distancias[no][INICIO] = tempo 

    while not pilha.empty():

        no = pilha.get()
        pilha.put(no)
        adjacenteBranco = False

        for adjacente in listaAdjacencia[no]:

            if cores[adjacente] == BRANCO:

                adjacenteBranco = True
                pilha.put(adjacente)
                tempo += 1
                distancias[adjacente][INICIO] = tempo
                cores[adjacente] = CINZA
                break
        
        if not adjacenteBranco:

            pilha.get()
            tempo += 1
            distancias[no][FINAL] = tempo
            cores[no] = PRETO

def rodaDFS(raiz):

    DFS(raiz)

    for no in listaAdjacencia.keys():

        if cores[no] == BRANCO: DFS(no)


#LEITURA DO GRAFO

listaAdjacencia = {}
cores = {}
distancias = {}
qntdArestas = int(raw_input("Quantidade de arestas:"))
print "defina as arestas:"
for aresta in xrange(qntdArestas):

    no1, no2 = map(str, raw_input().split())

    if no1 not in listaAdjacencia: 
        listaAdjacencia[no1] = [no2]
        if no2 not in listaAdjacencia: listaAdjacencia[no2] = []
        cores[no1] = BRANCO
        cores[no2] = BRANCO
        distancias[no1] = [-1,-1]
        distancias[no2] = [-1,-1]
    else: 
        listaAdjacencia[no1].append(no2)
        if no2 not in listaAdjacencia: listaAdjacencia[no2] = []
        cores[no2] = BRANCO
        distancias[no2] = [-1,-1]

raiz = raw_input("raiz:")
rodaDFS(raiz)

print distancias
print cores