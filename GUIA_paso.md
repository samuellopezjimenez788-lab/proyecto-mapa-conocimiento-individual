# Plan de División de Trabajo y Metodología en Git — Proyecto Mapa de Conocimiento

Este documento detalla la distribución de tareas entre Santiago y Samuel, explicando de manera detallada qué hizo cada uno, cómo lo hizo paso a paso y la secuencia exacta para gestionar el trabajo mediante ramas y commits en GitHub.

---

## 1. Diagnóstico del Estado Actual del Proyecto

* **Código Base:** Se cuenta con la lógica central del backend implementada bajo Programación Orientada a Objetos (`NodoConocimiento` y `MapaConocimiento`) en el archivo `main.py`.
* **Repositorio Base:** El repositorio individual/grupal está creado, limpio y sincronizado en la nube en la rama `main`.
* **Colaboradores:** El profesor Carlos Castro (`ccastro2050`) ya fue agregado e invitado al repositorio.
* **Documentación Inicial:** Ya se creó y subió el archivo `README.md` con la información del proyecto y las instrucciones de ejecución.

---

## 2. División Detallada del Trabajo por Integrante

### Santiago: Refactorización de Arquitectura & Desarrollo de API (Backend)

* **Tarea 1: Refactorización del código monolítico a Patrón en Capas**
  * **Qué hizo Santiago:** Extraer las clases y funciones principales de `main.py` (que resolvían la lógica central del mapa académico) y organizarlas explícitamente en capas desacopladas en lugar de tenerlo todo en un solo archivo.
  * **Cómo lo hizo paso a paso:**
    1. **Capa Repositorio (`repositories/`):** Creó clases y métodos dedicados exclusivamente al almacenamiento, recuperación y gestión de la persistencia de los objetos `NodoConocimiento` y `MapaConocimiento`.
    2. **Capa Servicio (`services/`):** Agrupó toda la lógica de negocio pura (validación de relaciones entre nodos, consultas de estados y recorridos del mapa académico)[cite: 1].
    3. **Capa Controlador (`controllers/`):** Diseñó los controladores encargados de recibir las peticiones, procesar los datos a través de los servicios y retornar las respuestas estructuradas[cite: 1].

* **Tarea 2: Construcción de la API y Endpoints**
  * **Qué hizo Santiago:** Exponer la funcionalidad del backend mediante una interfaz de programación accesible por HTTP si el proyecto lo requiere[cite: 1].
  * **Cómo lo hizo paso a paso:**
    1. Configuró el entorno e implementó los endpoints utilizando un framework web (como FastAPI o Flask)[cite: 1].
    2. Estructuró y organizó las rutas de la API para conectar las peticiones con los controladores y servicios correspondientes[cite: 1].

---

### Samuel: Spec Kit, Prompts & Interfaz de Usuario (Frontend & Documentación)

* **Tarea 1: Documentación Formal (Spec Kit y Prompts)**
  * **Qué hizo Samuel:** Redactar la documentación formal de planeación, arquitectura de software y la recopilación de los prompts iniciales que guiaron el desarrollo[cite: 1].
  * **Cómo lo hizo paso a paso:**
    1. Creó los 8 archivos Markdown / Spec Kit requeridos por la rúbrica para formalizar la planeación y el diseño del software[cite: 1].
    2. Recopiló y documentó de forma ordenada los prompts iniciales utilizados para guiar el desarrollo de la lógica del proyecto[cite: 1].
    3. Mantuvo actualizado el archivo `README.md` con la información general y las instrucciones de ejecución[cite: 1].

* **Tarea 2: Desarrollo de la Interfaz de Usuario (Frontend)**
  * **Qué hizo Samuel:** Crear la interfaz de usuario o vista conectada para interactuar con el sistema[cite: 1].
  * **Cómo lo hizo paso a paso:**
    1. Diseñó y estructuró las vistas o componentes visuales del frontend[cite: 1].
    2. Conectó la interfaz de usuario con los endpoints desarrollados por Santiago para asegurar la comunicación fluida entre el cliente y el servidor[cite: 1].

---

## 3. Pasos para Implementar la Estrategia de Ramas en Git

Para cumplir con la dinámica de ramas de Git, hacer commits ordenados de cada parte y realizar el proceso de merge integrando los cambios de ambos, Santiago y Samuel seguirán la siguiente secuencia de comandos en la terminal[cite: 1]:

### Configuración Inicial (Santiago y Samuel)
Antes de iniciar cualquier cambio, ambos deben asegurarse de tener la última versión de la rama principal:
```bash
git checkout main
git pull origin main
