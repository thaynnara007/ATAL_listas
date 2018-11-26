import Queue
BRANCO = 0
CINZA = 1
PRETO = 2
INF = 10000000

def BFS(no):

    global listaAdjacencia
    global cores
    global distancias

    fila = Queue.Queue()
    fila.put(no)
    cores[no] = CINZA
    distancias[no] = 0

    while not fila.empty():

        no = fila.get()

        for adjacente in listaAdjacencia[no]:

            if cores[adjacente] == BRANCO:

                fila.put(adjacente)
                cores[adjacente] = CINZA
                distancias[adjacente] = distancias[no] + 1
        
        cores[no] = PRETO
        

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
        distancias[no1] = INF
        distancias[no2] = INF
    else: 
        listaAdjacencia[no1].append(no2)
        if no2 not in listaAdjacencia: listaAdjacencia[no2] = []
        cores[no2] = BRANCO
        distancias[no2] = INF

u = raw_input("u:")
v = raw_input("v:")

BFS(u)
if distancias[v] != INF: print "Existe um caminho de %s a %s, e a distancia eh: %d" %(u,v,distancias[v])
else: print "Nao existe caminho entre %s e %s" %(u,v)