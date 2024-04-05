import timeit
import matplotlib.pyplot as plt


#algoritmo recursivo
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


#algoritmo iterativo con arreglo
def fibonacciList(n):
    F = [0] * (n + 1)
    F[0] = 0
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

valores_n = [3, 5, 7, 10]


# funcion encargada de medir la ducion de los algoritmos
def medirTiempo(f, n):
    tiempoTomado = timeit.timeit(lambda: f(n), number=1)
    return tiempoTomado

tiempos_recursivo = [medirTiempo(fibonacci, n) for n in valores_n]
tiempos_lista = [medirTiempo(fibonacciList, n) for n in valores_n]


#grafica que representa los tiempos 
plt.plot(valores_n, tiempos_recursivo, label='Recursivo')
plt.plot(valores_n, tiempos_lista, label='Lista')
plt.xlabel('n')
plt.ylabel('Tiempo (s), T(n)')
plt.title('Comparación de tiempo entre Fibonacci recursivo y con lista')
plt.legend()
plt.show()

