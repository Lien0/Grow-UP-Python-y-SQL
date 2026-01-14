from typing import List, Dict

logs: List[str] = ['user1','admin','user1','user2','user1','user2','admin','guest','user2','user1','admin']

def count_attempts(user_list: List[str]) -> Dict[str,int]:
  """
    La funcion recibe una lista de cadenas de texto y regresa
    un diccionario con clave cadena de texto y valor numero entero.

    Iniciamos la funcion creando un diccionario vacío.

    Inicia un solo bucle el cual recorre toda la lista.

    Ingresa la clave como el nombre de usuario logueado de la 
    lista proporcionada si la clave existe, por definicion
    de directorio actualiza su valor, si la clave no existe
    por definicion de directorio crea una nueva con valor 1.

    Posterior regresa el directorio con las claves de los usuarios
    con sus intentos de logueo.
  """
  logs_attempts: Dict[str,int] = {}

  for user in user_list:
      logs_attempts[user] = logs_attempts.get(user,0) + 1

  return logs_attempts


try:
    results = count_attempts(logs)
    max_user = ""
    max_value = 0

    print("Reporte de intentos sospechosos (Mayor a 2)")

    for u, c in results.items():
        if c > 2:
            print(f"Alerta: El usuario [{u}] tuvo {c} intentos.")
        
        if c > max_value:
            max_value = c
            max_user = u

    print("-" * 40)
    print(f"Análisis terminado. Usuario con mayor actividad: {max_user} ({max_value}) veces.")

except Exception as e:
    print(f"Error inesperado en el sistema: {e}")


    #AI Version:


# Constantes en MAYÚSCULAS (PEP 8)
# LOG_DATA: List[str] = [
#     'user1', 'admin', 'user1', 'user2', 'user1', 
#     'user2', 'admin', 'guest', 'user2', 'user1', 'admin'
# ]

# def count_attempts(user_list: List[str]) -> Dict[str, int]:
#     """
#     Procesa una lista de usuarios y cuenta sus apariciones.
    
#     Args:
#         user_list: Lista de nombres de usuario (strings).
        
#     Returns:
#         Diccionario con el conteo de intentos por usuario.
        
#     Lección Aprendida: Complejidad O(n). Recorremos la lista una sola vez.
#     """
#     attempts_dict: Dict[str, int] = {}

#     for user in user_list:
#         # LECCIÓN: .get(key, 0) evita el KeyError que ocurre al intentar
#         # sumar 1 a una llave que aún no existe en el diccionario.
#         attempts_dict[user] = attempts_dict.get(user, 0) + 1
    
#     return attempts_dict

# def generate_security_report(attempts: Dict[str, int], threshold: int = 2):
#     """
#     Analiza los intentos y detecta al usuario con mayor actividad.
#     """
#     max_user: str = ""
#     max_value: int = 0

#     print(f"{'--- REPORTE DE SEGURIDAD ---':^40}")
#     print(f"{'USUARIO':<20} | {'INTENTOS':<10}")
#     print("-" * 40)

#     for user, count in attempts.items():
#         # AC3: Filtrado de sospechosos
#         if count > threshold:
#             print(f"{user:<20} | {count:<10} [ALERTA]")

#         # LECCIÓN O(n): Encontrar el máximo en la misma pasada del bucle.
#         # Evita el error 'RuntimeError' al NO intentar borrar (del) 
#         # elementos del diccionario mientras se itera.
#         if count > max_value:
#             max_value = count
#             max_user = user

#     print("-" * 40)
#     # Formateo profesional con f-strings (2 decimales o alineación)
#     print(f"Usuario con mayor actividad: {max_user.upper()}")
#     print(f"Total de intentos: {max_value}")

# # --- Bloque de Ejecución Principal ---
# if __name__ == "__main__":
#     try:
#         results = count_attempts(LOG_DATA)
#         generate_security_report(results)
#     except Exception as e:
#         # En producción, esto iría a un logger, no solo a print.
#         print(f"Error crítico en el motor de análisis: {e}")
