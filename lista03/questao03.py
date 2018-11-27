def numBinomial(n, k):

    global dp

    for i in xrange(0, n):

        for j in xrange(k , 0, -1):

            dp[j] = dp[j] + dp[j - 1] #subestrutura otima
    
    return d[-1]


n = int(raw_input("n:"))
k = int(raw_input("k:"))
dp = [0 for i in xrange(k + 1)]
dp[0] = 1 #caso base

numBinomial(n,k)
print dp
print "c(%d, %d) = %d" %(n,k,dp[-1])