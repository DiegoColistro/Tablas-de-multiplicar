def solicitud_numero():
    global tabla
    tabla = int(input("Introduzca un número: "))


def tabla_multiplicar():
    for x in range(11):
        print("{} * {} = {}".format(tabla, x, x * tabla))


if __name__ == "__main__":
    while 1 <= 10:
        solicitud_numero()
        tabla_multiplicar()
