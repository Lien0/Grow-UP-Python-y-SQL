from finance_engine import FinanceCalculator, NegativePriceError
from decimal import Decimal
import pytest

@pytest.fixture
def calculator_default() -> FinanceCalculator:
  instance = FinanceCalculator()
  return instance

def test_success_calculate(calculator_default:FinanceCalculator):
  result:Decimal = calculator_default.calculate_final_price(10.0,10.0)
  assert result == Decimal('10.44')

def test_border_calculate(calculator_default:FinanceCalculator):
  result: Decimal = calculator_default.calculate_final_price(50.0, 100.0)
  assert result == Decimal(0)

def test_negative_price(calculator_default:FinanceCalculator):
  with pytest.raises(NegativePriceError) as excinfo:
    calculator_default.calculate_final_price(-20.0,20.0)

  assert "Error: El precio base no puede ser negativo." in str(excinfo.value)




