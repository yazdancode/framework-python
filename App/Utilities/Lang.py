class Lang:
    @staticmethod
    def persian_numbers(input: str) -> str:
        latin = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        persian = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
        for l, p in zip(latin, persian):
            input = input.replace(l, p)
        return input

    @staticmethod
    def latin_numbers(input: str) -> str:
        persian = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
        arabic = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩']
        latin = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for p, l in zip(persian, latin):
            input = input.replace(p, l)
        for a, l in zip(arabic, latin):
            input = input.replace(a, l)
        return input
