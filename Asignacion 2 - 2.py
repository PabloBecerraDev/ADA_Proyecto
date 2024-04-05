#solucion 1, esta es iterativa por lo tanto no se usa.
def sumasConPotencias(X, N):
    
    dp = [[0 for _ in range(X + 1)] for _ in range(X + 1)]       
    for i in range(X + 1):
        dp[i][0] = 1

    for i in range(1, X + 1):
        for j in range(1, X + 1):
            val = j - (i ** N)
            if val < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][val]
    return dp[X][X]



#solucion 2, esta es recursiva, asi mismo esta es la que usamos.
def formas(X, N, actual=1):
    if X == 0:
        return 1
    formas = 0
    potencia = actual ** N
    while potencia <= X:
        formas += formas(X - potencia, N, actual + 1)
        actual += 1
        potencia = actual ** N
    return formas


X = 10
N = 2
print("Número de formas de expresar", X, "como suma de potencias de", N, "es:", formas(X, N))
