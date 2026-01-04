User Story [US-SQL-001]
Título: Modelado del Esquema de Catálogo para "Stitch Store" ID: SQL-INI-001 Prioridad: Alta Nivel: Inicial 1/5

1. Descripción (Story)
Como Desarrollador Backend, quiero diseñar y crear la tabla inicial de productos para mi plataforma (donde venderás componentes de UI/UX), para asegurar que la información del catálogo se guarde de forma persistente y estructurada.

2. Criterios de Aceptación (AC)
AC1: Crear una base de datos llamada stitch_store_db y una tabla llamada products.

AC2: La tabla debe tener las siguientes columnas:

id: Serial/Autoincremental (Primary Key).

name: Nombre del componente (ej. "Navbar Premium"). No nulo.

category: Categoría (ej. "Web", "Mobile").

price: Precio unitario (Uso de tipo de dato preciso para dinero).

stock_quantity: Cantidad disponible (Entero).

created_at: Fecha de registro automática.

AC3: Insertar 3 registros de prueba.

AC4: Realizar una consulta que muestre el nombre y el precio de los productos que cuesten más de $50.00, ordenados de más caro a más barato.

3. Restricciones Técnicas
Seguir la 3ra Forma Normal (3NF) aunque sea una tabla simple.

Nombres de tablas y columnas en snake_case.

Prohibido usar FLOAT o REAL para la columna price (Consultar SQL Antipatterns).

4. Definición de Hecho (DoD)
[ ] El script SQL es compatible con PostgreSQL o MySQL.

[ ] Se definieron correctamente las llaves primarias y restricciones de nulidad.

[ ] El query de selección filtra y ordena correctamente.