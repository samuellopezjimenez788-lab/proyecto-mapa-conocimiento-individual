# Arquitectura del Software - Mapa de Conocimiento

## 1. Patrón de Diseño: Arquitectura por Capas
El proyecto está estructurado bajo una separación estricta de responsabilidades en tres capas principales para garantizar la escalabilidad, mantenibilidad y orden del código backend:

### 📄 Repositorios (`/src/repositories`)
* **Propósito:** Encapsular la persistencia y la gestión de los datos en memoria.
* **Componentes:** Contiene la clase `MapaRepository` y la estructura de los nodos (`NodoConocimiento`), encargados exclusivamente de almacenar, consultar y estructurar la información sin lógica de negocio.

### ⚙️ Servicios (`/src/services`)
* **Propósito:** Contener la lógica de negocio y las reglas de procesamiento.
* **Componentes:** La clase `MapaService` procesa las reglas de validación (como verificar si un nodo ya existe o validar la existencia de prerrequisitos antes de conectarlos).

### 🎮 Controladores (`/src/controllers`)
* **Propósito:** Manejar la interacción, entrada/salida y presentación de resultados al usuario.
* **Componentes:** La clase `MapaController` inicializa los datos de prueba y coordina la visualización del mapa académico en la consola.