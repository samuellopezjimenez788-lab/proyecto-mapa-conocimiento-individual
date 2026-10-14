class NodoConocimiento:
    def __init__(self, id_nodo, nombre, descripcion=""):
        self.id_nodo = id_nodo
        self.nombre = nombre
        self.descripcion = descripcion
        self.prerrequisitos = []

    def agregar_prerrequisito(self, nodo):
        if nodo not in self.prerrequisitos:
            self.prerrequisitos.append(nodo)


class MapaRepository:
    def __init__(self):
        self.nodos = {}

    def guardar_nodo(self, nodo):
        self.nodos[nodo.id_nodo] = nodo
        return nodo

    def obtener_nodo(self, id_nodo):
        return self.nodos.get(id_nodo)

    def obtener_todos(self):
        return list(self.nodos.values())