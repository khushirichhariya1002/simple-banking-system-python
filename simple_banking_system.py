import datetime

def log_action(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)   
        
        with open("bank_log.txt", "a") as file:
            file.write(
                f"{datetime.datetime.now()} -- {func.__name__}({args[0]}) -- Balance: {self._Account__balance}\n"
            )
        
        return result
    return wrapper


class Account:
    def __init__(self, name, account_no, balance=0):
        self.__name = name
        self.__acc_no = account_no
        self.__balance = balance
        self.history = []

    @log_action
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.__balance += amount
        self.history.append(f"Deposited {amount}")

    @log_action
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.__balance:
            raise ValueError("Insufficient balance!")
        self.__balance -= amount
        self.history.append(f"Withdrawn {amount}")

    def show_balance(self):
        return self.__balance

    def show_history(self):
        return self.history


if __name__ == "__main__":
    print("Welcome to Simple Banking System")
    name = input("Enter your name: ")
    acc_number = int(input("Enter your account number: "))

    acc = Account(name, acc_number, 0)

    while True:
        print("\n---- MENU ----")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Show Balance Only")
        print("4. Show History Only")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                acc.deposit(amount)
                print("\n Deposit Successful!")
                
                print("\nUpdated Balance:", acc.show_balance())
                print("Updated Transaction History:")
                for h in acc.show_history():
                    print("-", h)

            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                acc.withdraw(amount)
                print("\n Withdrawal Successful!")
                
                print("\nUpdated Balance:", acc.show_balance())
                print("Updated Transaction History:")
                for h in acc.show_history():
                    print("-", h)

            elif choice == "3":
                print("Current Balance:", acc.show_balance())

            elif choice == "4":
                print("Transaction History:")
                for h in acc.show_history():
                    print("-", h)

            elif choice == "5":
                print("Thank you! Exiting system...")
                break

            else:
                print("Invalid choice! Please select between 1–5.")
        
        except Exception as e:
            print("Error:", e)

    print("Transaction log saved in bank_log.txt")
