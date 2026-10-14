from src.repositories.mapa_repository import MapaRepository, NodoConocimiento

class MapaService:
    def __init__(self, repository: MapaRepository):
        self.repository = repository

    def crear_nodo(self, id_nodo, nombre, descripcion=""):
        nodo_existente = self.repository.obtener_nodo(id_nodo)
        if nodo_existente:
            raise ValueError(f"El nodo con ID {id_nodo} ya existe.")
        nuevo_nodo = NodoConocimiento(id_nodo, nombre, descripcion)
        return self.repository.guardar_nodo(nuevo_nodo)

    def conectar_nodos(self, id_origen, id_prerrequisito):
        nodo_origen = self.repository.obtener_nodo(id_origen)
        nodo_prereq = self.repository.obtener_nodo(id_prerrequisito)

        if not nodo_origen or not nodo_prereq:
            raise ValueError("Uno de los nodos especificados no existe.")
        
        nodo_origen.agregar_prerrequisito(nodo_prereq)
        return nodo_origen

    def listar_mapa(self):
        return self.repository.obtener_todos()