class NodoConocimiento:
    def __init__(self, id_nodo, titulo, descripcion):
        self.id_nodo = id_nodo
        self.titulo = titulo
        self.descripcion = descripcion
        self.conexiones = []

    def agregar_conexion(self, nodo):
        if nodo not in self.conexiones:
            self.conexiones.append(nodo)

    def __str__(self):
        return f"[{self.id_nodo}] {self.titulo}"


class MapaConocimiento:
    def __init__(self):
        self.nodos = {}  # Diccionario para guardar todos los nodos del mapa

    def agregar_nodo(self, nodo):
        """Agrega un nodo al mapa general."""
        if nodo.id_nodo not in self.nodos:
            self.nodos[nodo.id_nodo] = nodo

    def mostrar_mapa(self):
        """Muestra todos los temas y sus respectivas conexiones."""
        print("\n=== MAPA DE CONOCIMIENTO ===")
        for nodo in self.nodos.values():
            print(f"- Tema: {nodo.titulo} (ID: {nodo.id_nodo})")
            if nodo.conexiones:
                print("  Prerrequisitos / Conexiones:")
                for conexion in nodo.conexiones:
                    print(f"    -> {conexion.titulo}")
            else:
                print("  -> Sin conexiones previas")
        print("============================")


# Bloque de prueba principal
if __name__ == "__main__":
    # 1. Inicializamos el mapa
    mi_mapa = MapaConocimiento()

    # 2. Creamos los nodos
    nodo_algoritmos = NodoConocimiento("01", "Algoritmos", "Lógica de programación")
    nodo_python = NodoConocimiento("02", "Python Básico", "Sintaxis básica")
    
    # 3. Agregamos los nodos al mapa
    mi_mapa.agregar_nodo(nodo_algoritmos)
    mi_mapa.agregar_nodo(nodo_python)

    # 4. Conectamos Python a Algoritmos
    nodo_python.agregar_conexion(nodo_algoritmos)

    # 5. Mostramos el mapa completo en consola
    mi_mapa.mostrar_mapa()