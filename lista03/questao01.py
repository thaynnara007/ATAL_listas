def findSequencia():

    global sequencia
    global sizeSequencia
    global dp
    global sinal

    for i in xrange(sizeSequencia - 3, -1, -1):
        sinalAtual = "+" if sequencia[i] > sequencia[i + 1] else "-"
    
        if sinal != sinalAtual: dp[i] = dp[i + 1] + 1
        else: dp[i] = dp[i + 1]
        
        sinal = sinalAtual
    

sequencia = map(int, raw_input("Sequencia de inteiros:").split())
sizeSequencia = len(sequencia)

if len == 1: print 0
else: 

    dp = [0 for i in xrange(sizeSequencia)]
    dp[sizeSequencia -2] = 1;

    sinal = "+" if sequencia[-2] > sequencia[-1] else "-"
    findSequencia()

print dp[0] 
