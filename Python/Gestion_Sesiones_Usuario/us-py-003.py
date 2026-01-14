from typing import TypedDict, List, Dict, Any, Callable
from functools import wraps

#Clase para el tipado de el usuario.
class User(TypedDict):
  name:str
  password:str
  status:str
  attempts:int


#Decorador para la funcion de login
#Para hacer un typing estricto según Fluent Python y Effective Python 
#vamos a agregar los datos que ingresan y los que retorna de una funcion
#callable, como no sabemos que datos entran y cuales salen
#aplicaremos los ... , Any y asi acepta cualquier dato
#no es completamente necesario a menos que hayas colocado deforma 
#estricta como yo en mi IDE el Pylance para la revision de código.
def log_action(func:Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args:Any, **kwargs: Any) -> Any:
      print(f"--- DEBUG: Ejecutando acción: {func.__name__.upper()} con argumentos {args} ---")

      return func(*args, **kwargs)
    
    return wrapper


# Clase para la gestion de sesiones.
class SessionManager:

  def __init__(self, users:List[User]) -> None:
    self.__capsule: Dict[str, User] = {u['name']: u for u in users }
  """
    Constructor para inicializar las variables con los 
    datos del usuario.
  """

  #Aplicamos el decorador a la función.
  @log_action
  def login(self, username:str, password:str) -> tuple[bool, str]:
    #La funcion retorna una tupla con un boleano para 
    #la gestion del estado que se encuentre el inicio de sesion
    #y una cadena de texto para mostrar lo que sucede al usuario.

    user_data:User | None = self.__capsule.get(username)

    #Filtros para comprobar los datos ingresados por el usuario.
    if not user_data:
      return False, 'El usuario no existe.'
    
    if user_data["status"] == "blocked":
      return False ,"Usuario bloqueado. Contacte a soporte."
    
    if password == user_data['password']:
      self.reset_attempts(username)
      return True, f"Bienvenido, {username}."
    
    user_data['attempts'] += 1
    if user_data["attempts"] >= 3:
      self._blocked_status(username)
      return False,"Máximo de intentos realizados. Cuenta bloqueada."
    
    if password != user_data["password"]:
      self._add_attempt(username)
      return False, f"Contraseña incorrecta." \
      f"Intento {str(self.__capsule[username]['attempts'])}/3."

    return False, "Datos incorrectos."
      
  #Metodo para agregar intentos fallidos
  def _add_attempt(self, username:str ):
    self.__capsule[username]["attempts"] += 1

  #Metodo para bloquear un usuario
  def _blocked_status(self, username:str):
    self.__capsule[username]["status"] = "blocked"

  #Metodo para desbloquear un usuario.
  def reset_attempts(self, username:str):
    if username in self.__capsule:
      self.__capsule[username]["attempts"] = 0
      self.__capsule[username]["status"] = "active"
      print(f"{'Usuario: {username} ha sido desbloqueado.':>40} ")

  def __str__(self) -> str:
        # Cumpliendo con el requerimiento US-PY-003 AC3
        active_count = sum(1 for u in self.__capsule.values() if u['status'] == 'active')
        return f"SessionManager: {len(self.__capsule)} usuarios registrados ({active_count} activos)."


print(f"{'--- Inicio de sesion: ---':^80}")
username:str = ""
password:str = ""

#Lista a usar como prueba
USERS_LIST: List[User] = [
  {
    'name': 'User 1',
    'password': '1234',
    'status': 'active',
    'attempts':0
  },
  {
    'name': 'User 2',
    'password': '12345',
    'status': 'blocked',
    'attempts': 3
  },
  {
    'name': 'User 3',
    'password': '134',
    'status': 'active',
    'attempts':1
  }
]

def login_session(u:str, p:str) -> list[str]:
  u = input(f"{'Usuario: ':>40}")
  p = input(f"{'Contraseña: ':>40}")

  return [u,p]



username,password = login_session(username, password)

new_session = SessionManager(USERS_LIST)
print(new_session)


#Version de la IA.
# from typing import TypedDict, List, Dict, Any, Callable, Tuple
# from functools import wraps

# # 1. Definición de Datos
# class User(TypedDict):
#     name: str
#     password: str
#     status: str
#     attempts: int

# # 2. Decorador Profesional (Maneja el 'self' de forma implícita)
# def log_action(func: Callable[..., Any]) -> Callable[..., Any]:
#     @wraps(func)
#     def wrapper(*args: Any, **kwargs: Any) -> Any:
#         # args[0] suele ser 'self' en métodos de clase
#         print(f"\n[AUDIT] Ejecutando: {func.__name__.upper()} | Args: {args[1:]}")
#         return func(*args, **kwargs)
#     return wrapper

# # 3. Gestor de Sesiones
# class SessionManager:
#     def __init__(self, users_list: List[User]):
#         # Encapsulamiento: El diccionario vive en la instancia
#         self.__users: Dict[str, User] = {u["name"]: u for u in users_list}

#     @log_action
#     def login(self, username: str, password: str) -> Tuple[bool, str]:
#         """Retorna (Exito, Mensaje)"""
#         user = self.__users.get(username)

#         if not user:
#             return False, "Usuario no encontrado."

#         if user["status"] == "blocked":
#             return False, "ACCESO DENEGADO: Cuenta bloqueada. Contacte a soporte."

#         if user["password"] == password:
#             self.reset_attempts(username)
#             return True, f"Bienvenido, {username}."
        
#         # Lógica de Intento Fallido
#         user["attempts"] += 1
#         if user["attempts"] >= 3:
#             user["status"] = "blocked"
#             return False, "ALERTA: Demasiados intentos. Cuenta bloqueada ahora."
        
#         return False, f"Password incorrecto. Intento {user['attempts']}/3"

#     def reset_attempts(self, username: str) -> None:
#         if username in self.__users:
#             self.__users[username]["attempts"] = 0
#             self.__users[username]["status"] = "active"

#     def __str__(self) -> str:
#         # Cumpliendo con el requerimiento US-PY-003 AC3
#         active_count = sum(1 for u in self.__users.values() if u['status'] == 'active')
#         return f"SessionManager: {len(self.__users)} usuarios registrados ({active_count} activos)."

# # --- Simulación de Uso Profesional ---
# if __name__ == "__main__":
#     db_mock: List[User] = [
#         {'name': 'admin', 'password': 'root', 'status': 'active', 'attempts': 0},
#         {'name': 'editor', 'password': '123', 'status': 'active', 'attempts': 0}
#     ]

#     manager = SessionManager(db_mock)
#     print(manager) # Llama a __str__

#     # Simulación de ataque de fuerza bruta
#     for i in range(4):
#         success, msg = manager.login("admin", "wrong_pass")
#         print(f"Resultado: {msg}")
#         if not success and "bloqueada" in msg:
#             break