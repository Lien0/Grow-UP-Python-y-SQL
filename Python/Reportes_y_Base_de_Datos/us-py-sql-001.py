from typing import TypedDict, Dict, Optional, List, Callable, Any, Tuple, cast
import sqlite3 
from functools import wraps

#Clase de tipado para cada producto
class Product(TypedDict):
  id:int
  name:str
  price:float
  stock_quantity:int

#Clase de tipado para los tickets
class Transaction(TypedDict):
    commerce_name: str
    value: float
    tax: float
    total:float

#######################################################################
#Decorador para auditar guardado de compra en base de datos.
def sale_auditor(func:Callable[..., Any]) -> Callable[..., Any]:
  @wraps(func)
  def wrapper(*args: Any,**kwargs: Any ) -> Any:
    print(f"\n{'-'*5} {'Guardando compra, ejecutando: '}{func.__name__.upper()} {'-'*5}")
    return func(*args, **kwargs)
  return wrapper

#######################################################################
#Inicio de clase con metodos Sale Manager
class SaleManager:
  def __init__(self, db_path: str = "stitch_store.db"):
    self.db_path = db_path
    self._setup_db()
    self.products: Dict[str, Product] = self._load_products()

  def _get_connection(self):
    conn = sqlite3.connect(self.db_path)
    conn.row_factory = sqlite3.Row # Permite acceso por nombre: row['name']
    return conn

  def _setup_db(self):
    with self._get_connection() as conn:
        cursor = conn.cursor()

        cursor.executescript("""
          PRAGMA foreign_keys = ON; -- VITAL en SQLite para que funcionen las FK

          CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            category TEXT,
            price REAL NOT NULL,
            stock_quantity INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
          );

          CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity_sold INTEGER NOT NULL DEFAULT 0,
            sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(product_id) REFERENCES products(id)
          );
        """)

        initial_products = [
          ('Navbar', 'UI Design', 25.20, 2),
          ('Footer', 'UI Design', 57.20, 5),
          ('Dashboard Layout', 'UX Design', 88.30, 6)
        ]

        cursor.executemany("""
          INSERT OR IGNORE INTO products (name, category, price, stock_quantity) 
          VALUES (?, ?, ?, ?)
        """, initial_products)
        conn.commit()

  def _load_products(self) -> Dict[str, Product]:
    with self._get_connection() as conn:
        cursor = conn.cursor()
        rows = cursor.execute("SELECT * FROM products").fetchall()
        return {row['name']: cast(Product, dict(row)) for row in rows}


  def show_products(self):
    print(f"{'-'*20} {'Productos Disponibles'} {'-'*20}")
    for p in self.products:
      print(f"{'Producto:'} {self.products[p]['name']:<20} {'Precio:'}" \
          f" {self.products[p]['price']:<10} {'Stock:'} {self.products[p]['stock_quantity']}")


  def process_purchase(self, p:str, q:int) -> Optional[Tuple[int, int, str,float]]:
    #Uso de optional ya que no sabemos si lo que va a retornar .get
    #es el producto o es None
    selected_product: Optional[Product] = self.products.get(p)

    if not selected_product or selected_product['stock_quantity'] < q:
      return None
    
    selected_product['stock_quantity'] -= q
    return selected_product['id'], q, selected_product['name'], selected_product['price']    

  @sale_auditor
  def save_sale(self, id:int, q:int, stock:int):

    with self._get_connection() as conn:
      try:
        cursor = conn.cursor()

        cursor.execute("""
          INSERT INTO sales (product_id, quantity_sold) VALUES (?, ?)
        """, (id, q))

        cursor.execute("""
          UPDATE products SET stock_quantity = ? WHERE id = ?
        """, (stock, id))
        conn.commit()
      # print(f"Save product id: {id} quantity: {q}")
    
      except Exception as e:
        conn.rollback()
        print(f"Exception save sale failed. {e}")


#######################################################################
#Clase para la creacion de tickets
class TransactionProcessor: 
    #Constante para evitar numeros magicos en el codigo
    IVA_RATE: float = 0.16
    def __init__(self, name:str, val: float):
        self.name: str = name
        self.val: float = val


    def _calculate_tax(self) -> float:
        return self.val * self.IVA_RATE

    def get_final_report(self) -> Transaction:
        tax:float = self._calculate_tax()
        
        return {
            "commerce_name": self.name,
            "value": self.val,
            "tax": tax,
            "total": self.val + tax
        }
    

#######################################################################
#Declaracion de variables.
new_sale = SaleManager()
new_sale.show_products()
add_products: Dict[str, Tuple[int, int, str, float]] = {}
tickets: List[Transaction] = []

#Funcion para seleccionar un producto usando la clase de SaleManager
def product_select() -> Optional[Tuple[int, int, str, float]]:
    p = input(f"{'Nombre del producto.':>20} ")
    q = int(input(f"{'Cantidad:':>40} "))
    new_product: Tuple[int, int, str, float] | None = new_sale.process_purchase(p,q)
    return new_product

#While para agregar varios productos verificados a el directorio add_products
print(f"{'Seleccion de productos:':^40}")
while True:
  new_product = product_select()
  if new_product:
    add_products[new_product[2]] = new_product
    flag = input(f"{'Deseas agregar otro producto?':>10} {'Si':>10} {'No':>10}. ")
    if flag.upper() == "NO": break

#Funcion para guardar las compras.
def save_sales():
  for p in add_products:
    new_sale.save_sale(add_products[p][0], add_products[p][1], new_sale.products[add_products[p][2]]['stock_quantity'])
    processor = TransactionProcessor(add_products[p][2], add_products[p][3])
    tickets.append(processor.get_final_report())

  

#Imprimir el ticket de las compras.
save_sales()
print(f"\n{'-'*10} {'Ticket de compra'} {'-'*10}")
for t in tickets:
    print(f"\n--- Ticket: {t['commerce_name']} ---")
    print(f"Subtotal: ${t['value']:>10.2f}")
    print(f"IVA:      ${t['tax']:>10.2f}")
    print(f"Total:    ${t['total']:>10.2f}")

gran_total = sum(item['total'] for item in tickets)
print(f"Gran total: ${gran_total:.2f}")

input("\nPresione Enter para salir...")










    

