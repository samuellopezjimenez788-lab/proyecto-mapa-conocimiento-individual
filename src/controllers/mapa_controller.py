from src.services.mapa_service import MapaService

class MapaController:
    def __init__(self, service: MapaService):
        self.service = service

    def inicializar_datos_prueba(self):
        # Creamos nodos base
        self.service.crear_nodo("PROG1", "Fundamentos de Programación", "Lógica y Python básico")
        self.service.crear_nodo("POO", "Programación Orientada a Objetos", "Clases, herencia y polimorfismo")
        self.service.crear_nodo("BD", "Bases de Datos", "Modelado relacional y SQL")

        # Conectamos prerrequisitos
        self.service.conectar_nodos("POO", "PROG1")
        self.service.conectar_nodos("BD", "PROG1")

    def mostrar_mapa_consola(self):
        print("\n--- MAPA DE CONOCIMIENTO ACADÉMICO ---")
        nodos = self.service.listar_mapa()
        for nodo in nodos:
            print(f"\n[Tema]: {nodo.nombre} (ID: {nodo.id_nodo})")
            print(f"Descripción: {nodo.descripcion}")
            if nodo.prerrequisitos:
                print("Prerrequisitos:")
                for prereq in nodo.prerrequisitos:
                    print(f"  - {prereq.nombre}")
            else:
                print("Prerrequisitos: Ninguno")
        print("--------------------------------------\n")