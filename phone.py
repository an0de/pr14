class Phone:
    def __init__(
        self,
        brand: str,
        model: str,
        price: int,
        color: str,
        storage_gb: int,
        is_in_stock: bool,
    ) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.storage_gb = storage_gb
        self.is_in_stock = is_in_stock

    def get_full_name(self) -> str:
        return f"{self.brand} {self.model}"

    def apply_discount(self, discount_percent: float) -> None:
        self.price -= round(self.price * discount_percent / 100)

    def check_availability(self) -> str:
        if self.is_in_stock:
            return "В наличии"
        return "Нет в наличии"

    def __str__(self) -> str:
        in_stock = self.check_availability()
        return (
            f"{self.brand} {self.model} {self.storage_gb:d}GB "
            f"{self.color} ${self.price:d} {in_stock}"
        )


p1 = Phone("orange", "X10", 999, "black", 512, True)
p2 = Phone("orange", "X10", 899, "white", 256, True)
p3 = Phone("orange", "20", 1999, "black", 2048, False)
print(p1)
print(p1.get_full_name())
print(p2.check_availability())
print(p3)
p3.apply_discount(30)
print(p3)
