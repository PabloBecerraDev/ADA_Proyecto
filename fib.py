import time
import matplotlib.pyplot as plt

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacciList(n):
    F = [0] * (n + 1)
    F[0] = 0
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

def medirTiempo(f, n):
    inicio = time.time()
    f(n)
    fin = time.time()
    return fin - inicio


valores_n = [3, 5, 7, 10]


tiempos_recursivo = [medirTiempo(fibonacci, n) for n in valores_n]
tiempos_lista = [medirTiempo(fibonacciList, n) for n in valores_n]

#Graficar resultados
plt.plot(valores_n, tiempos_recursivo, label='Recursivo')
plt.plot(valores_n, tiempos_lista, label='Lista')
plt.xlabel('n')
plt.ylabel('Tiempo (s)')
plt.title('Comparación de tiempo entre Fibonacci recursivo y con lista')
plt.legend()
plt.show()

for i in tiempos_recursivo:
    print(i)

for i in tiempos_lista:
    print(i)