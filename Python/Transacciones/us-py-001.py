from typing import TypedDict, List

class Transaction(TypedDict):
    commerce_name: str
    category: str
    value: float
    tax: float
    total:float

#Clases deben estar en PascalCase
class TransactionProcessor: 
    #Constante para evitar numeros magicos en el codigo
    IVA_RATE: float = 0.16
    def __init__(self, name:str, cat:str, val: float):
        self.name: str = name
        self.cat: str = cat
        self.val: float = val


    def _calculate_tax(self) -> float:
        return self.val * self.IVA_RATE

    def get_final_report(self) -> Transaction:
        tax:float = self._calculate_tax()
        
        return {
            "commerce_name": self.name,
            "category": self.cat,
            "value": self.val,
            "tax": tax,
            "total": self.val + tax
        }
    




j = 0
transaction_reports: List[Transaction] = []
for i in range(3):
    print(f"\nCaptura de transacción {i+1}")
    commerce:str = input("Ingresa el nombre del comercio: ")
    category:str = input("Ingresa la categoría en la que se encuentra: ")

    while True:
        try:
            val = float(input("Ingresa el monto: "))
            if(val < 0): raise ValueError
            break
        except ValueError:
            print("Hubo un error el valor debe de ser un número con el siguiente " \
            "formato 0.00 evita cualquier caracter especial y debe ser positivo.")

    processor = TransactionProcessor(commerce, category, val)
    transaction_reports.append(processor.get_final_report())

#Formateo de decimales a dos con f-string 
for t in transaction_reports:
    print(f"\n--- Ticket: {t['commerce_name']} ---")
    print(f"Subtotal: ${t['value']:>10.2f}")
    print(f"IVA:      ${t['tax']:>10.2f}")
    print(f"Total:    ${t['total']:>10.2f}")

gran_total = sum(item['total'] for item in transaction_reports)
print(f"Gran total: ${gran_total:.2f}")

input("\nPresione Enter para salir...")







