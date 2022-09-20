def solicitud_numero():
    tabla_de_multiplicar = int(input("Introduzca un número: "))
    return tabla_de_multiplicar


def tabla_multiplicar():
    for x in range(11):
        print("{} * {} = {}".format(tabla_general, x, x * tabla_general))


if __name__ == "__main__":
    tabla_general = (solicitud_numero())
    tabla_multiplicar()