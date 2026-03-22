# Sistema de Gestión de Inventario para Laboratorio

Este es el repositorio de nuestro poryecto final para la clase de Programacion II.
El objetivo de este programa es simular el funcionamiento de un Sistema de administracion de un laboratorio

## Estado del Proyecto
Este código corresponde al **primer avance** del proyecto. Por ahora, el enfoque principal está en la arquitectura de las clases y demostrar que las herencias funcionan correctamente

En este avance los datos se guardan en la memoria temporal durante la ejecucion del programa, el objetivo final es utilizar el almacenamiento de datos para la siguiente entrega

## Conceptos de POO implementados
Para este avance, me aseguré de incluir los requisitos principales solicitados:

* **Clases y Objetos:** Separación de lógica en diferentes módulos (`GestorInventario`, `SistemaLaboratorio`, etc.).
* **Herencia Simple:** Clases como `ReactivoQuimico` y `EquipoSeguridad` heredan de clases padre más generales (`Consumible` y `Equipamiento`).
* **Herencia Múltiple:** La clase `ReactivoCritico` hereda tanto de `ReactivoQuimico` para sus propiedades físicas como de la clase `Auditoria` para registrar quién y por qué usa un material peligroso.
* **Metodos:** Uso de Métodos: Implementación de funciones específicas dentro de las clases (como `mostrar_inventario` o `consumir_stock_critico`) para procesar la información y generar salidas limpias en la consola.
##  Cómo ejecutar la demostración

No se necesita instalar ninguna librería extra.

1. Abre la carpeta del proyecto en tu editor (PyCharm) o en la terminal.
2. Ejecuta el archivo principal:
   
   "main.py"

### Equipo de Desarrollo
Este proyecto fue desarrollado por:

**Grupo C12:**
* **Álvaro Imanol Castillo Romero** - Usuario: aicr5@alu.ua.es
* **Gonzalo Gómez Ruiz** - Usuario: ggr33@alu.ua.es

*2026 - Universidad de Alicante | Ingenieria en Inteligencia Artificial*