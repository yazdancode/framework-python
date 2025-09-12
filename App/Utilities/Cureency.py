class Cureency:
    @staticmethod
    def format_price_in_hezar_toman(amount) -> int:
        return amount / 1000

    @staticmethod
    def format_price_in_toman(amount) -> int:
        return amount

    @staticmethod
    def format_price_in_rial(amount) -> int:
        return amount * 10
