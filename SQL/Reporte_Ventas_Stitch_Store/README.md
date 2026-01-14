User Story [US-SQL-003]
Título: Dashboard de Ventas y Rendimiento (Reporting) ID: SQL-ADV-001 Prioridad: Alta Nivel: Intermedio-Avanzado 2/5

1. Descripción (Story)
Como Gerente de Ventas, quiero un reporte que me diga cuánto dinero hemos generado por cada categoría de producto, para decidir qué categorías de diseño (UI vs UX) son más rentables.

2. Criterios de Aceptación (AC)
AC1: Usar la tabla products creada anteriormente.

AC2: Crear una nueva tabla sales que registre: id, product_id (FK), quantity_sold y sale_date.

AC3: Realizar un query utilizando Funciones de Agregación (SUM, COUNT).

AC4: El reporte debe mostrar: Nombre de la categoría, Total de productos vendidos en esa categoría y Ganancia total (Precio * Cantidad).

AC5: Usar la cláusula GROUP BY y filtrar solo las categorías que hayan generado más de $100.00 en ventas totales usando HAVING.

3. Restricciones Técnicas
El cálculo de ganancia debe hacerse dentro del SQL (no en Python).

Uso de JOIN para conectar ventas con productos.

Ordenar el resultado de mayor a menor ganancia.

4. Definición de Hecho (DoD)
[ ] El query calcula correctamente subtotales por grupo.

[ ] Se diferencia correctamente el uso de WHERE (filtro de filas) y HAVING (filtro de grupos).