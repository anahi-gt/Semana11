# ---------------------------------------------------------
# UNIVERSIDAD ESTATAL AMAZÓNICA
# ASIGNATURA: Programación Orientada a Objetos
# TEMA: Sistema de Gestión de Inventario (Semana 11)
# ESTUDIANTE: ANAHI GREFA TAPUY
# ---------------------------------------------------------


from producto import Producto
from inventario import Inventario


def mostrar_menu():
    sistema = Inventario()

    while True:
        print("\n" + "=" * 40)
        print("  SISTEMA DE GESTIÓN DE INVENTARIO (S11)")
        print("=" * 40)
        print("1. Agregar Producto")
        print("2. Eliminar Producto por ID")
        print("3. Actualizar Cantidad/Precio")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Todo el Inventario")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            id_p = input("ID: ")
            nom = input("Nombre: ")
            can = int(input("Cantidad: "))
            pre = float(input("Precio: "))
            sistema.añadir(Producto(id_p, nom, can, pre))

        elif opcion == "2":
            id_p = input("ID a eliminar: ")
            sistema.eliminar(id_p)

        elif opcion == "3":
            id_p = input("ID del producto: ")
            can = input("Nueva cantidad (deja vacío para no cambiar): ")
            pre = input("Nuevo precio (deja vacío para no cambiar): ")
            sistema.actualizar(id_p, int(can) if can else None, float(pre) if pre else None)

        elif opcion == "4":
            nom = input("Nombre a buscar: ")
            resultados = sistema.buscar_por_nombre(nom)
            for r in resultados: print(r)

        elif opcion == "5":
            for p in sistema.productos.values(): print(p)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break


if __name__ == "__main__":
    mostrar_menu()