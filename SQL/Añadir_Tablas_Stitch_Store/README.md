User Story [US-SQL-002]
Título: Implementación de Auditoría de Accesos y Relaciones ID: SQL-INT-001 Prioridad: Alta Nivel: Intermedio 1/5

1. Descripción (Story)
Como DBA de la plataforma, quiero normalizar la base de datos separando la información de los usuarios de sus intentos de acceso, para mantener la integridad referencial y optimizar las consultas de auditoría.

2. Criterios de Aceptación (AC)
AC1: Crear una tabla users con: id (PK), username (Único), email y status (ej. 'active', 'blocked').

AC2: Crear una tabla login_logs con:

id (PK).

user_id: Una Foreign Key (FK) que conecte con la tabla users.

attempt_date: Fecha y hora del intento (Timestamp).

ip_address: Dirección IP del intento.

AC3: Insertar 2 usuarios en la tabla users.

AC4: Insertar 5 intentos de acceso en login_logs repartidos entre esos 2 usuarios.

AC5: Consulta (Join): Realizar un INNER JOIN que muestre el username y la fecha de todos los intentos de acceso fallidos (puedes añadir una columna is_successful boolean si lo deseas).

3. Restricciones Técnicas
Normalización: El diseño debe cumplir estrictamente con la 3ra Forma Normal (3NF).

Integridad: La FK en login_logs debe tener una restricción ON DELETE CASCADE (si borro al usuario, se borran sus logs).

Rendimiento: Crea un Índice (INDEX) en la columna attempt_date para acelerar búsquedas históricas (Basado en SQL Performance Explained).

4. Definición de Hecho (DoD)
[ ] El script SQL define correctamente las relaciones uno-a-muchos (1:N).

[ ] No hay redundancia de nombres de usuario en la tabla de logs (solo IDs).

[ ] El JOIN funciona correctamente devolviendo datos combinados de ambas tablas.