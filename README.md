# Sistema de Gestión de Inventario para Laboratorio

Este es el repositorio de nuestro proyecto final para la clase de Programación II.
El objetivo de este programa es simular el funcionamiento de un Sistema de administración de un laboratorio

## Estado del Proyecto
Este código corresponde al **segundo avance** del proyecto. En esta etapa, hemos consolidado la arquitectura avanzada de clases y el sistema de herencias, enfocando los esfuerzos principales en el desarrollo y finalización de la interfaz de usuario por consola para interactuar con el laboratorio de forma intuitiva. El sistema ya cuenta con menús dinámicos, sobrecarga de operadores para comparar elementos y un control estricto de excepciones (`try-except`) ante datos inválidos. Actualmente, la información se administra en la memoria temporal durante la ejecución del programa, quedando como único objetivo pendiente la implementación de la persistencia de datos (almacenamiento en archivos) para la entrega final.


## Conceptos de POO implementados
Para este avance, me aseguré de incluir los requisitos principales solicitados:

## Conceptos de POO implementados
Para este avance, me aseguré de incluir los requisitos principales solicitados:

* **Clases y Objetos:** Separación de lógica en diferentes módulos (`GestorInventario`, `SistemaLaboratorio`, etc.).
* **Herencia Simple:** Clases como `ReactivoQuimico` y `EquipoSeguridad` heredan de clases padre más generales (`Consumible` y `Equipamiento`).
* **Herencia Múltiple:** Las clases críticas (`ReactivoQuimicoCritico` y `MaterialBiologicoCritico`) heredan tanto de su rama de consumibles para sus propiedades físicas, como de la clase `Auditoria` para registrar de manera independiente quién y por qué usa un material peligroso.
* **Sobrecarga de Operadores (Polimorfismo):** Se implementó polimorfismo mediante métodos mágicos nativos de Python. Se sobrecargó el operador de igualdad (`__eq__`) en métodos personalizados como `mismo_estado()` y `misma_ubicacion()` para comparar lógicamente si dos piezas de equipamiento comparten propiedades idénticas en el sistema sin necesidad de evaluar atributo por atributo de forma externa.
* **Manejo y Excepción de Errores:** El sistema cuenta con bloques de control `try-except` estratégicos para capturar excepciones del tipo `ValueError`. Esto previene de forma activa el colapso (*crash*) de la aplicación por consola si el usuario introduce accidentalmente caracteres alfabéticos en campos estrictamente numéricos (como cantidades, niveles de stock o umbrales críticos), garantizando la continuidad del bucle principal del programa.
* **Métodos:** Implementación de funciones específicas dentro de las clases (como `mostrar_inventario` o `consumir_stock_critico`) para procesar la información y generar salidas limpias en la consola.
* **Clases y Métodos Abstractos:** Se usó la clase `ItemInventario` como clase abstracta con dos objetivos principales: que los objetos por definir sean obligatoriamente `Consumibles` o `Equipamientos` específicos evitando así la creación de objetos genéricos, además se usó el método `mostrar_detalles()` como contrato obligatorio para que las clases hijas definan su lógica de visualización, garantizando que el Gestor de Inventario pueda interactuar de manera estandarizada con cualquier elemento del laboratorio.

## Estructura del Proyecto
El proyecto se encuentra modularizado en paquetes lógicos para facilitar el mantenimiento y escalabilidad del sistema:

```text
trabajo-final-c12/
│
├── clases/
│   ├── base/
│   │   └── clase_itemInventario.py         # Clase abstracta principal
│   │
│   ├── consumibles/
│   │   ├── clase_consumible.py             # Clase base para consumibles
│   │   ├── clase_reactivoQuimico.py        # Reactivos estándar
│   │   ├── reactivo_quimico_critico.py     # Reactivos peligrosos con Auditoría
│   │   ├── clase_materialBiologico.py       # Material biológico estándar
│   │   └── material_biologico_critico.py   # Material biológico peligroso con Auditoría
│   │
│   ├── equipos/
│   │   ├── clase_equipamiento.py           # Clase base para equipos de laboratorio
│   │   ├── clase_equipoSeguridad.py        # Duchas, extintores, etc.
│   │   └── clase_intrumentoAnalitico.py    # Microscopios, centrífugas, etc.
│   │
│   └── inventario/
│       ├── clase_gestorInventario.py       # Motor del inventario (Lista de objetos)
│       ├── auditoria.py                    # Mixin para control de uso crítico
│       └── clase_sistemaLaboratorio.py     # Interfaz de usuario por consola
│
├── main.py                                 # Script de inicio del sistema
└── mypy.ini                                # Archivo de configuración estricta de tipos
````

##  Cómo ejecutar la demostración

No se necesita instalar ninguna librería extra.

1. Abre la carpeta del proyecto en tu editor (PyCharm) o en la terminal.
2. Ejecuta el archivo principal:
   
  ### **"python main.py"**

## Equipo de Desarrollo
Este proyecto fue desarrollado por:

**Grupo C12:**
* **Álvaro Imanol Castillo Romero** - Usuario: aicr5@alu.ua.es
* **Gonzalo Gómez Ruiz** - Usuario: ggr33@alu.ua.es

*2026 - Universidad de Alicante | Ingeniería en Inteligencia Artificial*