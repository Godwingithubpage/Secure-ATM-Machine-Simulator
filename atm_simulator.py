import hashlib
import getpass

# User's data (for simplicity, the hashed password is stored here)
users = {
    # Store the hashed password
    "Uche G": hashlib.sha256("password123".encode()).hexdigest(),
    "Godwin Ifeanyi": hashlib.sha256("mypassword".encode()).hexdigest()
}

# Define the initial balance
balance = 1000  # Assume the user starts with CHF 1000 in their Swiss bank account


def authenticate():
    """Authenticate user by checking if the entered password is correct."""
    username = input("Enter your username: ")

    if username in users:
        # Hide the password input
        password = getpass.getpass("Enter your password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if the hashed version of the password matches the stored one
        if users[username] == hashed_password:
            print("Authentication successful!")
            return True
        else:
            print("Invalid password. Authentication failed.")
            return False
    else:
        print("User not found.")
        return False


def display_menu():
    """Display the menu for the ATM."""
    print("\nATM Machine Simulator")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


def check_balance():
    """Display the current balance."""
    print(f"Your current balance is: CHF {balance}")


def deposit_money():
    """Allow the user to deposit money."""
    global balance  # Use 'global' to modify the 'balance' variable defined outside the function
    try:
        amount = float(input("Enter amount to deposit: CHF "))
        if amount > 0:
            balance += amount
            print(
                f"Successfully deposited CHF {amount}. Your new balance is: CHF {balance}")
        else:
            print("Deposit amount must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")


def withdraw_money():
    """Allow the user to withdraw money."""
    global balance
    try:
        amount = float(input("Enter amount to withdraw: CHF "))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                print(
                    f"Successfully withdrew CHF {amount}. Your new balance is: CHF {balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")


# Main program loop
if __name__ == "__main__":
    # Authenticate before accessing ATM
    if authenticate():
        while True:
            display_menu()  # Show the menu
            choice = input("Choose an option: ")

            if choice == "1":
                check_balance()

            elif choice == "2":
                deposit_money()

            elif choice == "3":
                withdraw_money()

            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid option. Please choose a valid option.")
