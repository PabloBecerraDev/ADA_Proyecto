
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
resultado = fibonacci(10)
print(resultado)



def fibonacciList(n):
    F = [0] * (n + 1)
    F[0] = 0
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]


resultado = fibonacciList(10)
print(resultado)


