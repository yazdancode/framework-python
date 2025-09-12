from constants.Constants import CurrencyUnit


class Currency:
    @staticmethod
    def convert(amount: int, unit: CurrencyUnit) -> float:
        if unit == CurrencyUnit.RIAL:
            return amount * 10
        elif unit == CurrencyUnit.TOMAN:
            return amount
        elif unit == CurrencyUnit.HEZAR_TOMAN:
            return amount / 1000
        else:
            raise ValueError("واحد پولی نامعتبر است")

    @staticmethod
    def format_string(amount: int, unit: CurrencyUnit) -> str:
        converted = Currency.convert(amount, unit)
        return f"{converted:,.0f} {unit.value}"
