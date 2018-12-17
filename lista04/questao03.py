import Queue

INF = 10000000000

def findPath(procurado):

    global pais;
    path = str(procurado)
    no = procurado
    pai = pais[no] 

    while no != pai:
        path = (str(pai) + " -> ") + path
        no = pai
        pai = pais[pai]

    print path


def Dijkstra(root, procurado):

    global listaAdjacentes
    global distancias
    global pais

    fila = Queue.PriorityQueue()
    distancias[root] = 0
    par = (distancias[root], root)
    fila.put(par)
   
    while not fila.empty():

        _,topo = fila.get()
    
        if topo != procurado:
            if topo in listaAdjacentes:
                for peso, adjacente in listaAdjacentes[topo]:
                    if distancias[topo] + peso < distancias[adjacente]:
                        
                        distancias[adjacente] = distancias[topo] + peso
                        pais[adjacente] = topo
                        par = (distancias[adjacente], adjacente)
                        fila.put(par)
        else: 
            print "Menor caminho:"
            findPath(procurado)
            print "custo: %d" %distancias[procurado]
            break
    

#Leitura do grafo direcionado
listaAdjacentes = {}
distancias = {}
pais = {}

qntdNos, qntdArestas = map(int, raw_input("quantidade vertices e quantidade de arestas:").split())

print "vertice1, vertice2, peso"
for aresta in xrange(qntdArestas):

    no1, no2, peso = raw_input().split()
    peso = int(peso)

    if no1 not in listaAdjacentes:
        listaAdjacentes[no1] = [(peso,no2)]
        distancias[no1] = INF
        pais[no1] = no1
    else: listaAdjacentes[no1].append((peso,no2))

root = raw_input("vertice inicial: ")
procurado = raw_input("vertice final: ")
Dijkstra(root, procurado)

