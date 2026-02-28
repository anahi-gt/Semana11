class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Usamos guiones bajos para el encapsulamiento
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos para obtener atributos (Getters)
    def get_id(self): return self._id
    def get_nombre(self): return self._nombre
    def get_cantidad(self): return self._cantidad
    def get_precio(self): return self._precio

    # Métodos para modificar atributos (Setters)
    def set_cantidad(self, cantidad): self._cantidad = cantidad
    def set_precio(self, precio): self._precio = precio

    def __str__(self):
        return f"ID: {self._id} | Producto: {self._nombre} | Stock: {self._cantidad} | Precio: ${self._precio}"