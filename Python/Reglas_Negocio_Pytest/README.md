User Story [US-PY-ADV-001]
Título: Validación de Reglas de Negocio con PyTest ID: PY-ADV-001 Prioridad: Alta Nivel: Avanzado 1/5

1. Descripción (Story)
Como Líder de QA, quiero asegurar que el motor de cálculo de impuestos y descuentos de la tienda sea infalible, para evitar pérdidas financieras por errores de redondeo o lógica en el backend.

2. Criterios de Aceptación (AC)
AC1: Implementar el módulo finance_engine.py con la clase FinanceCalculator.

AC2: El método calculate_final_price(base_price: float, discount_pct: float) debe realizar:

Aplicación del descuento sobre el precio base.

Aplicación del IVA (16%) sobre el precio ya descontado.

Redondeo final a 2 decimales.

AC3: Gestión de Errores: Debe lanzar una excepción personalizada llamada NegativePriceError si el base_price es menor a cero.

AC4: Suite de Pruebas: Crear test_finance.py utilizando PyTest. Debes cubrir:

Un caso de éxito con valores estándar.

Un caso de borde (ej. descuento del 100%).

Una prueba de excepción que verifique el lanzamiento de NegativePriceError ante precios negativos.

3. Restricciones Técnicas
Arquitectura: Separación total entre la lógica de negocio (finance_engine.py) y el código de pruebas (test_finance.py).

Estándar: Uso estricto de Type Hints y cumplimiento de PEP 8.

Herramientas: Solo se permite el uso de pytest (instálalo con pip install pytest si no lo tienes).

4. Definición de Hecho (DoD)
[ ] El comando pytest se ejecuta en la terminal y todos los tests (mínimo 3) pasan con éxito (en verde).

[ ] La excepción personalizada está correctamente definida y capturada en los tests.

[ ] No existen errores de redondeo (ej. 10.555 debe ser 10.56 o 10.55 según la lógica financiera estándar).