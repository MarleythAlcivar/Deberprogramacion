# Crear el diccionario 'informacion_personal'
informacion_personal = {
    "nombre": "Marleyth Alcivar",
    "edad": 18,
    "ciudad": "Santo Domingo"
}

print(f"1.-Crear diccionario con informacion personal{informacion_personal}")

# Acceder y modificar el valor de 'ciudad'
informacion_personal["ciudad"] = "Manta"
print(f"2.- Acceder y modificar el valor de ciudad {informacion_personal}")


# Agregar una nueva clave-valor 'profesion' con un nuevo valor
informacion_personal["profesion"] = "Ingeniera"
print(informacion_personal)

# Verificar si la clave ' numero de telefono' existe, si no, agregarlo
if "telefono" not in informacion_personal:
    informacion_personal[" numero de telefono"] = "09876545623"
print(informacion_personal)

# Eliminar la clave 'edad'
del informacion_personal["edad"]
print(informacion_personal)

# Imprimir el diccionario final
print(informacion_personal)
