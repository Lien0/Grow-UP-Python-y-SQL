User Story [US-PY-001]
Título: Sistema de Registro de Transacciones de Fintech (MVP) ID: PY-INI-001 Prioridad: Alta Nivel: Inicial 1/5

1. Descripción (Story)
Como Desarrollador Backend Junior en una startup de Fintech, quiero crear un módulo de consola que permita capturar y procesar las transacciones financieras del día, para asegurar que los datos de los usuarios se registren correctamente antes de ser procesados por el motor contable.

2. Criterios de Aceptación (AC)
AC1: El programa debe solicitar por consola los datos de 3 transacciones. Por cada una: Nombre del comercio, Categoría (ej. Comida, Transporte, Salud) y Monto (float).

AC2: Validación de Datos: El monto debe ser un número positivo. Si el usuario ingresa un valor menor o igual a cero, el sistema debe notificar el error y solicitar el dato nuevamente hasta que sea válido (uso de un bucle while).

AC3: Al finalizar la captura, el sistema debe aplicar un impuesto simulado del 16% (IVA) a cada transacción y mostrar un reporte detallado.

AC4: El reporte final debe mostrar:

Cada transacción con su monto original, el IVA calculado y el total (monto + IVA).

El Gran Total de todas las transacciones sumadas (incluyendo impuestos).

3. Restricciones Técnicas
PEP 8: Nombramiento de variables en snake_case.

Type Hinting: Debes usar anotaciones de tipo en la medida de lo posible (ej. monto: float = 0.0).

Formateo: Uso obligatorio de f-strings para el reporte final, asegurando que los valores monetarios muestren exactamente 2 decimales.

Estructuras: Uso de una lista para almacenar las transacciones (puedes usar diccionarios o tuplas para representar cada transacción dentro de la lista).

4. Definición de Hecho (DoD)
[ ] El código sigue las guías de estilo de Effective Python (Item 2: Follow the PEP 8 Style Guide).

[ ] No hay errores de lógica en el cálculo del IVA.

[ ] La validación de entrada evita que el programa procese números negativos.

[ ] El código es legible y está comentado donde sea estrictamente necesario.