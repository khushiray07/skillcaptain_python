class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

user_db = []
def register_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if "@" not in email or "." not in email:
        print("Invalid email format!")
        return

    for user in user_db:
        if user.email == email:
            print("Email already registered!")
            return

    new_user = User(name, email, password)

    user_db.append(new_user)
    print("Registration successful!")


while True:
    choice = input("\nDo you want to register a new user? (yes/no): ").lower()
    if choice == "yes":
        register_user()
    else:
        print("\nRegistered Users:")
        for u in user_db:
            u.display_info()
            print("-" * 20)
        break
