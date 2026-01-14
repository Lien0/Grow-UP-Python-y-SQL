User Story [US-PY-003]
Título: Sistema de Gestión de Sesiones de Usuario (Auth Manager) ID: PY-INT-001 Prioridad: Alta Nivel: Intermedio 1/5

1. Descripción (Story)
Como Desarrollador de Seguridad, quiero una clase en Python que administre las sesiones de los usuarios, para controlar quién está logueado y bloquear automáticamente a los que superen un límite de intentos fallidos.

2. Criterios de Aceptación (AC)
AC1: Crear una clase SessionManager. Debe tener un atributo privado (encapsulado) que sea un diccionario para rastrear los intentos fallidos de cada usuario.

AC2: Método login(username, password):

Si el usuario ya está bloqueado, debe retornar "Usuario bloqueado. Contacte a soporte".

Si el password es incorrecto (puedes simular uno hardcodeado), debe sumar un intento fallido.

Si llega a 3 intentos fallidos, el estado del usuario debe cambiar a "Blocked".

AC3: Método reset_attempts(username): Debe limpiar los intentos fallidos de un usuario específico.

AC4: Uso de Decoradores: Crea un decorador simple @log_action que imprima en consola "Ejecutando acción: [nombre_del_metodo]" cada vez que se llame a login.

3. Restricciones Técnicas
POO: Usa encapsulamiento (prefijo __ para atributos privados).

Fluent Python: Implementa el método especial __str__ para que al imprimir el objeto SessionManager muestre cuántos usuarios hay en el sistema.

PEP 8: Tipado de datos (Type Hints) en todos los métodos.

4. Definición de Hecho (DoD)
[ ] La clase maneja correctamente el estado de "Bloqueado".

[ ] El decorador funciona y no rompe la ejecución.

[ ] Se evidencia el uso de lógica de diccionarios dentro de la clase.