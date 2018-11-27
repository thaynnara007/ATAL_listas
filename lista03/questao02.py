def casoBase():
    
    global dp
    global sizeSequencia1
    global sizeSequencia2

    for i in xrange(sizeSequencia2 + 1):
        for j in xrange(sizeSequencia1 + 1):

            if j == 0: dp[i][j] = i
            elif i == 0: dp[i][j] = j

def findOperacoes():

    global sequencia1
    global sequencia2
    global sizeSequencia1
    global sizeSequencia2
    global dp

    for i in xrange(1, sizeSequencia2 + 1):
        for j in xrange(1, sizeSequencia1 + 1):

            if  sequencia2[i- 1] == sequencia1[j - 1]: dp[i][j] = dp[i - 1][j - 1] #subestrutura otima
            else: dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i -1][j - 1] + 1) #subestrutura otima
    
    return d[-1][-1]

sequencia1 = raw_input("sequencia1:")
sequencia2 = raw_input("sequencia2:")
sizeSequencia1 = len(sequencia1)
sizeSequencia2 = len(sequencia2)

dp = [[0 for j in xrange(sizeSequencia1 + 1)] for i in xrange(sizeSequencia2 + 1)]

casoBase()
findOperacoes()

print dp
print "Quantidade de operacoes necessarias: %d" %dp[-1][-1]
