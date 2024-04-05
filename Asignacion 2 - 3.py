def superDigito(n):
    if n < 10:
        return n
    else:
        sumaDigitos = sum(int(digit) for digit in str(n))
        return superDigito(sumaDigitos)

print(superDigito(12345))

