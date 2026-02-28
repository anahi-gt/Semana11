import os
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = {} # Diccionario para búsqueda rápida
        self.archivo = "inventario.txt"
        self.cargar_desde_archivo()

    def añadir(self, producto):
        if producto.get_id() in self.productos:
            print("Error: El ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_en_archivo()
            print("Producto añadido correctamente.")

    def eliminar(self, id_p):
        if id_p in self.productos:
            del self.productos[id_p]
            self.guardar_en_archivo()
            print("Producto eliminado.")
        else:
            print("No se encontró el ID.")

    def actualizar(self, id_p, cantidad=None, precio=None):
        if id_p in self.productos:
            if cantidad is not None: self.productos[id_p].set_cantidad(cantidad)
            if precio is not None: self.productos[id_p].set_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

    # --- PERSISTENCIA EN ARCHIVOS ---
    def guardar_en_archivo(self):
        with open(self.archivo, "w") as f:
            for p in self.productos.values():
                # ¡CORREGIDO!: Ahora usa get_precio() en lugar de get_price()
                f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")

    def cargar_desde_archivo(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        p = Producto(datos[0], datos[1], int(datos[2]), float(datos[3]))
                        self.productos[datos[0]] = p