from src.repositories.mapa_repository import MapaRepository
from src.services.mapa_service import MapaService
from src.controllers.mapa_controller import MapaController

def main():
    # Inicializamos las capas
    repo = MapaRepository()
    service = MapaService(repo)
    controller = MapaController(service)

    # Cargamos datos de prueba y mostramos el mapa
    controller.inicializar_datos_prueba()
    controller.mostrar_mapa_consola()

if __name__ == "__main__":
    main()