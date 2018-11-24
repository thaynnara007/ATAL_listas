def findSinal(num):

    return "+" if num >= 0 else "-"

def findSequencia():

    global sizeSequencia
    global sequencia
    global sinais
    global dp

    for i in xrange(1, sizeSequencia):
        for j in xrange(i):
            
            if j == 0:
                dp[i - 1] = 1;
                sinais[i - 1] = findSinal(sequencia[j] - sequencia[i])

            elif(findSinal(sequencia[j] - sequencia[i]) != sinais[i - 1]):

                valor1 = dp[i - 1] + 1 #subestrutura otima1
                valor2 = dp[j - 1]  #subestrutura otima2
                
                if(valor2 < valor1):
                    dp[i - 1] = valor1
                    sinais[i - 1] = findSinal(sequencia[j] - sequencia[i])
            
            elif(findSinal(sequencia[j] - sequencia[i]) == sinais[i - 1]):

                valor1 = dp[i - 1] #subestrutura otima1
                valor2 = dp[j - 1]  #subestrutura otima2

                if(valor2 > valor1):
                    dp[i - 1] = valor2
                    sinais[i - 1] = sinais[j - 1]
 

sequencia = map(int, raw_input("Sequencia de inteiros:").split())
sizeSequencia = len(sequencia)

if sizeSequencia == 1: print 0
else: 

    dp = [0 for i in xrange(sizeSequencia - 1)]
    sinais = ["." for i in xrange(sizeSequencia - 1)]

    findSequencia()
    print dp 
    print dp[-1]
    

