# Definimos la función aplicar_descuento que toma dos parámetros:
# - cantidad: el valor al que se va a aplicar el descuento.
# - porcentaje_descuento: el porcentaje de descuento que se aplicará. Si no se especifica, usará 20% por defecto.
def aplicar_descuento(cantidad, porcentaje_descuento=20):
    # Calculamos el descuento multiplicando la cantidad por el porcentaje de descuento y dividiendo por 100.
    resultado = cantidad * porcentaje_descuento / 100
    # Retornamos el valor del descuento calculado.
    return resultado


# Definimos la función menu que se encargará de mostrar las opciones del menú al usuario.
def menu():
    # Mostramos un mensaje de título para que el usuario sepa de qué trata el programa.
    print("Deber de Programación: Aplicar Descuento")
    # Mostramos las opciones disponibles.
    print("1. Aplicar descuento por defecto (20%)")
    print("2. Aplicar un descuento personalizado")
    print("3. Salir")


# Iniciamos un bucle infinito con 'while True' para que el menú siga apareciendo hasta que el usuario elija salir.
while True:
    # Llamamos a la función menu() para mostrar las opciones.
    menu()

    # Pedimos al usuario que elija una opción y la guardamos en la variable 'opcion'.
    opcion = input("Elija una opción: ")

    # Verificamos si la opción elegida es '1' (descuento por defecto del 20%).
    if opcion == '1':
        # Pedimos al usuario que ingrese la cantidad sobre la que quiere calcular el descuento.
        cantidad = float(input("Ingrese la cantidad que desea calcular: "))
        # Llamamos a la función aplicar_descuento con la cantidad y el descuento por defecto (20%).
        print(f"El descuento aplicado es: {aplicar_descuento(cantidad)}")

    # Verificamos si la opción elegida es '2' (descuento personalizado).
    elif opcion == '2':
        # Pedimos al usuario que ingrese la cantidad sobre la que quiere calcular el descuento.
        cantidad = float(input("Ingrese la cantidad que desea calcular: "))
        # Pedimos al usuario que ingrese el porcentaje de descuento personalizado.
        descuento = float(input("Ingrese el porcentaje de descuento personalizado: "))
        # Llamamos a la función aplicar_descuento con la cantidad y el descuento personalizado.
        print(f"El descuento personalizado es: {aplicar_descuento(cantidad, descuento)}")

    # Verificamos si la opción elegida es '3' (salir del programa).
    elif opcion == '3':
        # Mostramos un mensaje de despedida.
        print("Saliendo del programa...")
        # Salimos del bucle,


