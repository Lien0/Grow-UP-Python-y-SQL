User Story [US-PY-SQL-001]
Título: Persistencia de Reportes en Base de Datos (ETL Básico)

ID: PY-SQL-INT-001

Prioridad: Crítica

Nivel: Intermedio 3/5

1. Descripción (Story)
Como Desarrollador Senior,

quiero un script en Python que lea una lista de ventas, las procese con una clase y las guarde automáticamente en la base de datos,

para automatizar la carga de datos del sistema.

2. Criterios de Aceptación (AC)
AC1: Usar la librería sqlite3 (incluida en Python) para conectar con la base de datos stitch_store.db.

AC2: Implementar una función o método save_sale(product_id: int, quantity: int) que inserte registros en la tabla sales.

AC3: Manejo de Transacciones Profesional:

Uso de bloque try-except-finally.

Si la inserción es exitosa: Ejecutar connection.commit().

Si ocurre un error (ej. el producto no existe): Ejecutar connection.rollback() y mostrar el error.

Indispensable: Cerrar la conexión en el bloque finally.

AC4: Decorador: Aplicar tu decorador @log_action a la función que guarda la venta para auditar el proceso.

3. Restricciones Técnicas
Seguridad: Está prohibido usar f-strings o concatenación dentro del string de SQL. Debes usar parámetros de consulta (?) para prevenir Inyección SQL.

Automatización: El script debe incluir el comando CREATE TABLE IF NOT EXISTS sales... al inicio para que el entorno sea autogestionable.

Integridad: Asegúrate de que los product_id que intentes insertar existan en tu tabla de productos (o inserta los productos primero en el mismo script).

4. Definición de Hecho (DoD)
[ ] El script se ejecuta sin errores de "Database locked".

[ ] Al finalizar, si abres la base de datos, las filas están correctamente insertadas.

[ ] El decorador imprime el log en consola antes de cada inserción.