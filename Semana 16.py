# Crear un nuevo archivo llamado notas_personales.txt en modo escritura.
archivo_notas = open('notas_personales.txt', 'w')  # Si no existe, lo crea; si existe, lo abre para escribir

# Escribir varias notas personales en el archivo utilizando el método write().
archivo_notas.write('Mi banda favorita es INSPIRACIÓN CRISTIANA.\n')
archivo_notas.write('La mejor canción de INSPIRACIÓN CRISTIANA es VENCERÉ.\n')

# Escribir varias líneas a la vez utilizando el método writelines().
notas_adicionales = [
    'También disfruto el reguetón cristiano y coritos antiguos.\n',
    'A veces escucho romance cristiano.\n',
    'Prefiero la música cristiana en inglés, pero en español siento que las canciones son mejor.\n'
]
archivo_notas.writelines(notas_adicionales)  # Escribe todas las líneas de una sola vez

# Cerrar el archivo después de escribir.
archivo_notas.close()

# Lectura del archivo de texto:
# Abrir el archivo notas_personales.txt en modo lectura.
archivo_notas = open('notas_personales.txt', 'r')  # Abrir el archivo en modo lectura
linea_actual = archivo_notas.readline()  # Leer la primera línea del archivo

# Leer el archivo línea por línea hasta que no haya más contenido.
while linea_actual:
    print(linea_actual.strip())  # Imprimir la línea sin espacios en blanco adicionales
    linea_actual = archivo_notas.readline()  # Leer la siguiente línea

# Cerrar el archivo después de la lectura.
archivo_notas.close()
