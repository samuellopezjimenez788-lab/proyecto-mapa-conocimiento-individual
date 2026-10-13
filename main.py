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
        self.nodos = {}

    def agregar_nodo(self, nodo):
        if nodo.id_nodo not in self.nodos:
            self.nodos[nodo.id_nodo] = nodo

    def mostrar_mapa(self):
        print("\n=== MAPA DE CONOCIMIENTO ACADÉMICO ===")
        for nodo in self.nodos.values():
            print(f"- Tema: {nodo.titulo} (ID: {nodo.id_nodo})")
            print(f"  Descripción: {nodo.descripcion}")
            if nodo.conexiones:
                print("  Prerrequisitos / Conexiones:")
                for conexion in nodo.conexiones:
                    print(f"    -> {conexion.titulo}")
            else:
                print("  -> Tema inicial (Sin prerrequisitos)")
            print("-" * 40)
        print("======================================")


# Bloque de prueba principal con más temas
if __name__ == "__main__":
    mi_mapa = MapaConocimiento()

    # Creamos los nodos
    nodo_algoritmos = NodoConocimiento("01", "Algoritmos", "Lógica de programación y resolución de problemas")
    nodo_python = NodoConocimiento("02", "Python Básico", "Sintaxis, variables y estructuras de control")
    nodo_bd = NodoConocimiento("03", "Bases de Datos Relacionales", "Modelado de datos y SQL")

    # Agregamos los nodos al mapa
    mi_mapa.agregar_nodo(nodo_algoritmos)
    mi_mapa.agregar_nodo(nodo_python)
    mi_mapa.agregar_nodo(nodo_bd)

    # Configuramos las dependencias / conexiones
    nodo_python.agregar_conexion(nodo_algoritmos)
    nodo_bd.agregar_conexion(nodo_algoritmos)

    # Mostramos el mapa completo
    mi_mapa.mostrar_mapa()