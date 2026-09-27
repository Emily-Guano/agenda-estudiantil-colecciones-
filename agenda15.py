# Tarea - Manejo de colecciones de datos
# Estudiante: Emily Brianna Guano Paccha
# Problema: Agenda de contactos estudiantiles

# COLECCIONES USADAS
# Diccionario: relaciona nombre -> telefono
# Lista: mantiene el orden de registro
# Conjunto: evita telefonos duplicados

contactos = {}
historial_orden = []
numeros_registrados = set()

def agregar_contacto():
    # Inserta/agrega datos
    nombre = input("Ingrese nombre: ").strip().title()
    telefono = input("Ingrese telefono: ").strip()

    if telefono in numeros_registrados:
        print(">> Error: El telefono ya esta registrado.")
        return

    contactos[nombre] = telefono
    historial_orden.append(nombre)
    numeros_registrados.add(telefono)
    print(f">> Contacto '{nombre}' agregado con exito.")

def mostrar_contactos():
    # Muestra de forma clara la informacion
    if not contactos:
        print(">> No hay contactos para mostrar.")
        return

    print("\n--- LISTADO DE CONTACTOS ---")
    # Recorrer elementos - operacion adicional
    for i, (nombre, telefono) in enumerate(contactos.items(), 1):
        print(f"{i}. Nombre: {nombre} | Tel: {telefono}")
    print(f"Total registrados: {len(contactos)}")
    print(f"Orden de registro (lista): {historial_orden}")

def buscar_contacto():
    # Operacion adicional: Buscar
    nombre = input("Nombre a buscar: ").strip().title()
    if nombre in contactos:
        print(f">> Encontrado: {nombre} - Tel: {contactos[nombre]}")
    else:
        print(">> Contacto no encontrado.")

def eliminar_contacto():
    # Operacion adicional: Eliminar
    nombre = input("Nombre a eliminar: ").strip().title()
    if nombre in contactos:
        telefono_eliminado = contactos.pop(nombre)
        numeros_registrados.discard(telefono_eliminado)
        print(f">> Contacto '{nombre}' eliminado correctamente.")
    else:
        print(">> No existe ese contacto.")

def menu():
    while True:
        print("\n=== AGENDA ESTUDIANTIL ===")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Seleccione una opcion (1-5): ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    menu()
