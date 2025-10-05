from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ₹{self.price:.2f}")
        print(f"Quantity: {self.quantity}")

product_db: list[Product] = []

def read_nonempty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Please enter a non-empty value.")

def read_float(prompt: str, min_value: float = 0.0) -> float:
    while True:
        try:
            x = float(input(prompt))
            if x >= min_value:
                return x
            print(f"Please enter a number ≥ {min_value}.")
        except ValueError:
            print("Please enter a valid number.")

def read_int(prompt: str, min_value: int = 0) -> int:
    while True:
        try:
            x = int(input(prompt))
            if x >= min_value:
                return x
            print(f"Please enter an integer ≥ {min_value}.")
        except ValueError:
            print("Please enter a valid integer.")

def register_product():
    print("\n Register a Product ")
    name = read_nonempty("Product name: ")
    price = read_float("Price: ₹")
    quantity = read_int("Quantity: ")

    prod = Product(name=name, price=price, quantity=quantity)
    product_db.append(prod)
    save_to_file(prod)  
    print(f" Registered: {name}")

def save_to_file(product: Product, filename: str = "products.csv"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{product.name},{product.price},{product.quantity}\n")

def display_all_products():
    print("\n=== Registered Products ===")
    if not product_db:
        print("No products registered yet.")
        return
    for i, p in enumerate(product_db, start=1):
        print(f"\nProduct {i}:")
        p.display_info()

def main():
    while True:
        print("\n--- Product Registration System ---")
        print("1. Register a new product")
        print("2. View all registered products")
        print("3. Exit")
        choice = input("Choose 1/2/3: ").strip()

        if choice == "1":
            register_product()
        elif choice == "2":
            display_all_products()
        elif choice == "3":
            print("Bye")
            break
        else:
            print("Invalid choice.try again.")

if __name__ == "__main__":
    main()
