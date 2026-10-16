def aplicar(funcion, valor):
    return funcion(valor)


def crear_multiplicador(factor):
    def multiplicar(x):
        return x * factor
    return multiplicar


def despedir(nombre):
    return f"Adios {nombre}"


g = despedir
print(g("Ana"))


def cuadrado(x):
    return x ** 2


print(aplicar(str.upper, "python"))
print(aplicar(abs, -7))
print(aplicar(cuadrado, 4))


def crear_sumador(n):
    def sumar(x):
        return x + n
    return sumar


sumar10 = crear_sumador(10)
print(sumar10(5))

doble = crear_multiplicador(2)
triple = crear_multiplicador(3)
funciones = [doble, triple, cuadrado]
for f in funciones:
    print(f(4))    