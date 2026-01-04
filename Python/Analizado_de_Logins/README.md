User Story [US-PY-002]

Título: Analizador de Frecuencia de Logins (Ciberseguridad) ID: PY-INI-002 Prioridad: Media Nivel: Inicial 2/5

1. Descripción (Story)

Como Analista de Seguridad de "Stitch Store", quiero un programa que procese una lista de nombres de usuario que han intentado ingresar al sistema, para identificar quiénes han tenido intentos fallidos repetidos y detectar posibles ataques de fuerza bruta.

2. Criterios de Aceptación (AC)

AC1: El programa debe recibir una lista de strings (puedes hardcodear la lista al inicio). Ejemplo: ['user1', 'admin', 'user1', 'guest', 'admin', 'admin'].

AC2: Debes crear una función llamada count_attempts(user_list: List[str]) -> Dict[str, int] que devuelva un diccionario donde la llave sea el nombre de usuario y el valor sea cuántas veces aparece en la lista.

AC3: El reporte final debe imprimir solo los usuarios que tienen más de 2 intentos.

AC4: Debes identificar al "Usuario con mayor actividad" (el que más veces aparece).

3. Restricciones Técnicas

Algoritmo: No uses el método .count() de las listas dentro de un bucle (eso elevaría la complejidad a $O(n^2)$). Intenta resolverlo en un solo paso ($O(n)$) usando un diccionario.

Typing: Uso de Dict y List de la librería typing.

PEP 8: Docstrings descriptivos para la función.

4. Definición de Hecho (DoD)
[ ] El código es eficiente (Complejidad Lineal $O(n)$).
[ ] La salida por consola es clara y profesional.
[ ] Se aplican f-strings para el reporte.