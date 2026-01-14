from decimal import Decimal, ROUND_HALF_EVEN


class NegativePriceError(Exception):
  """Clase creada para reportar un valor negativo."""
  pass

class FinanceCalculator:
  __IVA: Decimal = Decimal('0.16')
  def __init__(self):
    pass

  def calculate_final_price(self, base_price:float, discount_pct:float) -> Decimal:
    if base_price < 0: 
      raise NegativePriceError("Error: El precio base no puede ser negativo.")
    new_base_price: Decimal = Decimal(str(base_price))
    new_discount_pct: Decimal = Decimal(str(discount_pct))
    neto:Decimal = new_base_price - (new_base_price * (new_discount_pct / 100))
    total:Decimal = neto + (neto * self.__IVA)
    total_rounded:Decimal = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
    return total_rounded



if __name__ == "__main__":
  print('Primera prueba')
  base_price:float = float(input("Precio. "))
  discount_pct:float = float(input("Porcentaje de descuento. "))
  calculator = FinanceCalculator()
  print(f"Total: {calculator.calculate_final_price(base_price,discount_pct)}")