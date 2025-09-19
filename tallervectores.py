from os import name


def mostrar_menu():
    print("\n--- MENU DE OPCIONES ---")
    print("1. Agregar usuario (append)")
    print("2. Agregar varios usuarios (extend)")
    print("3. Insertar usuario en posicion especifica (insert)")
    print("4. Eliminar usuario por nombre (remove)")
    print("5. Eliminar usuario por posicion (pop)")
    print("6. Buscar posicion de un usuario (index)")
    print("7. Contar repeticiones de un usuario (count)")
    print("8. Ordenar usuarios (sort)")
    print("9. Invertir lista (reverse)")
    print("10. Mostrar lista de usuarios")
    print("11. Finalizar")


def agregar_usuario(lista):
    usuario = input("Ingrese el nombre del usuario a agregar: ")
    lista.append(usuario)
    print("Usuario agregado con append")


def agregar_varios(lista):
    usuarios = input("Ingrese varios usuarios separados por coma: ").split(",")
    lista.extend([u.strip() for u in usuarios])
    print("Usuarios agregados con extend")


def insertar_usuario(lista):
    usuario = input("Ingrese el nombre del usuario a insertar: ")
    pos = int(input("Ingrese la posicion: "))
    lista.insert(pos, usuario)
    print("Usuario insertado con insert")


def eliminar_usuario(lista):
    usuario = input("Ingrese el nombre del usuario a eliminar: ")
    lista.remove(usuario)
    print("Usuario eliminado con remove")


def eliminar_posicion(lista):
    pos = int(input("Ingrese la posicion a eliminar: "))
    eliminado = lista.pop(pos)
    print(f"Usuario {eliminado} eliminado con pop")


def buscar_usuario(lista):
    usuario = input("Ingrese el nombre del usuario a buscar: ")
    pos = lista.index(usuario)
    print(f"El usuario {usuario} esta en la posicion {pos}")


def contar_usuario(lista):
    usuario = input("Ingrese el nombre del usuario a contar: ")
    cantidad = lista.count(usuario)
    print(f"El usuario {usuario} aparece {cantidad} veces")


def ordenar_lista(lista):
    lista.sort()
    print("Lista ordenada con sort")


def invertir_lista(lista):
    lista.reverse()
    print("Lista invertida con reverse")


def mostrar_lista(lista):
    print("\nLista de usuarios")
    for i, usuario in enumerate(lista):
        print(f"{i}. {usuario}")


def menu_principal():
    usuarios = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_usuario(usuarios)
        elif opcion == "2":
            agregar_varios(usuarios)
        elif opcion == "3":
            insertar_usuario(usuarios)
        elif opcion == "4":
            eliminar_usuario(usuarios)
        elif opcion == "5":
            eliminar_posicion(usuarios)
        elif opcion == "6":
            buscar_usuario(usuarios)
        elif opcion == "7":
            contar_usuario(usuarios)
        elif opcion == "8":
            ordenar_lista(usuarios)
        elif opcion == "9":
            invertir_lista(usuarios)
        elif opcion == "10":
            mostrar_lista(usuarios)
        elif opcion == "11":
            print("Finalizando programa")
            break
        else:
            print("Opcion no valida")


if name == "main":
    menu_principal()
